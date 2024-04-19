######## Import the required pacakges ############
import streamlit as st
import google.generativeai as genai

####### Provide your api key ###################
api_key="AIzaSyBzumjD3ZMsobIL_GeuNscmhIBu-HWM3N4"
genai.configure(api_key=api_key)

########### Read the model #####################
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

######## Choose the heading ###############
st.header("Gemini AI Chat Bot")

######## Create a chat history ###################
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]


############ Provide the input and apply button#######################
input=st.text_input("Input:")
submit=st.button("Click for response")

################ Call the model if both input and submit presents ###############
if submit and input:
    response=chat.send_message(input)
    st.session_state['chat_history'].append(("You",input))

    for value in response:
        st.session_state['chat_history'].append(("Bot",value.text))

st.subheader("Response")
for role,text in st.session_state['chat_history']:
    st.write(f"{role} : {text}")