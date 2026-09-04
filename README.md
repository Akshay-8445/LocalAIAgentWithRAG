Local AI Agent with RAG

A private, locally running question-answering assistant built with Python, LangChain, ChromaDB, and Ollama. It converts the content of data.txt into embeddings, retrieves the most relevant passages, and generates answers grounded in the supplied document.

Overview

This project demonstrates a simple Retrieval-Augmented Generation (RAG) workflow. Instead of relying only on the language model's general knowledge, the application retrieves relevant information from a local text file and supplies it as context to the model.

The assistant is instructed to answer only from the retrieved context. If the document does not contain the requested information, it returns a clear fallback response.

Features

Runs locally using Ollama

Answers questions from a custom data.txt file

Stores document embeddings in ChromaDB

Automatically selects a new vector collection when the source text changes

Prevents stale information from an older dataset from appearing in responses

Uses context-grounded prompting to reduce hallucinations

Provides a simple command-line interface

Requires no paid API key

Technologies Used

Technology

Purpose

Python

Core programming language

LangChain

RAG workflow and prompt construction

Ollama

Runs the LLM and embedding model locally

Llama 3.2

Generates answers

mxbai-embed-large

Creates text embeddings

ChromaDB

Stores and retrieves vector embeddings

Project Structure

LocalAIAgentWithRAG/
├── main.py             # CLI, prompt and answer-generation logic
├── vector.py           # Document loading, embeddings and retrieval
├── data.txt            # Knowledge source used by the assistant
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
