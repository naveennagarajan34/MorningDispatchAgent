from datetime import datetime
import json
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

from news import get_top_news
from weather import get_weather
from notifier import send_telegram_message

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def build_morning_briefing():
    print("1. Fetching local weather data...")
    weather_data = get_weather()

    print("2. Fetching Tamil Nadu news updates...")
    news_data = get_top_news(limit=5)

    print("3. Synthesizing briefing with Gemini...")

    prompt = f"""
You are an executive morning briefing assistant.

Here is the current weather data for the user's location:
{json.dumps(weather_data, indent=2)}

Here are today's top Tamil Nadu news stories:
{json.dumps(news_data, indent=2)}

Produce a clean, professional, and concise "Morning Dispatch" structured exactly as:
1. **Weather Outlook**: 2-3 sentences covering current conditions, forecast highs/lows, and whether rain precautions are needed.
2. **Top Tamil Nadu Briefs**: Bullet points summarizing the main news stories clearly in 1-2 lines each.
3. **Daily Takeaway**: One crisp closing note for the day ahead.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite", contents=prompt
    )

    return response.text


def save_dispatch_to_file(content):
    """
    Saves the briefing to an outputs/ directory with a date stamp.
    """
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    today_str = datetime.now().strftime("%Y-%m-%d")
    file_path = output_dir / f"dispatch_{today_str}.md"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# Morning Dispatch — {today_str}\n\n")
        f.write(content)

    print(f"\n[Saved to {file_path}]")
    return file_path


if __name__ == "__main__":
    briefing = build_morning_briefing()

    print("\n" + "=" * 50)
    print("           MORNING DISPATCH")
    print("=" * 50 + "\n")
    print(briefing)

    # Save to disk
    save_dispatch_to_file(briefing)

    # Dispatch to Telegram
    print("\nSending briefing to Telegram...")
    send_telegram_message(briefing)
