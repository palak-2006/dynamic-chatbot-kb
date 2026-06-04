# Dynamic Chatbot Knowledge Base

## Overview
This project is a Retrieval-Augmented Generation (RAG) chatbot that can answer questions from PowerPoint documents.

The system:
1. Extracts text from PPTX files.
2. Splits text into chunks.
3. Generates embeddings using Sentence Transformers.
4. Stores embeddings in ChromaDB.
5. Retrieves relevant content for user queries.
6. Uses Google Gemini API to generate final answers.

## Technologies Used

- Python
- ChromaDB
- Sentence Transformers
- LangChain Text Splitters
- Google Gemini API
- python-pptx

## Project Structure
