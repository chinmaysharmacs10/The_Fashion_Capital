import flask
from flask import Flask,jsonify,request
import json
import pickle
import pandas as pd

def load_models():
    file_name = 'models/KMeans_pickle.p'
    with open(file_name,'rb') as pickled:
        d = pickle.load(pickled)
        model = d['model']
    return model

def preprocess(data):
    data.rename(columns={'Tshirt_no_of_ratings': 'Number_of_ratings', 'Tshirt_cstmr_rating_name': 'Customer_rating',
                         'Tshirt_cstmr_rating_cstmr_review': 'Customer_Review',
                         'Tshirt_cstmr_rating_date': 'Review_date'}, inplace=True)
    data['Review_date'] = data['Review_date'].str[21:]
    data['Review_date'] = pd.to_datetime(data['Review_date'])
    data['Review_date'] = data['Review_date'].dt.strftime('%Y%m%d')

    data['Tshirt_name'] = data.Tshirt_name.astype(str)
    data['Review_date'] = data.Review_date.astype(str)
    data['Customer_rating'] = data.Customer_rating.astype(str)

    data['Customer_rating'] = data['Customer_rating'].str[:3]
    data['Customer_rating'] = pd.to_numeric(data['Customer_rating'])
    data.Review_date = pd.to_numeric(data.Review_date, errors='coerce')
    data['Number_of_ratings'] = data['Number_of_ratings'].str.replace(',', '').astype(int)
    data = data.dropna()

    #plt.scatter(data['Customer_rating'], data['Review_date'])
    #plt.xlabel('Customer_rating')
    #plt.ylabel('Review_date')
    #plt.show()

    X = pd.DataFrame()
    X['rating'] = data['Customer_rating']
    X['date'] = data['Review_date']
    X1 = X.to_numpy()

    return X1


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/clustering')
def predict():
    df = pd.read_csv('amazon_tshirts_new.csv')
    input_data = preprocess(df)
    model = load_models()
    clusterer = model.fit(input_data)
    centers = clusterer.cluster_centers_
    labels = clusterer.predict(input_data)
    return jsonify(labels)

if __name__ == '__main__':
    application.run(debug=True)