# 📚 DocQuery AI

A simple **Retrieval-Augmented Generation (RAG)** application that lets you ask questions about your own PDF documents.

You can use your **class notes, study material, research papers, documentation, reports, etc.**

---

## 🎯 What Are We Building?

We are building a basic **Document Q&A RAG application**.

```text
PDF → Load → Chunk → Embeddings → ChromaDB
                                      ↓
User Query → Similarity Search → Relevant Chunks
                                      ↓
                              Prompt + Context
                                      ↓
                                     LLM
                                      ↓
                                    Answer
```

### Why are we building this?

The goal is **real-world hands-on experience**, not just learning RAG theory.

By building this project, you'll understand:

* Document loading & chunking
* Embeddings and vector databases
* Similarity search & Top-K retrieval
* Prompt + context → LLM
* Basic RAG architecture
* External API integration
* Python virtual environments & dependencies
* Git/GitHub collaboration
* Debugging real-world errors

---

## 💡 Try It With Your Own Documents

Replace the sample PDF with your own document:

```text
data/
└── pdf_data.pdf
```

Then ask questions such as:

```text
What are the main topics in this document?

Explain CAP theorem in simple terms.

Summarize chapter 3.

What are the key points discussed?
```

> ⚠️ Don't upload passwords, API keys, confidential company documents, or other sensitive information.

---

## 🛠️ Technologies

* **Python** — Application development
* **LangChain** — RAG pipeline
* **OpenRouter** — LLM API
* **HuggingFace / BGE-small** — Embeddings
* **ChromaDB** — Vector database
* **PyPDF** — PDF processing
* **python-dotenv** — Environment variables
* **Git & GitHub** — Version control & collaboration

---

# 🚀 Getting Started

## Prerequisites

Install:

* Python **3.10+**
* Git
* GitHub account
* Basic Python knowledge
* OpenRouter API key

Check Python:

### Windows

```bash
python --version
```

### Linux / macOS

```bash
python3 --version
```

---

## 1️⃣ Clone the Repository

```bash
git clone <REPOSITORY_URL>
cd <PROJECT_NAME>
```

---

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure API Key

Create `.env`:

```env
OPENROUTER_API_KEY=your_api_key_here
```

**Never commit `.env` or your API key to GitHub.**

Use `.env.example` to show required environment variables.

---

## 5️⃣ Add Your PDF

Put your document here:

```text
data/
└── pdf_data.pdf
```

---

## 6️⃣ Run

```bash
python main.py
```

Then:

```text
AI: Hi, how can I help you with your document?

Human: What are the main topics discussed?
```

Type `exit` to stop.

---

# 🤝 Contributing

Everyone is encouraged to contribute!

### You can contribute by:

* 🐛 Fixing bugs
* 📚 Improving documentation
* ✨ Adding features
* 🧠 Improving the RAG pipeline
* 💡 Suggesting ideas
* 🧪 Experimenting with chunking, embeddings, Top-K, prompts, etc.

### GitHub Workflow

If you don't have direct access:

```text
Fork → Clone → Create Branch → Make Changes
       ↓
     Test
       ↓
     Commit → Push → Pull Request
```

Example:

```bash
git checkout -b feature/add-source-citations

git add .
git commit -m "Add source citations"

git push origin feature/add-source-citations
```

Then create a **Pull Request** to the `main` branch.

When creating a PR, explain:

* **What** you changed
* **Why** you changed it
* **How** you tested it

---

# 🔮 Ideas to Explore

Once the basic RAG works, try adding:

* [ ] Multiple PDF support
* [ ] DOCX/TXT support
* [ ] Source/page citations
* [ ] Chat history
* [ ] Streaming responses
* [ ] FastAPI `/upload` and `/ask` APIs
* [ ] Reranking
* [ ] Hybrid search
* [ ] Redis caching
* [ ] RAG evaluation
* [ ] Docker
* [ ] Cloud deployment

---

## 🎓 The Goal

Don't just say:

> **"I know RAG."**

Be able to say:

> **"I built a RAG application, understood how it works, debugged it, and contributed to a real GitHub project."**

**Learn → Build → Break → Debug → Improve → Share 🚀**
