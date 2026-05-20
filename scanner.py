# scanner.py

```python
import requests
import pandas as pd
import time
from datetime import datetime

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

BASE_URL = "https://api.binance.com"


def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=payload)


def scan_market():

    exchange_info = requests.get(
        f"{BASE_URL}/api/v3/exchangeInfo"
    ).json()

    symbols = [
        s['symbol']
        for s in exchange_info['symbols']
        if s['quoteAsset'] == 'USDT'
        and s['status'] == 'TRADING'
    ]

    matched = []

    for symbol in symbols:

        try:

            data = requests.get(
                f"{BASE_URL}/api/v3/klines",
                params={
                    "symbol": symbol,
                    "interval": "15m",
                    "limit": 3
                },
                timeout=5
            ).json()

            df = pd.DataFrame(data)

            close0 = float(df.iloc[2][4])
            close1 = float(df.iloc[1][4])
            close2 = float(df.iloc[0][4])

            vol0 = float(df.iloc[2][5])
            vol1 = float(df.iloc[1][5])

            condition = (
                close0 > close1 * 1.02 and
                close1 < close2 * 0.96 and
                close0 > close2 and
                vol0 > vol1
            )

            if condition:

                recovery = round(
                    ((close0 - close1) / close1) * 100,
                    2
                )

                matched.append(
                    f"{symbol} | Recovery: {recovery}%"
                )

            time.sleep(0.03)

        except:
            pass

    if matched:

        msg = "🚀 V-SHAPE RECOVERY COINS\n\n"

        for coin in matched[:15]:
            msg += f"{coin}\n"

        send_telegram(msg)


while True:

    try:

        print(f"Scanning {datetime.now()}")

        scan_market()

        print("Waiting 15 mins...\n")

        time.sleep(900)

    except Exception as e:

        print(e)

        time.sleep(60)
```

---

# requirements.txt

```text
pandas
requests
```

---

# render.yaml

```yaml
services:
  - type: worker
    name: crypto-scanner
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python scanner.py
```

---

# README.md

```text
Crypto Scanner
```

---

# EXACT PROCESS

## STEP 1

GitHub repository open karo.

## STEP 2

Top right me:

Add file → Create new file

## STEP 3

Pehli file name:

scanner.py

Poora scanner.py code paste karo.

Neeche:

Commit new file

## STEP 4

requirements.txt banao.

## STEP 5

render.yaml banao.

## STEP 6

README.md banao.

## STEP 7

Render open karo:

[https://dashboard.render.com](https://dashboard.render.com)

## STEP 8

New + → Background Worker

## STEP 9

GitHub repo select karo.

## STEP 10

Deploy karo.

---

# IMPORTANT

scanner.py me ye replace zaroor karna:

```python
BOT_TOKEN = "8686170685:AAFUbav9bo8npfu9MMKrb3krED_naFffAZM"
CHAT_ID = "1155630899"
```

Apne actual Telegram bot token aur chat id se.
