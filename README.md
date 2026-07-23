# 🛠️ Nova — Neurofive Solutions IT Helpdesk Chatbot

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/LLM-Groq%20API-00A67E)
![License](https://img.shields.io/badge/License-MIT-green)

A persona-driven AI chatbot built with a custom system prompt, served through the **Groq API** (Llama 3.3 70B) and wrapped in a polished **Streamlit** chat interface. Nova plays the role of a friendly IT Helpdesk Assistant for a fictional company, Neurofive Solutions — staying in character, giving real troubleshooting steps, and politely declining anything off-topic.

> Built as part of **Week 2 · Generative AI & Prompt Engineering**

---

## ✨ Features

- 💬 **Real-time chat UI** with message history, avatars, and typing indicator
- 🎭 **Persona-locked system prompt** — Nova never breaks character or reveals it's an LLM
- 🚧 **Off-topic guardrails** — politely redirects unrelated requests back to IT topics
- 🔐 **Security-aware** — never hands out passwords or bypasses company policy
- ⚡ **Fast inference** via Groq's LPU-accelerated API
- 🎨 **Custom dark theme** with a branded hero header and sidebar
- ☁️ **One-click deploy** to Streamlit Community Cloud

---

## 🖼️ Preview

| Chat in action |
|---|
| *(Add a screenshot or GIF of the app here after deploying)* |

---

## 🧠 How it works

The bot's personality lives entirely in a **system prompt** (see `app.py`), which instructs the model to:

1. Stay in character as "Nova" at all times
2. Give concise, step-by-step IT troubleshooting advice
3. Redirect off-topic questions back to IT support
4. Never share passwords or bypass security policy
5. Keep replies short and friendly, with the occasional emoji

Every user message is sent to Groq's `llama-3.3-70b-versatile` model alongside this system prompt and the running conversation history, so the model has full context for follow-up questions.

---

## 📁 Project structure

```
neurofive-it-helpdesk-bot/
├── app.py                  # Streamlit app + persona + chat logic
├── requirements.txt        # Python dependencies
├── .env.example             # Template for your local API key
├── .streamlit/
│   └── config.toml          # Theme configuration
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Getting started (local)

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/neurofive-it-helpdesk-bot.git
cd neurofive-it-helpdesk-bot
```

### 2. Create a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Groq API key
Get a free key at [console.groq.com/keys](https://console.groq.com/keys), then:
```bash
cp .env.example .env
# then edit .env and paste your key
```
`.env` looks like:
```
GROQ_API_KEY=gsk_your_actual_key_here
```

### 5. Run the app
```bash
streamlit run app.py
```
The app opens at `http://localhost:8501`.

---

## ☁️ Deploy to Streamlit Community Cloud

1. Push this repo to your own GitHub account (make sure `.env` is **not** committed — it's already in `.gitignore`).
2. Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with GitHub.
3. Click **New app** → select your repo, branch (`main`), and `app.py` as the entry point.
4. Before deploying, open **Advanced settings → Secrets** and add:
   ```toml
   GROQ_API_KEY = "gsk_your_actual_key_here"
   ```
5. Click **Deploy**. Your chatbot will be live at a public `*.streamlit.app` URL within a minute or two.

> The app reads the key from `st.secrets` automatically when deployed, and falls back to your local `.env` when run locally — no code changes needed between environments.

---

## 🧪 Testing the persona

Try prompts like:
- "My laptop has been really slow the past two days, what should I check?"
- "I forgot my email password, can you just reset it for me?"
- "How do I connect to the VPN from home?"
- "Can you give me a recipe for chicken curry?" *(off-topic — watch Nova redirect)*
- "The 3rd floor printer says paper jam but there's no paper stuck."

---

## 🛡️ Tech stack

| Layer | Tool |
|---|---|
| LLM | [Groq API](https://console.groq.com/) — `llama-3.3-70b-versatile` |
| UI | [Streamlit](https://streamlit.io/) |
| Language | Python 3.9+ |
| Hosting | Streamlit Community Cloud |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋 Author

Built by [Your Name] — Week 2 submission, Generative AI & Prompt Engineering.
