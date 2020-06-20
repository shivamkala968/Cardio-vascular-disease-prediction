

"""
Created on Sat Jun 13 02:20:31 2020

@author: shivam kala
"""
"""
Created on  JUNE 21 ,2020

@author: Shivam kala
"""
import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("cardio-prediction-rfc-model2.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(age,gender1,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke1,alco1,active1):
    
    gender=5
    smoke=5
    alco=5
    active=5
    bmi=float(float(weight)/(float(height)/100)**2)
    age=((float(age)*365)-19464)/2468.4
  
    height=(float(height)-164.36)/8.2
    weight=(float(weight)-74.119)/14.315
    ap_hi=(float(ap_hi)-126.287)/17.9
    ap_lo=(float(ap_lo)-81.33)/9.88
    cholesterol=float(cholesterol)
    gluc=float(gluc)
   
    
    

    if gender1=="Male" or gender1=="MALE" or gender1=="male" or gender1=="m" or gender1=="M"  :
        gender=2
    elif gender1=="Female" or gender1=="FEMALE" or gender1=="female" or gender1=="f" or gender1=="F":
        gender=1

    if smoke1=="Yes" or smoke1=="Y"  or smoke1=="y" or smoke1=="1" or smoke1=="YES" or smoke1=="yes":
        smoke=1
    elif smoke1=="No" or smoke1=="N"  or smoke1=="n" or smoke1=="0" or smoke1=="NO":
        smoke=0
    if alco1=="Yes" or  alco1== "Y" or alco1== "y" or alco1== "1" or alco1== "YES" or alco1=="yes" :
        alco=1
    elif alco1=="No" or alco1== "N" or alco1== "n" or alco1== "0" or alco1== "NO" or alco1=="no":
        alco= 0
    if active1=="Yes" or active1== "Y" or active1== "y" or active1== "1" or active1== "YES" or active1=="yes"  :
        active= 1
    elif active1=="No" or active1== "N" or active1== "n" or active1== "0" or active1== "NO" or active1=="no":
        active=0
    bmi=(bmi-27.52)/6.081


    prediction=classifier.predict([[age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active,bmi]])
    print(prediction)
    return prediction



def main():
    st.title("Cardio Vascular Disease prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Cardio Vascular Disease prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age= (st.text_input("Age(in years)","Type Here")).strip()
    gender1 = st.text_input("Gender(Male or Female)","Type Here")
    height = st.text_input("Height (in cms)","Type Here").strip()
    weight = st.text_input("Weight (in kgs )","Type Here").strip()
    ap_hi = st.text_input("Systolic blood pressure","Type Here").strip()
    ap_lo = st.text_input("Diastolic blood pressure ","Type Here").strip()

    cholesterol = st.text_input("Cholesterol (1: normal, 2: above normal, 3: well above normal )","Type Here").strip()
    gluc = st.text_input("Glucose (1: normal, 2: above normal, 3: well above normal )","Type Here").strip()
    smoke1 = st.text_input("Smoker (Yes/No)","Type Here")
    smoke1=str(smoke1)
    alco1 = st.text_input("Alcohol Consumer (Yes/No)","Type Here")
    alco1=str(alco1)
    active1 = st.text_input("Active (Yes/No)","Type Here")
    active1=str(active1)
   

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(age,gender1,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke1,alco1,active1)
        if result==0:
            st.success('Low chances of Cardio Vascular Disease')
        elif result==1:
            st.success('High chances of Cardio Vascular Disease')

    if st.button("About"):
        st.text("MADE BY")
        st.text("Shivam kala")

if __name__=='__main__':
    main()
    
    
    