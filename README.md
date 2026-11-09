# ☀️ Morning Dispatch Agent

An automated, serverless daily briefing AI agent built with Python, Google Gemini, and GitHub Actions. Every morning at 7:00 AM IST, the agent automatically aggregates local weather forecasts and regional Tamil Nadu news, synthesizes an executive summary, and delivers the briefing directly to your Telegram chat—with zero local machine dependency.

---

## 🚀 Features

- **Automated Weather Monitoring:** Retrieves current conditions, temperature ranges, and precipitation alerts.
- **Regional News Aggregation:** Gathers top headlines across Tamil Nadu via RSS/API feeds.
- **LLM Synthesis:** Synthesizes clear, bulleted executive briefs using Google's `gemini-3.5-flash-lite` model.
- **Instant Telegram Delivery:** Dispatches notifications via the Telegram Bot API.
- **Zero-Maintenance Scheduling:** Runs serverless on GitHub Actions cron runners.

---

## 🛠️ Tech Stack

- **Language:** Python 3.11+
- **LLM Engine:** Google Gemini API (`google-genai` SDK)
- **Model:** `gemini-3.5-flash-lite`
- **Automation / CI/CD:** GitHub Actions (Cron schedule: `30 1 * * *` UTC / 7:00 AM IST)
- **Delivery:** Telegram Bot API (`requests`)

---

## 📂 Project Structure

```text
morning_dispatch/
├── .github/
│   └── workflows/
│       └── dispatch.yml    # GitHub Actions cron workflow
├── outputs/                # Local daily markdown archive
├── agent.py                # Main orchestrator script
├── news.py                 # News fetching module
├── notifier.py             # Telegram delivery service
├── weather.py              # Weather data retrieval module
├── requirements.txt        # Project dependencies
├── .env.example            # Sample environment variables
└── .gitignore
