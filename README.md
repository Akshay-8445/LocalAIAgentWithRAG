# Local_AI_Agent_with_RAG🤖
---
A private, locally running question-answering assistant built with Python, LangChain, ChromaDB, and Ollama. It converts the content of data.txt into embeddings, retrieves the most relevant passages, and generates answers grounded in the supplied document.
---
## Overview

This project demonstrates a simple Retrieval-Augmented Generation (RAG) workflow. Instead of relying only on the language model's general knowledge, the application retrieves relevant information from a local text file and supplies it as context to the model.

The assistant is instructed to answer only from the retrieved context. If the document does not contain the requested information, it returns a clear fallback response.

---
## Features

Runs locally using Ollama
Answers questions from a custom data.txt file
Stores document embeddings in ChromaDB
Automatically selects a new vector collection when the source text changes
Prevents stale information from an older dataset from appearing in responses
Uses context-grounded prompting to reduce hallucinations
Provides a simple command-line interface

---
## Technologies Used⚙️

Python - Core programming language
LangChain - RAG workflow and prompt construction
Ollama - Runs the LLM and embedding model locally
Llama 3.2 - Generates answers
mxbai - embed-large - Creates text embeddings
ChromaDB - Stores and retrieves vector embeddings

---

 ## Project Structure
 ```
LocalAIAgentwithRAG/
│
├── main.py
├── vector.py
├── data.txt
├── requirements.txt
├── README.md
└── .gitignore

```
---
## Project Screenshots

![Application Output]<img width="1920" height="1200" alt="Screenshot 2026-09-04 111353" src="https://github.com/user-attachments/assets/8f2891f8-47be-4507-80b0-ca228ee12699" />


![Application Dataset]<img width="1920" height="1200" alt="Screenshot 2026-09-04 140806" src="https://github.com/user-attachments/assets/9db39481-2a4e-478a-aad7-d2ae69f0d99e" />

---
## Future Improvements🛠️

Add a Streamlit web interface
Support PDF and DOCX documents
Allow users to upload files
Display retrieved sources with answers
Add conversation history
Support multiple documents
Add similarity-score filtering
Improve the user interface

---
## Learning Outcomes

This project demonstrates:

Retrieval-Augmented Generation
Large Language Models
Text embeddings
Vector databases
Semantic search
Prompt engineering
Local AI model execution
Python-based AI application development


## Author🧑‍💻
Akshay Pal
## Linkedin:https://www.linkedin.com/in/akshay-pal-60115b286/
