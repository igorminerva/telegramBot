# 🌟 Telegram Daily Quotes Bot

A simple and fun Telegram bot that shares not inspirational quotes with users on request and sends a daily quote to subscribers — personalized with their name.

---

## ✨ Features

- `/start` — Greets the user with a welcome message.
- `/subscribe` — Subscribe to daily motivational quotes.
- `/quote` — Get a random quote on demand.
- Sends quotes daily to all subscribers (automated with a scheduler).
- Quotes stored in a `CSV` file for easy editing.
- Personalized responses using the user's Telegram username or first name.

---

## 📁 Project Structure

telegramBot/ <br>
├── main.py # Main bot logic <br>
├── quotes.csv # List of quotes (one per line) <br>
├── requirements.txt # Dependencies <br>
└── README.md # This file

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/telegram-daily-quotes-bot.git
cd telegram-daily-quotes-bot
```
### 2. Set Up a Virtual Environment

python3 -m venv .venv
source .venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Add Your Quotes

Edit quotes.csv and add one quote per line:

Stay positive, work hard, make it happen.
Believe you can and you're halfway there.
Don't watch the clock; do what it does — keep going.

    Ensure it's saved in UTF-8 encoding (LibreOffice/Excel lets you choose this on export).

### 5. Configure Your Bot

In main.py, replace:

BOT_TOKEN = 'YOUR_BOT_TOKEN'

with your actual bot token from BotFather.
🧪 Run the Bot

python main.py

🛠 Requirements

    Python 3.8+

    python-telegram-bot

    pandas

    apscheduler

Install with:

pip install -r requirements.txt

📜 License

MIT License — feel free to use, modify, and share!
💡 Future Ideas

    Web dashboard for managing quotes

    Google Sheets integration

    Quote categories

    User stats / analytics

🤝 Connect With Me

Feel free to reach out or contribute!
Check out my **[LinkedIn](https://www.linkedin.com/in/igorminerva/)** or **[GitHub](https://github.com/igorminerva)**.
