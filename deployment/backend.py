import pandas as pd
import joblib

def predict(channel,region,fresh,milk,grocery,frozen,detergents_paper,delicatessen):

    if channel == 'Horeca (Hotel, Restaurant, and Cafe)':
        channel_conv = 1
    else:
        channel_conv = 2

    if region == 'Lisbon':
        region_conv = 1
    elif region == 'Oporto':
        region_conv = 2
    else:
        region_conv = 3

    data = {
        'Channel': channel_conv,
        'Region': region_conv,
        'Fresh': fresh,
        'Milk': milk,
        'Grocery': grocery,
        'Frozen': frozen,
        'Detergents_Paper': detergents_paper,
        'Delicatessen': delicatessen,
    }

    features = pd.DataFrame(data, index=[0])

    load_model = joblib.load("model.pkl")
    prediction = load_model.predict(features)

    if prediction == 0:
        prediction = 'Retail Customer Who Would Buy Alot Grocery Product'
    elif prediction == 1:
        prediction = 'Horeca Customer Who Would Buy Alot Fresh Product'
    elif prediction == 2:
        prediction = 'Flexible Customer Who Would Buy Alot Grocery Product on Retail and Buy Alot Fresh Product on Horeca'
    else:
        prediction = 'Flexible Customer Who Would Buy Alot Grocery Product on Retail and Horeca'
    return prediction