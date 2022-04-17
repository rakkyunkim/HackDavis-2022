#import libraries:

import pickle
from flask import Flask
from flask import render_template
from flask import request
# import pandas as pd
import numpy as np

print("start")
app = Flask(__name__)

#load in model
loaded_model = pickle.load(open("LogRegr_pickle.obj","rb"))

#names of all data fields on website:
cols = ["BMI", "smoking", "drinking", "stroke", "PhysHealth", "MentHealth"
        "DiffWalk", "Sex", "Age", "Race", "Diabetes", "PhysAct", "GenHealth",
        "Sleep", "Asthma", "KidneyDisease","SkinCancer"]

#loading webapp on website
@app.route('/', methods=["GET", "POST"])
def home():
        if request.method == "POST":
                print("Post received")
                print("====Request form:", request.form["BMI"], "\n====obtained!")
                # Binary keys
                jupyter_vec = np.zeros(41)
                jupyter_vec[1] = 1 if request.form['smoking'] == 'Yes' else 0
                jupyter_vec[2] = 1 if request.form['drinking'] == 'Yes' else 0
                jupyter_vec[3] = 1 if request.form['stroke'] == 'Yes' else 0
                jupyter_vec[6] = 1 if request.form['DiffWalk'] == 'Yes' else 0
                jupyter_vec[7] = 1 if request.form['Sex'] == 'Yes' else 0
                jupyter_vec[8] = 1 if request.form['PhysAct'] == 'Yes' else 0
                jupyter_vec[10] = 1 if request.form['Asthma'] == 'Yes' else 0
                jupyter_vec[11] = 1 if request.form['KidneyDisease'] == 'Yes' else 0
                jupyter_vec[12] = 1 if request.form['SkinCancer'] == 'Yes' else 0
                jupyter_vec[13] = 1 if request.form["Age"] == "18-24" else 0
                jupyter_vec[14] = 1 if request.form["Age"] == "25-29" else 0
                jupyter_vec[15] = 1 if request.form["Age"] == "30-34" else 0
                jupyter_vec[16] = 1 if request.form["Age"] == "35-39" else 0
                jupyter_vec[17] = 1 if request.form["Age"] == "40-44" else 0
                jupyter_vec[18] = 1 if request.form["Age"] == "45-49" else 0
                jupyter_vec[19] = 1 if request.form["Age"] == "50-54" else 0
                jupyter_vec[20] = 1 if request.form["Age"] == "55-59" else 0
                jupyter_vec[21] = 1 if request.form["Age"] == "60-64" else 0
                jupyter_vec[22] = 1 if request.form["Age"] == "65-69" else 0
                jupyter_vec[23] = 1 if request.form["Age"] == "70-74" else 0
                jupyter_vec[24] = 1 if request.form["Age"] == "75-79" else 0
                jupyter_vec[25] = 1 if request.form["Age"] == "80 or older" else 0
                jupyter_vec[26] = 1 if request.form["Race"] == "American Indian/Alaskan Native" else 0
                jupyter_vec[27] = 1 if request.form["Race"] == "Asian" else 0
                jupyter_vec[28] = 1 if request.form["Race"] == "Black" else 0
                jupyter_vec[29] = 1 if request.form["Race"] == "Hispanic" else 0
                jupyter_vec[30] = 1 if request.form["Race"] == "Other" else 0
                jupyter_vec[31] = 1 if request.form["Race"] == "White" else 0
                jupyter_vec[32] = 1 if request.form["GenHealth"] == "Excellent" else 0
                jupyter_vec[33] = 1 if request.form["GenHealth"] == "Fair" else 0
                jupyter_vec[34] = 1 if request.form["GenHealth"] == "Good" else 0
                jupyter_vec[35] = 1 if request.form["GenHealth"] == "Poor" else 0
                jupyter_vec[36] = 1 if request.form["GenHealth"] == "Very good" else 0
                jupyter_vec[37] = 1 if request.form["Diabetes"] == "No" else 0
                jupyter_vec[38] = 1 if request.form["Diabetes"] == "No, borderline diabetes" else 0
                jupyter_vec[39] = 1 if request.form["Diabetes"] == "Yes" else 0
                jupyter_vec[40] = 1 if request.form["Diabetes"] == "Yes (during pregnancy)" else 0
                #continuous
                jupyter_vec[0] = float(request.form['BMI'])
                jupyter_vec[4] = float(request.form['PhysHealth'])
                jupyter_vec[5] = float(request.form['MentHealth'])
                jupyter_vec[9] = float(request.form['Sleep'])
                jupyter_vec[0] = 2*(jupyter_vec[0] - 12.02)/94.85 - 1
                jupyter_vec[4] = 2*(jupyter_vec[4] - 0)/30 - 1
                jupyter_vec[5] = 2*(jupyter_vec[5] - 0)/30 - 1
                jupyter_vec[9] = 2*(jupyter_vec[9] - 1)/24 - 1
                filehandler = open("LogRegr_pickle.obj", "rb")
                model_ = pickle.load(filehandler)
                conclusion = model_.predict(jupyter_vec.reshape(1,-1))
                probabilities = model_.predict_proba(jupyter_vec.reshape(1,-1))
                print(conclusion, probabilities)
                return render_template("hackdavis_website.html", 
                                       OUTPUT_RESULT = ("At Risk" if conclusion==1 else "Not at risk"), # +"... "+
                                       OUTPUT_TXT = "You are "+ str(probabilities[0][1]*100)[:5] +"% similar to patients with a history of heart disease."
                                       )
        return render_template("hackdavis_website.html")


#PREDICT FUNCTION NOT USED IN THE WEBSITE!!!
#make predictions with trained model:
@app.route('/predict', methods = ["GET","POST"])
def predict():
        print(request.form.values())
        features = [f for f in request.form.values()]
        
        return render_template("hackdavis_website", pred = "Your chance of developing heart disease is {}".format(features[0]))

print("end")
      
        








    
    

