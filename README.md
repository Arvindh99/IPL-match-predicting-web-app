# IPL Match Prediction

This project focuses on predicting the winner of IPL cricket matches based on teams, toss winner, toss decision, and venues. The dataset used contains 17 variables and 816 data entries.

### Dataset Information

The dataset consists of the following variables:

    - Id: Unique identifier for each match
    - Season: Year of the IPL season
    - City: City where the match took place
    - Date: Date of the match
    - Team1: First team participating in the match
    - Team2: Second team participating in the match
    - Toss Winner: Team that won the toss
    - Toss Decision: Decision made by the toss winner (batting or fielding)
    - Result: Result of the match (normal, tie, or no result)
    - DL Applied: Whether the Duckworth-Lewis method was applied (1 if applied, 0 otherwise)
    - Winner: Team that won the match
    - Win by Runs: Number of runs by which the winning team won
    - Win by Wickets: Number of wickets remaining when the winning team chased the target
    - Player of the Match: Player awarded as the Man of the Match
    - Venue: Venue where the match took place
    - Umpire1: First umpire of the match
    - Umpire2: Second umpire of the match
    
### Web App

A web application has been developed to predict the winner of cricket matches based on the provided variables. The Random Forest algorithm is used for making the predictions. You can access the web app by visiting the following link: [IPL Match Prediction Web App](https://share.streamlit.io/arvindh99/ipl-match-predicting-web-app/main/IPL_pred.py)

Feel free to explore the web app and try out different inputs to predict the match winners.

### Contribution

If you have any suggestions or improvements for this project, please feel free to share. Contributions are always welcome to enhance the accuracy and performance of the match prediction model.

Let's enjoy the excitement of IPL and make informed predictions with this IPL Match Prediction project!

### Acknowledgments

We would like to acknowledge the Streamlit community for their excellent framework that made it easy to develop this Web Application. Their documentation and examples have been instrumental in the development process.
