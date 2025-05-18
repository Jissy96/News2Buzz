# 📰✨ News2Buzz

**AI-Powered Social Media Post Generator with Brand Tone, Bias Detection & Emoji/Sticker Personalization**

---

## 🚀 Project Overview

**News2Buzz** is an intelligent end-to-end platform that transforms breaking news and trending topics into branded, tone-aware, multimodal social media posts. It combines Natural Language Processing (NLP), generative AI, and data pipelines to deliver rich content (text + emojis + stickers) for platforms like Instagram, LinkedIn, X (Twitter), and more.

This project is developed by a 6-member student team at Loyalist College as part of Semester 4.

---

## 🎯 Core Features

- 🔍 **News Scraping & Intelligence** (NewsAPI, Reddit, Google News)
- 🧠 **Sentiment Analysis & Bias Detection**
- ✍️ **AI Content Generation with Brand Tone**
- 😊 **Emoji and Sticker Personalization**
- 📅 **Post Scheduling and Platform Integration**
- 📊 **Engagement Prediction and A/B Testing**
- 🧾 **Trend & Bias Dashboard for Monitoring**

---

## 🧱 Tech Stack

| Layer        | Tools Used |
|--------------|------------|
| **Scraping** | NewsAPI, snscrape, Reddit API |
| **Processing** | Python, Spacy, Transformers, Airflow |
| **Streaming** | Apache Kafka, Redis |
| **NLP Models** | BERT, T5, LLaMA, GPT-style models |
| **Storage** | OpenSearch, SQL/NoSQL |
| **Backend** | FastAPI, Celery |
| **Frontend** | React.js (or basic HTML/CSS prototype) |
| **Deployment** | Docker, GitHub Actions (planned) |

---

## 📂 Project Structure

```bash
news2buzz/
├── backend/
│   ├── fastapi_app/
│   ├── services/  # Ingestor, Generator, Scheduler, etc.
│   └── models/    # ML models and utils
├── frontend/
│   ├── public/
│   └── src/
├── airflow_dags/
├── notebooks/
├── data/
│   └── sample_news/
├── .github/
│   └── workflows/
├── README.md
└── requirements.txt

