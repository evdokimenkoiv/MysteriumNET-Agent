import os
import time
import json
import socket
import requests

MANAGER_URL = os.getenv("MANAGER_URL", "http://127.0.0.1:8080")
MANAGER_SECRET = os.getenv("MANAGER_SECRET", "")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS", "")
AGENT_NAME = os.getenv("AGENT_NAME", socket.gethostname())

def register_once():
    url = f"{MANAGER_URL.rstrip('/')}/agents/register"
    headers = {"X-Manager-Secret": MANAGER_SECRET}
    payload = {
        "agent_name": AGENT_NAME,
        "wallet_address": WALLET_ADDRESS,
        "host": socket.gethostname(),
        "version": "1.0.0",
    }
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=10)
        print("Register:", r.status_code, r.text)
    except Exception as e:
        print("Register error:", e)

def main():
    print("Agent starting...")
    print("MANAGER_URL=", MANAGER_URL)
    while True:
        register_once()
        time.sleep(60)

if __name__ == "__main__":
    main()
