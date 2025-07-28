import streamlit as st
import joblib
st.title("Spam - Detector")
def load_model():
    return joblib.load("modespam.pkl")

model=load_model()

    
with st.form("test-form"):
    mail=st.text_area("enter the mail message")
    submit=st.form_submit_button(label="Submit Message")

if submit:
    if mail.strip():
             preds=model.predict([mail])[0]
             if preds==1:

                st.error("spam detected")
             else:
                st.success("not a spam !")

    else:
         st.error("enter a message")


    
