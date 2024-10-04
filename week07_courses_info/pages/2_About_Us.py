import streamlit as st

st.set_page_config(page_title="About Us")

# Header of the page
st.header("About this App")

# Description of the app (one-line)
st.write("This is a Streamlit app that demonstrates how to use the OpenAI API to generate text completions.")

# Drop-down (expandable) section
with st.expander("How to use this app"):
    # st.write("Here are some of the key features:")
    st.markdown("""
    1. Enter your prompt under the text area.
    2. Click the 'Submit' button.
    3. The app will generate a text completion based on your prompt.
    """)



# st.bar_chart({"data": [1, 5, 2, 6, 2, 11]})

# with st.expander("See explanation"):
#      st.write('''
#          The chart above shows some numbers I picked for you.
#          I rolled actual dice for these, so they're *guaranteed* to
#          be random.
#      ''')
#      st.image("https://static.streamlit.io/examples/dice.jpg")
