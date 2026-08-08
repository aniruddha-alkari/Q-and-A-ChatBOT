import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import os

import os
from dotenv import load_dotenv

load_dotenv()

# Langsmith tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ['LANGCHAIN_PROJECT']="QandA Chatbot"

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

if 'store' not in st.session_state:
        st.session_state.store={}

def generate_llm(selected_llm):
    if selected_llm=="openai/gpt-oss-120b":
        groq_api_key=os.getenv("GROQ_API_KEY")
        llm=ChatGroq(model=selected_llm,groq_api_key=groq_api_key)
    elif selected_llm=="gemma3":
        llm=Ollama(model=selected_llm)
    
    return llm

def get_retriever(uploaded_files):
    documents=[]
    for uploaded_file in uploaded_files:
        temppdf=f"./temp.pdf"
        with open(temppdf,"wb") as file:
            file.write(uploaded_file.getvalue())
            file_name=uploaded_file.name

        loader=PyPDFLoader(temppdf)
        docs=loader.load()
        documents.extend(docs)

    # Split and create embeddings for the documents
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=500)
    splits = text_splitter.split_documents(documents)
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
    retriever = vectorstore.as_retriever()

    return retriever

def get_session_history(session_id:str)->BaseChatMessageHistory:
    if session_id not in st.session_state.store:
        st.session_state.store[session_id]=ChatMessageHistory()
    return st.session_state.store[session_id]

# Title of the App
st.title("Q&A ChatBOT")

# Drop down to select various models
st.sidebar.title("Settings")
selected_llm=st.sidebar.selectbox("Select an LLM Model",["openai/gpt-oss-120b","gemma3"])
llm=generate_llm(selected_llm)

# Main interface for user input
session_id = st.text_input("Session ID", value="default_session")
user_input = st.text_input("Your question:")
uploaded_files = st.file_uploader("Choose A PDF file", type="pdf", accept_multiple_files=True)

# Add a submit button
submit_button = st.button("Submit Question")

contextualize_q_system_prompt=(
            "Given a chat history and the latest user question"
            "which might reference context in the chat history, "
            "formulate a standalone question which can be understood "
            "without the chat history. Do NOT answer the question, "
            "just reformulate it if needed and otherwise return it as is."
        )
contextualize_q_prompt = ChatPromptTemplate.from_messages(
                [
                    ("system", contextualize_q_system_prompt),
                    MessagesPlaceholder("chat_history"),
                    ("human", "{input}"),
                ]
            )

if uploaded_files:
    retriever=get_retriever(uploaded_files)
    history_aware_retriever=create_history_aware_retriever(llm,retriever,contextualize_q_prompt)
else:
    history_aware_retriever = None

# Answer question
system_prompt = (
                "You are an assistant for question-answering tasks. "
                "Use the following pieces of retrieved context to answer "
                "the question. If you don't know the answer, say that you "
                "don't know. Use three sentences maximum and keep the "
                "answer concise."
                "\n\n"
                "{context}"
            )
qa_prompt = ChatPromptTemplate.from_messages(
                [
                    ("system", system_prompt),
                    MessagesPlaceholder("chat_history"),
                    ("human", "{input}"),
                ]
            )
        
question_answer_chain=create_stuff_documents_chain(llm,qa_prompt)

if history_aware_retriever is not None:
    # RAG Chain
    rag_chain = create_retrieval_chain(
        history_aware_retriever,
        question_answer_chain
    )

    conversational_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer"
    )

else:
    # Normal Chat Chain (No Retriever)

    normal_chain = (
        ChatPromptTemplate.from_messages([
            ("system", "You are a helpful AI assistant."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])
        | llm
    )

    conversational_chain = RunnableWithMessageHistory(
        normal_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
    )

if submit_button and user_input:
    response = conversational_chain.invoke(
        {"input": user_input},
        config={
            "configurable": {
                "session_id": session_id
            }
        }
    )

    # Get updated chat history
    session_history = get_session_history(session_id)

    # Display Session ID
    st.markdown(f"## Session ID: {session_id}")

    # Display conversation
    for message in session_history.messages:
        if message.type == "human":
            st.markdown(f"**🧑 User:** {message.content}")
        elif message.type == "ai":
            st.markdown(f"**🤖 Assistant:** {message.content}")
elif submit_button and not user_input:
    st.warning("Please enter a question before submitting.")