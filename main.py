import yfinance as yf, requests, os

# Download live Gold - this runs inside GitHub, no Google ban
data = yf.download("GC=F", period="2d", interval="15m", progress=False)
price = float(data['Close'].iloc[-1])
low = float(data['Low'].iloc[-2])

# Your HOWZA A+ logic (cloned from your NotebookLM link)
# Sweep low + reclaim = A+
is_a_plus = low < 3970 and price > low + 8

if is_a_plus:
    msg = f"📊 *AI-ANALYST- A+ SIGNAL*\nGold swept ${low:.2f} -> now ${price:.2f}\n\nEntry: 3975-3985\nSL: 3964\nTP: 4025 / 4060\n\nThis analyst lives on GitHub, no ban from Google"
else:
    msg = f"AI-ANALYST- Live Check: Gold ${price:.2f} - No A+ yet. Running 24/7 from GitHub."

# Send to your Telegram group
requests.post(f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage",
json={"chat_id": os.getenv("CHAT_ID"), "text": msg, "parse_mode":"Markdown"})
