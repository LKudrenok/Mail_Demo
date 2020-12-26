from flask import Flask, render_template, request, redirect, url_for

from prediction import PricePredictor, ERROR_PRICE
import data


app = Flask(__name__)

price_predictor = PricePredictor()


@app.route('/price')
def price_page():
    predicted_price = int(request.args['predicted_price'])
    if predicted_price == ERROR_PRICE:
        success = False
    else:
        success = True
    return render_template('prediction.html', price=predicted_price, success=success)


@app.route('/', methods=['POST', 'GET'])
def form_page():
    context = dict()
    context['property_type'] = data.property_type
    context['neighbourhood_cleansed'] = data.neighbourhood_cleansed
    context['room_type'] = data.room_type
    context['bed_type'] = data.bed_type
    context['amenities'] = data.amenities
    context['cancellation_policy'] = data.cancellation_policy_displayed

    if request.method == 'POST':
        form_data = dict()

        # text features
        form_data['place_name'] = request.form.get('place_name')
        form_data['summary'] = request.form.get('summary')
        form_data['description'] = request.form.get('description')
        form_data['neighborhood_overview'] = request.form.get('neighborhood_overview')
        form_data['notes'] = request.form.get('notes')
        form_data['house_rules'] = request.form.get('house_rules')
        form_data['host_about'] = request.form.get('host_about')

        # reviews
        form_data['reviews'] = request.form.get('reviews')

        # amenities
        form_data['amenities'] = request.form.getlist('amenities')

        # other features
        form_data['host_since'] = request.form.get('host_since')
        form_data['experiences_offered'] = request.form.get('experiences_offered')
        form_data['neighbourhood_cleansed'] = request.form.get('neighbourhood_cleansed')
        form_data['latitude'] = request.form.get('latitude')
        form_data['longitude'] = request.form.get('longitude')
        form_data['property_type'] = request.form.get('property_type')
        form_data['room_type'] = request.form.get('room_type')
        form_data['bed_type'] = request.form.get('bed_type')
        form_data['cancellation_policy'] = request.form.get('cancellation_policy')
        form_data['accommodates'] = request.form.get('accommodates')
        form_data['bathrooms'] = request.form.get('bathrooms')
        form_data['bedrooms'] = request.form.get('bedrooms')
        form_data['beds'] = request.form.get('beds')
        form_data['guests_included'] = request.form.get('guests_included')
        form_data['extra_people'] = request.form.get('extra_people')
        form_data['minimum_nights'] = request.form.get('minimum_nights')
        form_data['security_deposit'] = request.form.get('security_deposit')
        form_data['cleaning_fee'] = request.form.get('cleaning_fee')
        form_data['require_guest_profile_picture'] = request.form.get('require_guest_profile_picture')
        form_data['require_guest_phone_verification'] = request.form.get('require_guest_phone_verification')

        predicted_price = price_predictor.predict(form_data)
        return redirect(url_for('price_page', predicted_price=predicted_price))

    return render_template('form.html', **context)


if __name__ == '__main__':
    app.run(debug=False)
