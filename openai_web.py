import streamlit as st
from langchain.llms import OpenAI
import tiktoken

st.title("Ted's Simple OpenAI App")

openai_api_key = st.sidebar.text_input('OpenAI API Key')

# Token Counting Function
# This function takes a string as input and counts the number of tokens using the tiktoken library.
# The encoding for the OpenAI language model (gpt-3.5-turbo) is specified, and token counting is performed
def count_tokens(string: str) -> int:
    encoding_name = "p50k_base"
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

# Response Generation Function
# Uses the OpenAI language model (OpenAI) to generate a response based on the input text.
# The temperature parameter controls the randomness of the output.
# The function also displays the number of tokens in the input.
def generate_response(input_text):
    try:
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        response = llm(input_text)
        num_tokens = count_tokens(input_text)
        st.info(f"Input contains {num_tokens} tokens.")
        st.info(response)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Streamlit Form
# A form is created to take user input.
# If the OpenAI API key is not provided or invalid, a warning is displayed.
# Upon form submission with a valid API key, the generate_response function is called to generate and display the response.
with st.form('my_form'):
    text = st.text_area('Enter text:', 'How to get started with DSA')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)