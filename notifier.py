import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram_message(message: str):
    """
    Sends a text message directly to your Telegram chat via Telegram Bot API.
    """
    if not BOT_TOKEN or not CHAT_ID:
        print("[Notifier Error] Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID in .env")
        return False

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}

    try:
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        print("[Notifier] Telegram message sent successfully!")
        return True
    except Exception as e:
        print(f"[Notifier Error] Failed to send Telegram message: {e}")
        return False


if __name__ == "__main__":
    send_telegram_message("Test from Morning Dispatch Bot! Online and operational.")
