import traceback
import pickle
from datetime import datetime

import pandas as pd
import numpy as np
import catboost
from geopy.distance import great_circle
from scipy import spatial
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import data


ERROR_PRICE = -1

TEXT_FEATURES = ['place_name', 'summary', 'description', 'neighborhood_overview',
                 'notes', 'house_rules', 'host_about']
NUMERICAL_FEATURES = ['latitude', 'longitude', 'accommodates', 'bathrooms', 'bedrooms', 'beds',
                      'guests_included', 'extra_people', 'minimum_nights', 'security_deposit',
                      'cleaning_fee']
BOOL_FEATURES = ['require_guest_profile_picture', 'require_guest_phone_verification']

CENTER = {'latitude': 51.50906022294971, 'longitude': -0.1279480991633811}


class NeighboursCounter:
    def __init__(self):
        self.neighbours = pd.read_csv('models/neighbours.csv', index_col=0)
        self.tree = spatial.KDTree(self.neighbours.to_numpy())
        self.thresholds = [0.5, 1, 1.5, 2]
        self.thresholds_degree = [t / 111.319 for t in self.thresholds]

    def query(self, coordinates: tuple) -> list:
        other = spatial.KDTree([coordinates])
        result = self.tree.count_neighbors(other, r=self.thresholds_degree)
        return result


class PricePredictor:
    def __init__(self):
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        with open('models/vectorizer.pickle', 'rb') as vectorizer_file:
            self.vectorizer = pickle.load(vectorizer_file)
        self.text_model = catboost.CatBoostRegressor().load_model('models/text.catboost')
        self.amenities_model = catboost.CatBoostRegressor().load_model('models/amenities.catboost')
        self.final_model = catboost.CatBoostRegressor().load_model('models/final.catboost')

        self.neighbourhood_mean = pd.read_csv('models/neighbourhood_mean.csv', index_col=0)
        self.neighbourhood_count = pd.read_csv('models/neighbourhood_count.csv', index_col=0)
        self.property_type_mean = pd.read_csv('models/property_type_mean.csv', index_col=0)
        self.room_type_mean = pd.read_csv('models/room_type_mean.csv', index_col=0)

    def predict(self, data_: dict) -> int:
        try:
            data_ = self.handle_form_data(data_)
            preprocessed_data = self.preprocess_data(data_)
            preprocessed_data['avail_ratio'] = 0.3386712

            review_score, reviews_count = self.get_sentiment_score(data_['reviews'])
            preprocessed_data['review_score'] = review_score
            preprocessed_data['reviews_count'] = review_score

            combined_text = ' '.join([data_[feature] for feature in TEXT_FEATURES])
            text_prediction = self.get_text_prediction(combined_text)
            preprocessed_data['text_price'] = text_prediction

            preprocessed_data['amenity_mean'] = self.get_amenities_prediction(data_['amenities'])

            preprocessed_data = preprocessed_data[data.final_model_features]
            price = self.final_model.predict(preprocessed_data)
            price = np.exp(price[0])
        except Exception as e:
            traceback.print_exc()
            price = ERROR_PRICE

        return int(price)

    def handle_form_data(self, data_: dict) -> dict:
        data_['host_since'] = datetime.strptime(data_['host_since'], '%Y-%m-%d')

        for numerical_feature in NUMERICAL_FEATURES:
            if data_[numerical_feature] == '':
                data_[numerical_feature] = 0.0
            else:
                data_[numerical_feature] = float(data_[numerical_feature])

        for bool_feature in BOOL_FEATURES:
            data_[bool_feature] = bool(int(data_[bool_feature]))

        data_['cancellation_policy'] = self.process_cancellation_policy(data_['cancellation_policy'])

        return data_

    def get_text_prediction(self, text: str) -> float:
        text_vectorized = self.vectorizer.transform([text])
        text_vectorized = np.array(text_vectorized.todense(), dtype=np.float16)
        prediction = np.exp(self.text_model.predict(text_vectorized))
        return prediction[0]

    def get_amenities_prediction(self, amenities: list) -> float:
        all_amenities = data.amenities + data.amenities_additional
        df = pd.DataFrame(columns=all_amenities, index=[0])
        df.fillna(0, inplace=True)
        for amenity in amenities:
            df[amenity] = 1
        df['total_count'] = len(amenities)
        prediction = np.exp(self.amenities_model.predict(df))
        return prediction[0]

    def get_sentiment_score(self, text: str) -> (float, int):
        reviews = str(text)
        if reviews == '':
            return 0, 0

        reviews = reviews.split('\n')
        reviews_count = len(reviews)
        cumulative_score = 0
        for review in reviews:
            review_score = self.sentiment_analyzer.polarity_scores(review.strip())['compound']
            cumulative_score += review_score
        sentiment_score = cumulative_score / reviews_count
        return sentiment_score, reviews_count

    def preprocess_data(self, raw_data: dict) -> pd.DataFrame:
        df = pd.DataFrame(index=[0])

        for col in BOOL_FEATURES + NUMERICAL_FEATURES:
            df[col] = raw_data[col]
        df['cancellation_policy'] = raw_data['cancellation_policy']

        df['host_is_superhost'] = False
        df['host_has_profile_pic'] = True
        df['host_identity_verified'] = True

        df['special_experience'] = False if raw_data['experiences_offered'] == 'none' else True
        df['good_bed'] = True if raw_data['bed_type'].lower() in ['airbed', 'real bed'] else False
        df['neighbourhood_mean'] = self.neighbourhood_mean.loc[raw_data['neighbourhood_cleansed']].values[0]
        df['neighbourhood_count'] = self.neighbourhood_count.loc[raw_data['neighbourhood_cleansed']].values[0]
        df['room_type_mean'] = self.room_type_mean.loc[raw_data['room_type']].values[0]
        df['property_type_mean'] = self.property_type_mean.loc[raw_data['property_type']].values[0]
        df['host_duration_months'] = (datetime.today() - raw_data['host_since']).days // 30

        df['distance_from_center_km'] = self.calc_distance_from_center(raw_data['latitude'], raw_data['longitude'])
        count_neighbors = neighbour_counter.query((raw_data['latitude'], raw_data['longitude']))
        for i, threshold in enumerate(neighbour_counter.thresholds):
            df[f'Count_dst_{threshold}'] = count_neighbors[i]
        df.drop(['latitude', 'longitude'], axis=1, inplace=True)

        return df

    @staticmethod
    def calc_distance_from_center(latitude: float, longitude: float) -> float:
        dist = great_circle((latitude, longitude), (CENTER['latitude'], CENTER['longitude']))
        return dist.km

    @staticmethod
    def process_cancellation_policy(string: str) -> str:
        index = data.cancellation_policy_displayed.index(string)
        return data.cancellation_policy[index]


neighbour_counter = NeighboursCounter()
