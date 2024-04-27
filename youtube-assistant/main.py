import streamlit as st
import langchain_helper as lch
import textwrap

st.title("Youtube Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        video_url = st.sidebar.text_area('Enter the youtube video url', max_chars=100)
        query = st.sidebar.text_area('Enter your query' , max_chars=50, key='query')
        k = st.number_input('Enter the number of documents to search',  min_value=1, max_value=4)
        submitted = st.form_submit_button('Submit')

if query and video_url and submitted:
    db = lch.create_vectordb_from_youtube(video_url)
    response = lch.get_response_from_query(db, query, k)
    response = textwrap.fill(response, width=100)
    st.subheader('Answer:')
    st.text(textwrap.fill(response, width=100))