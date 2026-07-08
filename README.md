<div align="center">

# 🤖 Q&A ChatBOT

### An Intelligent RAG-Based Question Answering Application using LangChain, HuggingFace Embeddings & Multiple LLMs

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?logo=streamlit)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-yellow)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Database-orange)
![RAG](https://img.shields.io/badge/RAG-Retrieval%20Augmented%20Generation-purple)

</p>

A modern AI-powered Question & Answer chatbot that supports both **general conversations with Large Language Models** and **Retrieval-Augmented Generation (RAG)** for answering questions from uploaded PDF documents.

</div>

---

# 📖 Overview

Q&A ChatBOT is an interactive AI assistant built with **LangChain**, **Streamlit**, **HuggingFace Embeddings**, and **ChromaDB**.

The application supports two different use cases:

### 💬 1. General AI Chat

Users can directly ask questions to an LLM just like ChatGPT.

### 📄 2. PDF Question Answering (RAG)

Users can upload PDF documents and ask questions based only on the uploaded content.

The chatbot retrieves the most relevant document chunks using semantic search and generates accurate context-aware responses using Retrieval-Augmented Generation (RAG).

---

# ✨ Features

- 🤖 Chat directly with Large Language Models
- 📄 Upload one or multiple PDF documents
- 🔍 Semantic Search using HuggingFace Embeddings
- 🧠 Retrieval-Augmented Generation (RAG)
- 💬 Conversational Memory
- 🔄 History Aware Retriever
- 📚 Context-based Question Answering
- ⚡ Fast document retrieval using ChromaDB Vector Store
- 🎯 Multiple LLM selection from dropdown
- 🖥️ Clean Streamlit UI
- 📎 Upload PDFs directly from chat interface

---

# 🏗️ Project Architecture

```
                User
                  │
                  ▼
          Streamlit Interface
                  │
      ┌───────────┴───────────┐
      │                       │
      ▼                       ▼
General Chat             Upload PDF
      │                       │
      ▼                       ▼
 Selected LLM        PDF Loader
                              │
                              ▼
                     Text Splitter
                              │
                              ▼
                  HuggingFace Embeddings
                              │
                              ▼
                       ChromaDB Vector DB
                              │
                              ▼
                 History Aware Retriever
                              │
                              ▼
                     Retrieval Chain
                              │
                              ▼
                     Selected LLM
                              │
                              ▼
                        Final Answer
```

---

# 🚀 Technologies Used

## Programming Language

- Python

## Frameworks

- LangChain
- Streamlit

## Embedding Model

- HuggingFace Embeddings

## Vector Database

- ChromaDB

## Document Processing

- PyPDF

## AI Models

- User Selectable LLMs
- HuggingFace Embedding Models

---

# 🧠 How RAG Works

The application follows the Retrieval-Augmented Generation pipeline.

### Step 1

Upload one or multiple PDF documents.

↓

### Step 2

Extract text from PDF.

↓

### Step 3

Split the text into smaller chunks.

↓

### Step 4

Generate embeddings using HuggingFace Embeddings.

↓

### Step 5

Store embeddings inside ChromaDB.

↓

### Step 6

Retrieve the most relevant document chunks.

↓

### Step 7

Pass retrieved context to the selected LLM.

↓

### Step 8

Generate an accurate answer grounded in the uploaded document.

---

# 📂 Project Structure

```
Q-and-A-ChatBOT/
│
├── Screenshot/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
└── ...
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/aniruddha-alkari/Q-and-A-ChatBOT.git
```

Go inside the project

```bash
cd Q-and-A-ChatBOT
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your API key.

Example:

```env
GROQ_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

# 💡 Usage

## General Chat

- Select an LLM from the dropdown.
- Ask any question.
- The chatbot responds directly using the selected model.

---

## PDF Chat (RAG)

- Upload one or multiple PDF files.
- Wait for document processing.
- Ask questions related to the uploaded document.
- The chatbot retrieves relevant content before generating the answer.

---

# 🖼️ Application Screenshots

## Home Page

![Home](Screenshot/home.png)

---

## Model Selection

![Model](Screenshot/model_selection.png)

---

## Chat Interface

![Chat](Screenshot/chat.png)

---

## PDF Upload

![Upload](Screenshot/upload_pdf.png)

---

## Question Answering

![Answer](Screenshot/answer.png)

---

# 🎯 Supported Use Cases

- Research Paper Q&A
- Resume Analysis
- Company Policy Documents
- Books
- User Manuals
- Reports
- Educational PDFs
- Knowledge Base Chatbot
- AI Assistant

---

# 🔥 Key Highlights

- Retrieval-Augmented Generation (RAG)
- HuggingFace Embeddings
- ChromaDB Vector Database
- Multiple LLM Support
- Conversational Memory
- History Aware Retrieval
- Semantic Search
- Streamlit UI
- LangChain Framework

---

# 📌 Future Improvements

- OCR support for scanned PDFs
- Chat history persistence
- Authentication
- Citation/Source highlighting
- Support for DOCX, TXT and Excel files
- Hybrid Search (BM25 + Vector Search)
- Cloud deployment
- Multi-user support

---

# 📜 License

This project is intended for educational and learning purposes.

---

# 👨‍💻 Author

**Aniruddha Alkari**

Machine Learning | Generative AI | LLM | LangChain | Python

GitHub:
https://github.com/aniruddha-alkari

---

## ⭐ If you like this project

Please consider giving this repository a **Star ⭐**

It motivates me to build more AI and Machine Learning projects.