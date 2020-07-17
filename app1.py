

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("filename1.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(variance,skewness,curtosis,entropy, entropy1):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[variance,skewness,curtosis,entropy, entropy1]])
    print(prediction)
    return prediction



def main():
    st.title("Drip Irrigation System ")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Drip Irrigation System ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("CropType","Type Here")
    skewness = st.text_input("CropDays","Type Here")
    curtosis = st.text_input("SoilMoisture","Type Here")
    entropy = st.text_input("temp","Type Here")
    entropy1 = st.text_input("Humidity","Type Here")
    result=""
    if st.button("Predict"):
      
        result=predict_note_authentication(variance,skewness,curtosis,entropy, entropy1)
    if(result==1):
       
       st.success('Irrigation is required {}'.format(result))
    else:
      
      st.success('Irrigation is not required {}'.format(result))
   
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    