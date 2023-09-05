import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
import tensorflow as tf

  

def sample():
    return "working"
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(indgred1, indgred2, indgred3, indgred4, indgred5, indgred6, indgred7, indgred8, indgred9, indgred10, indgred11, indgred12, indgred13):  
    indgred=[[indgred1, indgred2, indgred3, indgred4, indgred5, indgred6, indgred7, indgred8, indgred9, indgred10, indgred11, indgred12, indgred13]]
    model = tf.keras.models.load_model("D:\Mithies\M_model.h5")
    result = model.predict(indgred)
    if result > 0.5:
        a = 'machine will failure'
    else:
        a = 'machine will not failure'
    return a
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Machine Failure Classification")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:blue;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Machine Failure Classification App </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    indgred1= st.number_input("ProductID")
    indgred2= st.number_input("Type")
    indgred3= st.number_input("Air Temperature")
    indgred4= st.number_input("Process Temperature")
    indgred5= st.number_input("Rotational Speed")
    indgred6= st.number_input("Torque")
    indgred7= st.number_input("Tool Wear")
    indgred8= st.number_input("TWF")
    indgred9= st.number_input("HDF")
    indgred10= st.number_input("PWF")
    indgred11= st.number_input("OSF")
    indgred12= st.number_input("RNF")
    indgred13= st.number_input("POF")
    result=""
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
   # sample()
    if st.button("Predict"):
        result = prediction(indgred1, indgred2, indgred3, indgred4, indgred5, indgred6, indgred7, indgred8, indgred9, indgred10, indgred11, indgred12, indgred13)
    st.success('The Classification is {}'.format(result))
     
if __name__=='__main__':
    main()