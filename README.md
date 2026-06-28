# 📄 AI Resume Analyzer Agent

An Agentic AI web application that analyzes, scores, and improves your resume using Google Gemini 1.5 Flash.

## 🤖 What the Agent Does (5 Steps)

1. **Extract Skills** — reads your resume and lists all skills
2. **Match Analysis** — compares your resume to the target job role
3. **ATS Score** — scores your resume out of 100
4. **Rewrite Summary** — generates an improved professional summary
5. **Recommendations** — gives 5 actionable tips to improve your resume

## 📁 Project Files

```
resume-analyzer-agent/
├── app.py            → Streamlit web UI
├── agent.py          → Agentic AI logic (5-step analysis)
├── pdf_parser.py     → PDF text extraction
├── requirements.txt  → Python libraries
├── .env              → Your API key (never share this)
└── README.md         → This file
```

## 🚀 How to Run

### Step 1 — Install libraries
```bash
pip install -r requirements.txt
```

### Step 2 — Add your Gemini API key
- Get free key at: https://aistudio.google.com
- Open `.env` file and paste your key:
```
GOOGLE_API_KEY=your_key_here
```

### Step 3 — Run the app
```bash
streamlit run app.py
```

### Step 4 — Open in browser
```
http://localhost:8501
```

## ☁️ Deploy to Streamlit Cloud (Free)

1. Push this project to GitHub
2. Go to https://share.streamlit.io
3. Connect your GitHub repo
4. Set `GOOGLE_API_KEY` in Secrets
5. Deploy!

## 🛠️ Tech Stack

- **Streamlit** — Web UI
- **Google Gemini 1.5 Flash** — AI/LLM
- **pdfplumber** — PDF parsing
- **python-dotenv** — Environment variables

## 🌐 Live Demo
👉 **[Click Here to Use the App](https://resumeanalyzer-agent-dzj7nan7pqgntimuxm5yjj.streamlit.app/)**