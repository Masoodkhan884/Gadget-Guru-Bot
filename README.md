

# 📦 Gadget Guru Bot 🤖

An intelligent AI-powered chatbot built using **LLM + RAG (Retrieval-Augmented Generation)** to answer queries about gadgets, products, and technical topics with high accuracy.

---

## 🚀 Features

* 💬 Conversational AI chatbot
* 🔍 Retrieval-Augmented Generation (RAG)
* ⚡ Powered by **Groq LLMs**
* 🧠 Context-aware responses
* 📄 Document-based knowledge retrieval (FAISS / embeddings)
* 🌐 Streamlit-based interactive UI
* 🔧 Modular backend architecture

---

## 🏗️ Project Structure

```
gadget-guru-bot/
│
├── app.py                  # Streamlit frontend
├── src/
│   ├── llm.py              # LLM integration (Groq API)
│   ├── rag.py              # Retrieval logic
│   ├── embeddings.py       # Embedding generation
│   └── utils.py            # Helper functions
│
├── data/                   # Knowledge base / documents
├── faiss_index/            # Vector database
├── .env                    # API keys (ignored)
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/gadget-guru-bot.git
cd gadget-guru-bot
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv botenv
source botenv/bin/activate     # Linux/Mac
botenv\Scripts\activate        # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_api_key_here
```

Get your API key from 👉 [https://console.groq.com/](https://console.groq.com/)

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧠 LLM Configuration

Make sure you're using a **supported model**:

```python
model = "llama-3.3-70b-versatile"
```

⚠️ Older models like `llama3-70b-8192` are deprecated.

---

## 🔍 How It Works

1. User enters a query
2. Relevant context is retrieved from vector database (FAISS)
3. Context + query is passed to LLM
4. AI generates an accurate response

---

## 📌 Example Use Cases

* 📱 Gadget recommendations
* 💻 Laptop comparisons
* ☕ Product queries (e.g., coffee makers)
* 🧾 Technical Q&A
* 🛍️ E-commerce assistants

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit 🎨
* FAISS 🔎
* LangChain / Custom RAG ⚙️
* Groq API 🚀

---

## ⚡ Future Improvements

* ✅ Add multi-turn memory
* ✅ Integrate LangGraph for workflows
* ✅ Add voice input/output
* ✅ Deploy on cloud (Streamlit / Docker)
* ✅ Add product recommendation engine

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Commit changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Masood Khan**
Software Engineer | AI Enthusiast

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---


