import os
import time
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data, timeout=15)

def main():
    send_telegram("✅ 雲端交易監控機器人已啟動")
    while True:
        # 先測試用，每 15 分鐘通知一次
        send_telegram("📡 雲端監控中：程式仍正常運作")
        time.sleep(900)

if __name__ == "__main__":
    main()