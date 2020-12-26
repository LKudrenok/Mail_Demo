neighbourhood_cleansed = ['Barking and Dagenham', 'Barnet', 'Bexley', 'Brent', 'Bromley', 'Camden', 'City of London',
                          'Croydon', 'Ealing', 'Enfield', 'Greenwich', 'Hackney', 'Hammersmith and Fulham', 'Haringey',
                          'Harrow', 'Havering', 'Hillingdon', 'Hounslow', 'Islington', 'Kensington and Chelsea',
                          'Kingston upon Thames', 'Lambeth', 'Lewisham', 'Merton', 'Newham', 'Redbridge', 'Richmond upon Thames',
                          'Southwark', 'Sutton', 'Tower Hamlets', 'Waltham Forest', 'Wandsworth', 'Westminster']

property_type = ['Aparthotel', 'Apartment', 'Barn', 'Bed and breakfast', 'Boat',
                 'Boutique hotel', 'Bungalow', 'Bus', 'Cabin', 'Camper/RV',
                 'Casa particular (Cuba)', 'Chalet', 'Condominium', 'Cottage',
                 'Dome house', 'Earth house', 'Farm stay', 'Guest suite',
                 'Guesthouse', 'Hostel', 'Hotel', 'House', 'Houseboat', 'Hut', 'Igloo',
                 'Island', 'Lighthouse', 'Loft', 'Nature lodge', 'Other', 'Parking Space', 'Resort',
                 'Ryokan (Japan)', 'Serviced apartment', "Shepherd's hut (U.K., France)",
                 'Tent', 'Tiny house', 'Tipi', 'Townhouse', 'Treehouse', 'Villa', 'Yurt']

room_type = ['Private room', 'Entire home/apt', 'Shared room']

bed_type = ['Real Bed', 'Pull-out Sofa', 'Futon', 'Couch', 'Airbed']

amenities = ['24-hour check-in', 'Accessible-height bed', 'Accessible-height toilet', 'Air conditioning',
             'Air purifier', 'Alfresco bathtub', 'Amazon Echo', 'BBQ grill', 'Baby bath', 'Baby monitor',
             'Babysitter recommendations', 'Balcony', 'Bath towel', 'Bathroom essentials', 'Bathtub',
             'Bathtub with bath chair', 'Beach essentials', 'Beach view', 'Beachfront', 'Bed linens',
             'Bedroom comforts', 'Bidet', 'Body soap', 'Breakfast', 'Breakfast table', 'Building staff',
             'Buzzer/wireless intercom', 'Cable TV', 'Carbon monoxide detector', 'Cat(s)', 'Ceiling fan',
             'Ceiling hoist', 'Central air conditioning', 'Changing table', 'Children’s books and toys',
             'Children’s dinnerware', 'Cleaning before checkout', 'Coffee maker', 'Convection oven', 'Cooking basics',
             'Crib', 'DVD player', 'Day bed', 'Dining table', 'Disabled parking spot', 'Dishes and silverware',
             'Dishwasher', 'Dog(s)', 'Doorman', 'Double oven', 'Dryer', 'EV charger', 'Electric profiling bed',
             'Elevator', 'En suite bathroom', 'Espresso machine', 'Essentials', 'Ethernet connection', 'Exercise equipment',
             'Extra pillows and blankets', 'Family/kid friendly', 'Fax machine', 'Fire extinguisher', 'Fire pit',
             'Fireplace guards', 'Firm mattress', 'First aid kit', 'Fixed grab bars for shower', 'Fixed grab bars for toilet',
             'Flat path to front door', 'Formal dining area', 'Free parking on premises', 'Free street parking',
             'Full kitchen', 'Game console', 'Garden or backyard', 'Gas oven', 'Ground floor access', 'Gym', 'HBO GO',
             'Hair dryer', 'Handheld shower head', 'Hangers', 'Heat lamps', 'Heated floors', 'Heated towel rack',
             'Heating', 'High chair', 'High-resolution computer monitor', 'Host greets you', 'Hot tub', 'Hot water',
             'Hot water kettle', 'Indoor fireplace', 'Internet', 'Iron', 'Ironing Board', 'Jetted tub', 'Keypad', 'Kitchen',
             'Kitchenette', 'Lake access', 'Laptop friendly workspace', 'Lock on bedroom door', 'Lockbox', 'Long term stays allowed',
             'Luggage dropoff allowed', 'Memory foam mattress', 'Microwave', 'Mini fridge', 'Mobile hoist', 'Mountain view',
             'Murphy bed', 'Netflix', 'Other', 'Other pet(s)', 'Outdoor kitchen', 'Outdoor parking', 'Outdoor seating', 'Outlet covers',
             'Oven', 'Pack ’n Play/travel crib', 'Paid parking off premises', 'Paid parking on premises', 'Patio or balcony',
             'Pets allowed', 'Pets live on this property', 'Pillow-top mattress', 'Pocket wifi', 'Pool', 'Pool with pool hoist',
             'Printer', 'Private bathroom', 'Private entrance', 'Private living room', 'Private pool', 'Projector and screen', 'Rain shower',
             'Refrigerator', 'Roll-in shower', 'Room-darkening shades', 'Safety card', 'Self check-in', 'Shampoo', 'Shared gym',
             'Shared pool', 'Shower chair', 'Single level home', 'Ski-in/Ski-out', 'Smart TV', 'Smart lock', 'Smoke detector',
             'Smoking allowed', 'Soaking tub', 'Sound system', 'Stair gates', 'Stand alone steam shower', 'Standing valet', 'Steam oven',
             'Step-free access', 'Stove', 'Suitable for events', 'Sun loungers', 'TV', 'Table corner guards', 'Tennis court', 'Terrace',
             'Toilet paper', 'Touchless faucets', 'Walk-in shower', 'Warming drawer', 'Washer', 'Washer / Dryer', 'Waterfront',
             'Well-lit path to entrance', 'Wheelchair accessible', 'Wide clearance to bed', 'Wide clearance to shower, toilet',
             'Wide doorway', 'Wide entryway', 'Wide hallway clearance', 'Wifi', 'Window guards', 'Wine cooler']

amenities_additional = ['translation missing: en.hosting_amenity_49', 'translation missing: en.hosting_amenity_50']

cancellation_policy = ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period', 'super_strict_30', 'super_strict_60']
cancellation_policy_displayed = ['Flexible', 'Moderate', 'Strict', 'Strict - with grace period', 'Super strict (30)', 'Super strict (60)']

final_model_features = ['special_experience', 'good_bed', 'host_is_superhost', 'host_has_profile_pic',
                        'host_identity_verified', 'require_guest_phone_verification', 'require_guest_profile_picture',
                        'cancellation_policy', 'minimum_nights', 'extra_people', 'security_deposit', 'cleaning_fee',
                        'guests_included', 'beds', 'bedrooms', 'bathrooms', 'accommodates', 'property_type_mean',
                        'room_type_mean', 'neighbourhood_mean', 'host_duration_months', 'distance_from_center_km',
                        'amenity_mean', 'review_score', 'reviews_count', 'avail_ratio', 'text_price', 'neighbourhood_count',
                        'Count_dst_0.5', 'Count_dst_1', 'Count_dst_1.5', 'Count_dst_2']
