# Langchain-api-with-streamlit
# 🤖 LangChain + Ollama API with Streamlit UI

A simple full-stack LLM application using:

* ⚡ **FastAPI** backend
* 🧠 **LangChain + Ollama (LLaMA 3)** for text generation
* 🎨 **Streamlit** frontend UI

This project demonstrates how to build and serve **LLM-powered APIs** and consume them in a user-friendly interface.

---

## 🚀 Features

* 📝 Generate **essays** from a topic
* 🎵 Generate **poems for kids**
* 🔌 API endpoints using LangServe
* 💻 Interactive Streamlit frontend
* ⚡ Local LLM inference via Ollama (no API key needed)

---

## 🛠️ Tech Stack

* FastAPI
* LangChain
* LangServe
* Ollama (LLaMA 3)
* Streamlit
* Python

---

## 📂 Project Structure

```id="tree99"
.
├── app.py        # FastAPI + LangChain server
├── client.py     # Streamlit frontend
└── README.md
```

---

## ⚙️ How It Works

### 🔹 Backend (`app.py`)

* Creates a FastAPI server 
* Uses **Ollama (LLaMA 3)** as the LLM
* Defines two prompt pipelines:

  * `/essay` → generates essays
  * `/poem` → generates poems
* Exposes endpoints using `LangServe`

---

### 🔹 Frontend (`client.py`)

* Built with Streamlit 
* Takes user input (topic)
* Sends request to:

  ```
  http://localhost:8000/poem/invoke
  ```
* Displays generated output in real-time

---

## ▶️ Getting Started

### 1. Install dependencies

```bash id="install_dep"
pip install fastapi uvicorn langchain langserve streamlit requests
```

---

### 2. Install & Run Ollama

Download from: https://ollama.com

Then run:

```bash id="ollama_run"
ollama run llama3
```

---

### 3. Start Backend Server

```bash id="run_backend"
python app.py
```

Server will run at:

```
http://localhost:8000
```

---

### 4. Run Streamlit App

```bash id="run_frontend"
streamlit run client.py
```

---

## 🧪 Example Usage

* Enter: `rainbows`
* Output: a 100-word poem for a child 🌈

---

## 🔗 API Endpoints

| Endpoint        | Description    |
| --------------- | -------------- |
| `/essay/invoke` | Generate essay |
| `/poem/invoke`  | Generate poem  |

---

## 🧠 Example Prompt Templates

* Essay:

  ```
  Write me an essay about {topic} with 100 words
  ```

* Poem:

  ```
  Write me a poem about {topic} for a 5-year-old with 100 words
  ```

---

## 🔧 Future Improvements

* Add chat interface (memory)
* Support multiple models
* Add authentication
* Deploy to cloud (Render / AWS / Docker)
* Add streaming responses

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve.

---

## 📜 License

MIT License

---

## ⭐ Acknowledgements

* LangChain
* Ollama
* FastAPI
* Streamlit

---

