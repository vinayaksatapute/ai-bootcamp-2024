# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
# from helper_functions import llm
from logics.customer_query_handler import process_user_message

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Streamlit App")

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    # response = llm.get_completion(user_prompt) 
    response, course_details = process_user_message(user_prompt)
    st.write(response)

    st.divider()
    df_course_details = pd.json_normalize(course_details)
    st.dataframe(df_course_details)

    print(f"User Input is:  {user_prompt}")

    # """
    # course_details : [
    #         {
    #         'name': 'Ethical Hacking for Beginners', 
    #         'category': 'Cybersecurity', 
    #         'provider': 'SecureTech', 
    #         'course_code': 'EH-ST401', 
    #         'duration': '6 weeks', 
    #         'rating': 4.8, 
    #         'skills_covered': ['Penetration Testing', 'Network Scanning', 'Vulnerability Assessment'], 
    #         'description': 'Learn the basics of ethical hacking and penetration testing. Understand network scanning and vulnerability assessment to start a career in cybersecurity.', 
    #         'price': 749.99
    #         }
    #     ]
    # """

