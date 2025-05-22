# 🤖 AI Prompt Generator

A full-stack AI-powered prompt engineering web application that:

* Accepts user queries
* Uses AI to generate responses in formal and casual tones
* Stores all interactions in a PostgreSQL database
* Displays history and results via a Streamlit frontend

---

## Live Demo

Frontend: [Streamlit App](https://unbeatablebann-ai-prompt-generator-app-vachgp.streamlit.app/)

Backend: [GitHub Repo](https://github.com/UnbeatableBann/AI-Prompt-Generator-Backend)

---

## Tech Stack

* **Frontend:** Streamlit
* **Backend:** Flask (Python)
* **Database:** PostgreSQL
* **AI Model:** Gemini / OpenAI (pluggable)
* **Deployment:**

  * Frontend: Streamlit Cloud
  * Backend: Render or Railway

---

## Features

* Mock Authentication (user ID stored in session)
* Tone/Style selection (Casual, Formal, or Both)
* AI-based prompt generation via REST API
* Query + Response storage with timestamps
* Full history view per user
* Environment-based configuration

---

## 🧪 Testing but in Backend

* Unit Tests:

  * Prompt formatting logic
  * AI generation logic (mocked)
  * API route validation
* Integration Test:

  * Simulates full interaction: query → AI response → DB store → history fetch

Run tests:

```bash
pytest test/
```

---

## Repo Structure (Frontend)

```
frontend/
├── app.py                # Streamlit UI
├── .env.example          # Environment config
├── requirements.txt      # Dependencies
└── README.md
```

---

## 📦 Setup & Run

### Backend (separate repo)

```bash
git clone https://github.com/your-backend-repo
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
cp .env.example .env      # Update DB_URL and API_KEY
python app.py
```

### Frontend

```bash
git clone https://github.com/your-frontend-repo
cd frontend
pip install -r requirements.txt
cp .env.example .env      # Set BACKEND_URL
streamlit run app.py
```

---

## Prompt Strategy

* The AI receives structured prompts like:

  ```
  Generate a response to the following user query in a casual and formal tone:
  Query: {user_input}
  ```
* Separate prompts help improve tone fidelity and generation quality.

---

## .env.example (Frontend)

```
BACKEND_URL=http://localhost:5000
```

---

## .env.example (Backend)

```
DATABASE_URL=postgresql://user:password@host:port/dbname
API_KEY=your-genai-api-key
```

---

## Contributing

Me and Myself. You also contribute but be meaningful.

---

## License

MIT License
