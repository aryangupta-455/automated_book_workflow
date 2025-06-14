# 📘 Automated Book Workflow System

This project automates the transformation of classical book chapters using AI — from scraping to rewriting, reviewing, and storing versions.

> ✅ Internship Task — AI Publication Pipeline

---

## 🚀 Features

- ✅ Scrapes book chapters from [Wikisource](https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1)
- ✅ AI rewriting using GPT (OpenAI API)
- ✅ AI reviewing (editing/clarifying)
- ✅ Human-in-the-loop editor (CLI)
- ✅ Version tracking using ChromaDB
- ✅ Search + feedback-aware retrieval
- ✅ CLI for human feedback and final editing

---

## 🧱 Tech Stack

- Python
- Playwright (web scraping)
- OpenAI API (GPT-3.5)
- ChromaDB (vector store)
- Dotenv (API key management)

---

## 📂 How to Run

1. Clone the repo
2. Create a `.env` file with your OpenAI key:
    ```
    OPENAI_API_KEY=your_key_here
    ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    playwright install
    ```
4. Run the main app:
    ```
    python app.py
    ```
5. Run search test:
    ```
    python search_test.py
    ```

---

## 🎥 Demo Video

👉 [Insert Loom or Google Drive link here]

---

## ⚠️ Disclaimer

This project was built purely for **evaluation purposes only** as part of an internship task.  
The developer retains full rights to all work.

---

## 📬 Author

- Aryan Gupta  
- [GitHub Profile](https://github.com/aryangupta-455)
