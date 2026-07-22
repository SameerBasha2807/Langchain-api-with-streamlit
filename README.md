# LangChain API with Streamlit

A simple full-stack LLM application built using **FastAPI**, **LangChain**, **Ollama**, and **Streamlit**. The application exposes LangChain pipelines as REST APIs and provides a Streamlit interface for interacting with a locally hosted LLM.

## Features

* Generate essays from a given topic
* Generate poems for children
* FastAPI backend with LangServe
* Interactive Streamlit frontend
* Local LLM inference using Ollama

## Tech Stack

* Python
* FastAPI
* LangChain
* LangServe
* Ollama (Llama 3)
* Streamlit

## Project Structure

```text
.
├── app.py
├── client.py
└── README.md
```

## Installation

### Clone the Repository
### Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```
### Install Dependencies

```bash
pip install fastapi uvicorn langchain langserve streamlit requests
```

## Install Ollama

Download Ollama from:

https://ollama.com

Pull the required model:

```bash
ollama pull llama3
```

## Run the Backend

```bash
python app.py
```

The API will be available at:

```
http://localhost:8000
```

## Run the Streamlit Application

```bash
streamlit run client.py
```

