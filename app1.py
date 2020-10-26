
import pickle
import streamlit as st 
from PIL import Image
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
pickle_in = open("filename1.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome All"

def predict_note_authentication(variance,skewness,curtosis,entropy, entropy1):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy, entropy1]])
    print(prediction)
    return prediction



def main():
    st.title("Drip Irrigation System ")
    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;">Drip Irrigation System ML App</h2>
    <h3 style="color:white;text-align:center;">اپنی فصلوں کیلئے آبپاشی کی ضرورت تلاش کریں </h3>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    display = ("Wheat/گندم", "Ground Nuts/مونگ پھلی","Garden flowers/باغ کے پھول","Maize/مکئی","Paddy/چاول","Potato/آلو","pulse/دالوں کی فصل","SugerCane/گنا","coffee/کافی")

    options = list(range(len(display)))

    variance = st.selectbox("Crop Type", options, format_func=lambda x: display[x])
   # variance = st.text_input("CropType","")
    skewness = st.text_input("Crop Days/فصلوں کے دن","")
    curtosis = st.text_input("Soil Moisture/مٹی کی نمی","")
    entropy = st.text_input("temperature/درجہ حرارت ","")
    entropy1 = st.text_input("Humidity/نمی ","")
    
 
    result=""
    if st.button("Predict"):
      
        result=predict_note_authentication(variance,skewness,curtosis,entropy, entropy1)
    if(result==1):
       
       st.success('Irrigation is required-آبپاشی ضروری ہے')
   
    else:
      
      st.success('Irrigation is not required-آبپاشی کی ضرورت نہیں ہے')
   
@app.route('/predict_api',methods=['GET', 'POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''   
    data = request.get_json(force=True)
   
    
   
     final_features = [np.array(data)]
    recommended =classifier.predict(data)
 
    
    return jsonify(recommended=recommended)

    


if __name__=='__main__':
    main()
    
    
    
    
    
    
