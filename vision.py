from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image # This line imports the Image class from the Pillow (PIL Fork) library, which is commonly used for image processing tasks like opening and displaying images.

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## functions to load Gemini pro model and get responses
model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image): # This line defines a function named get_gemini_response that takes two arguments:
    if input!="":
        response=model.generate_content([input,image])# If there's input text, this line calls the generate_content method on the model object, passing a list containing both the input and the image as arguments.
    else:
        response=model.generate_content(image)# In the else case (no text input), this line calls the generate_content method with only the image argument.

    # The function returns the text portion of the generated response object.
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")

uploaded_file = st.file_uploader("Choose an image...",type=["jpg","jpeg","png"]) # This line creates a file uploader in the app, allowing users to select an image file. It restricts acceptable file types to JPEG, JPG, and PNG.
image = "" # This line initializes the image variable as an empty string, which will be used to store the uploaded image object.
if uploaded_file is not None: # This line checks if a file has been uploaded using the file uploader.

    image = Image.open(uploaded_file) # If a file is uploaded, this line opens the uploaded image file using the Image.open function from PIL and stores it in the image variable.
    st.image(image, caption="Uploaded Image.", use_column_width=True) # This line displays the uploaded image in the app using the st.image function. It includes a caption and uses the full column width for better visibility.


    submit=st.button("Tell me about the image")

    ## if submit is clicked 
    if submit:

        response=get_gemini_response(input,image)
        st.subheader("The Response is")
        st.write(response)