# 🤖 AI Prompt Generator

A full-stack AI-powered prototype that:

* Accepts user input
* Generates AI-based responses using prompt engineering
* Stores all interactions in a PostgreSQL database
* Displays results and history via a modern Streamlit UI

---

## 🌐 Live Demo

[Hosted Link](https://your-deployment-url.com)

---

## 💪 Tech Stack

| Layer    | Technology              |
| -------- | ----------------------- |
| Frontend | Streamlit               |
| Backend  | Flask + REST API        |
| Database | PostgreSQL + SQLAlchemy |
| AI Model | Gemini / GPT API        |
| Testing  | Pytest                  |

---

## 🧠 Prompt Engineering Strategy

Each query is reformulated to suit the selected tone:

* **Casual**: Friendly, conversational tone
* **Formal**: Professional and structured tone
* **Both (Default)**: Generates both tones

Example of internal prompt sent to the AI engine:

```
Please answer the following question in a [tone] tone: "[user_query]"
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/UnbeatableBann/ai-prompt-generator.git
cd ai-prompt-generator
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables

```bash
cp .env.example .env
```

Then fill in:

```
BACKEND_URL=http://localhost:5000 or render URL
DATABASE_URL=postgresql://username:password@localhost:5432/yourdb
GEMINI_API_KEY=your_gemini_api_key
```

### 4. Run the Backend Server

```bash
cd backend
flask run
```

### 5. Run the Streamlit Frontend

```bash
cd frontend
streamlit run app.py
```

### 6. Run Tests

```bash
pytest
```

---

## 🔧 Folder Structure

```
ai-prompt-generator/
├── backend/
│   ├── app.py
│   ├── models.py
│   └── ai_service.py
├── frontend/
│   └── app.py
├── tests/
│   ├── test_prompt.py
│   ├── test_api.py
│   └── test_full.py
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

## 🔮 Features

* ✍️ Text input form with tone selection
* 🎨 AI-generated responses (Casual, Formal, Both)
* 📅 Historical view of past prompts and answers
* 🌐 API integration with Gemini or GPT
* 📊 Unit + Integration Tests using Pytest

---

## 🚀 Deployment

* **Backend**: Deploy Flask API on Render.
* **Frontend**: Use Streamlit Community Cloud or host with Streamlit Sharing

---

## 📚 License

MIT License

---

## 👥 Contributors

Built with ❤️ by \Shadab Jamadar
