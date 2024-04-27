from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import LLMChain
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

video_url = 'https://www.youtube.com/watch?v=p--YZ1QKVj4&ab_channel=BloombergLive'
def create_vectordb_from_youtube(video_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url)
    transript = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transript)
    db = FAISS.from_documents(docs, embeddings)
    return db

# print(create_vectordb_from_youtube(video_url))

def get_response_from_query(db, query, k):
    # text-davinci can handle 4096 tokens and out chunk sise is 1000 , thus we can have 4 chunks

    docs = db.similarity_search(query, k)
    docs_page_content = " ".join([d.page_content for d in docs])

    llm = OpenAI(model='gpt-3.5-turbo-instruct',temperature=0.7)

    prompt = PromptTemplate(
        input_variables = ['question', 'docs'],
        template = """Here are some relevant information from the video: {docs}. Now, can you answer the following question: {question}"""
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(question=query,docs= docs_page_content)
    response = response.replace("\n", "")
    return response


# def youtube_assistant(video_url):
#     llm = OpenAI(temperature=0.7)
#     prompt_template_name = PromptTemplate(
#         input_variables = ['video_url'],
#         template = f'Can you summarize the video at {video_url} for me?'
#     )

#     name_chain  = LLMChain(llm = llm, prompt  = prompt_template_name, output_key='video_summary')
#     responce = name_chain({'video_url': video_url})
#     return responce
