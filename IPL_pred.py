import pickle
import streamlit as st
import pandas as pd

matches = pd.read_csv("matches2.csv")
matches['winner'].fillna('Draw', inplace=True)
matches.replace(['Mumbai Indians', 'Kolkata Knight Riders', 'Royal Challengers Bangalore', 'Chennai Super Kings',
                 'Rajasthan Royals', 'Delhi Capitals', 'Gujarat Lions', 'Kings XI Punjab',
                 'Sunrisers Hyderabad', 'Rising Pune Supergiants', 'Kochi Tuskers Kerala']
                , ['MI', 'KKR', 'RCB', 'CSK', 'RR', 'DC', 'GL', 'KXIP', 'SRH', 'RPS', 'KTK'], inplace=True)

matches.head(5)

encode = {'team1': {'MI': 1, 'KKR': 2, 'RCB': 3, 'CSK': 4, 'RR': 5, 'DC': 6, 'GL': 7, 'KXIP': 8, 'SRH': 9, 'RPS': 10,
                    'KTK': 11},
          'team2': {'MI': 1, 'KKR': 2, 'RCB': 3, 'CSK': 4, 'RR': 5, 'DC': 6, 'GL': 7, 'KXIP': 8, 'SRH': 9, 'RPS': 10,
                    'KTK': 11},
          'toss_winner': {'MI': 1, 'KKR': 2, 'RCB': 3, 'CSK': 4, 'RR': 5, 'DC': 6, 'GL': 7, 'KXIP': 8, 'SRH': 9,
                          'RPS': 10, 'KTK': 11},
          'winner': {'MI': 1, 'KKR': 2, 'RCB': 3, 'CSK': 4, 'RR': 5, 'DC': 6, 'GL': 7, 'KXIP': 8, 'SRH': 9, 'RPS': 10,
                     'KTK': 11, 'Draw': 12}}
matches.replace(encode, inplace=True)
matches.head(5)

dicVal = encode['winner']

df_matches = matches[['team1', 'team2', 'city', 'toss_decision', 'toss_winner', 'venue', 'winner']]
df_matches.head(5)

df = pd.DataFrame(df_matches)

df["city"].unique()
df["venue"].unique()
df["toss_decision"].unique()

cat_list = df["city"]
encoded_data, mapping_index = pd.Series(cat_list).factorize()
cat_list1 = df["venue"]
encoded_data1, mapping_index1 = pd.Series(cat_list1).factorize()
cat_list2 = df["toss_decision"]
encoded_data2, mapping_index2 = pd.Series(cat_list2).factorize()

from sklearn.preprocessing import LabelEncoder

var_mod = ['city', 'toss_decision', 'venue']
le = LabelEncoder()
for i in var_mod:
    df[i] = le.fit_transform(df[i])

from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics


def classification_model(model, data, predictors, outcome):
    model.fit(data[predictors], data[outcome])
    predictions = model.predict(data[predictors])
    print(predictions)
    accuracy = metrics.accuracy_score(predictions, data[outcome])
    print('Accuracy : %s' % '{0:.3%}'.format(accuracy))


model = RandomForestClassifier(n_estimators=100)
outcome_var = ['winner']
predictor_var = ['team1', 'team2', 'city', 'toss_decision', 'toss_winner', 'venue']
classification_model(model, df, predictor_var, outcome_var)

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

#coding for web app:

def prediction(team1, team2, city, toss_decision, toss_winner, venue):
    if team1 == "MI":
        team1 = 1
    elif team1 == "KKR":
        team1 = 2
    elif team1 == "RCB":
        team1 = 3
    elif team1 == "CSK":
        team1 = 4
    elif team1 == "RR":
        team1 = 5
    elif team1 == "DC":
        team1 = 6
    elif team1 == "GL":
        team1 = 7
    elif team1 == "KXIP":
        team1 = 8
    elif team1 == "SRH":
        team1 = 9
    elif team1 == "RPS":
        team1 = 10
    else:
        team1 = 11

    if team2 == "MI":
        team2 = 1
    elif team2 == "KKR":
        team2 = 2
    elif team2 == "RCB":
        team2 = 3
    elif team2 == "CSK":
        team2 = 4
    elif team2 == "RR":
        team2 = 5
    elif team2 == "DC":
        team2 = 6
    elif team2 == "GL":
        team2 = 7
    elif team2 == "KXIP":
        team2 = 8
    elif team2 == "SRH":
        team2 = 9
    elif team2 == "RPS":
        team2 = 10
    else:
        team2 = 11

    if city == "Hyderabad":
        city = 0
    elif city == "Pune":
        city = 1
    elif city == "Rajkot":
        city = 2
    elif city == "Indore":
        city = 3
    elif city == "Bengaluru":
        city = 4
    elif city == "Mumbai":
        city = 5
    elif city == "Kolkata":
        city = 6
    elif city == "Delhi":
        city = 7
    elif city == "Chandigarh":
        city = 8
    elif city == "Kanpur":
        city = 9
    elif city == "Jaipur":
        city = 10
    elif city == "Chennai":
        city = 11
    elif city == "Cape Town":
        city = 12
    elif city == "Port Elizabeth":
        city = 13
    elif city == "Durban":
        city = 14
    elif city == "Centurion":
        city = 15
    elif city == "East London":
        city = 16
    elif city == "Johannesburg":
        city = 17
    elif city == "Kimberley":
        city = 18
    elif city == "Bloemfontein":
        city = 19
    elif city == "Ahmedabad":
        city = 20
    elif city == "Cuttack":
        city = 21
    elif city == "Nagpur":
        city = 22
    elif city == "Dharamsala":
        city = 23
    elif city == "Kochi":
        city = 24
    elif city == "Visakhapatnam":
        city = 25
    elif city == "Raipur":
        city = 26
    elif city == "Ranchi":
        city = 27
    elif city == "Abu Dhabi":
        city = 28
    elif city == "Sharjah":
        city = 29
    elif city == "Dubai":
        city = 30
    elif city == "Mohali":
        city = 31
    else:
        city = 32

    if toss_decision == "field":
        toss_decision = 0
    else:
        toss_decision = 1

    if toss_winner == "MI":
        toss_winner = 1
    elif toss_winner == "KKR":
        toss_winner = 2
    elif toss_winner == "RCB":
        toss_winner = 3
    elif toss_winner == "CSK":
        toss_winner = 4
    elif toss_winner == "RR":
        toss_winner = 5
    elif toss_winner == "DC":
        toss_winner = 6
    elif toss_winner == "GL":
        toss_winner = 7
    elif toss_winner == "KXIP":
        toss_winner = 8
    elif toss_winner == "SRH":
        toss_winner = 9
    elif toss_winner == "RPS":
        toss_winner = 10
    else:
        toss_winner = 11

    if venue == "Rajiv Gandhi International Stadium, Uppal":
        venue = 0
    elif venue == "Maharashtra Cricket Association Stadium":
        venue = 1
    elif venue == "Saurashtra Cricket Association Stadium":
        venue = 2
    elif venue == "Holkar Cricket Stadium":
        venue = 3
    elif venue == "M. Chinnaswamy Stadium":
        venue = 4
    elif venue == "Wankhede Stadium":
        venue = 5
    elif venue == "Eden Gardens":
        venue = 6
    elif venue == "Feroz Shah Kotla Ground":
        venue = 7
    elif venue == "Punjab Cricket Association IS Bindra Stadium, Mohali":
        venue = 8
    elif venue == "Green Park":
        venue = 9
    elif venue == "Sawai Mansingh Stadium":
        venue = 10
    elif venue == "MA Chidambaram Stadium, Chepauk":
        venue = 11
    elif venue == "Dr DY Patil Sports Academy":
        venue = 12
    elif venue == "Newlands":
        venue = 13
    elif venue == "St George's Park":
        venue = 14
    elif venue == "Kingsmead":
        venue = 15
    elif venue == "SuperSport Park":
        venue = 16
    elif venue == "Buffalo Park":
        venue = 17
    elif venue == "New Wanderers Stadium":
        venue = 18
    elif venue == "De Beers Diamond Oval":
        venue = 19
    elif venue == "OUTsurance Oval":
        venue = 20
    elif venue == "Brabourne Stadium":
        venue = 21
    elif venue == "Sardar Patel Stadium, Motera":
        venue = 22
    elif venue == "Barabati Stadium":
        venue = 23
    elif venue == "Vidarbha Cricket Association Stadium, Jamtha":
        venue = 24
    elif venue == "Himachal Pradesh Cricket Association Stadium":
        venue = 25
    elif venue == "Nehru Stadium":
        venue = 26
    elif venue == "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium":
        venue = 27
    elif venue == "Subrata Roy Sahara Stadium":
        venue = 28
    elif venue == "Shaheed Veer Narayan Singh International Stadium":
        venue = 29
    elif venue == "JSCA International Stadium Complex":
        venue = 30
    elif venue == "Sheikh Zayed Stadium":
        venue = 31
    elif venue == "Sharjah Cricket Stadium":
        venue = 32
    elif venue == "Dubai International Cricket Stadium":
        venue = 33
    elif venue == "Narendra modi stadium":
        venue = 34
    else:
        venue = 35

    prediction = classifier.predict([[team1, team2, city, toss_decision, toss_winner, venue]])
    print(prediction)
    return prediction


def main():
    st.title("Indian Premier League Cricket Match Prediction")
    st.subheader("Built with Steamlit by Arvindh")

    team1 = st.selectbox("Team 1", ("MI", "KKR", "RCB", "CSK", "RR", "DC", "GL", "KXIP", "SRH", "RPS", "KTK"))
    team2 = st.selectbox("Team 2", ("MI", "KKR", "RCB", "CSK", "RR", "DC", "GL", "KXIP", "SRH", "RPS", "KTK"))
    city = st.selectbox("City", (
    "Hyderabad", "Pune", "Rajkot", "Indore", "Bengaluru", "Mumbai", "Kolkata", "Delhi", "Chandigarh", "Kanpur",
    "Jaipur", "Chennai", "Cape Town", "Port Elizabeth", "Durban", "Centurion", "East London", "Johannesburg",
    "Kimberley", "Bloemfontein", "Ahmedabad", "Cuttack", "Nagpur", "Dharamsala", "Kochi", "Visakhapatnam", "Raipur",
    "Ranchi", "Abu Dhabi", "Sharjah", "Dubai", "Mohali", "Ahmedabad"))
    toss_decision = st.selectbox("Toss decision", ("field", "bat"))
    toss_winner = st.selectbox("Toss winner",
                               ("MI", "KKR", "RCB", "CSK", "RR", "DC", "GL", "KXIP", "SRH", "RPS", "KTK"))
    venue = st.selectbox("Venue", ("Rajiv Gandhi International Stadium, Uppal",
                                   "Maharashtra Cricket Association Stadium",
                                   "Saurashtra Cricket Association Stadium", "Holkar Cricket Stadium",
                                   "M. Chinnaswamy Stadium", "Wankhede Stadium", "Eden Gardens",
                                   "Feroz Shah Kotla Ground",
                                   "Punjab Cricket Association IS Bindra Stadium, Mohali",
                                   "Green Park", "Sawai Mansingh Stadium",
                                   "MA Chidambaram Stadium, Chepauk", "Dr DY Patil Sports Academy",
                                   "Newlands", "St George's Park", "Kingsmead", "SuperSport Park",
                                   "Buffalo Park", "New Wanderers Stadium", "De Beers Diamond Oval",
                                   "OUTsurance Oval", "Brabourne Stadium",
                                   "Sardar Patel Stadium, Motera", "Barabati Stadium",
                                   "Vidarbha Cricket Association Stadium, Jamtha",
                                   "Himachal Pradesh Cricket Association Stadium", "Nehru Stadium",
                                   "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
                                   "Subrata Roy Sahara Stadium",
                                   "Shaheed Veer Narayan Singh International Stadium",
                                   "JSCA International Stadium Complex", "Sheikh Zayed Stadium",
                                   "Sharjah Cricket Stadium", "Dubai International Cricket Stadium", "Narendra modi stadium"))
    result = ""

    if st.button("Predict"):
        result = prediction(team1, team2, city, toss_decision, toss_winner, venue)
        if result == 1:
            st.success('The Predicted winner is MI')
        elif result == 2:
            st.success('The Predicted winner is KKR')
        elif result == 3:
            st.success('The Predicted winner is RCB')
        elif result == 4:
            st.success('The Predicted winner is CSK')
        elif result == 5:
            st.success('The Predicted winner is RR')
        elif result == 6:
            st.success('The Predicted winner is DC')
        elif result == 7:
            st.success('The Predicted winner is GL')
        elif result == 8:
            st.success('The Predicted winner is KXIP')
        elif result == 9:
            st.success('The Predicted winner is SRH')
        elif result == 10:
            st.success('The Predicted winner is RPS')
        else:
            st.success('The Predicted winner is KTK')




if __name__ == '__main__':
    main()
