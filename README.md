# 🚀 Binance Futures Testnet Trading Bot

A simplified Python trading bot that allows you to place **Market**, **Limit**, and **Stop-Limit** orders on Binance Futures Testnet (USDT-M).
Includes both **CLI** and **Streamlit UI**, with proper logging, validation, and error handling.

---

## 📌 Features

* ✅ Place **MARKET**, **LIMIT**, and **STOP-LIMIT** orders
* ✅ Supports **BUY** and **SELL**
* ✅ CLI + Interactive Mode
* ✅ Lightweight UI using Streamlit
* ✅ Input validation
* ✅ Logging of requests, responses, and errors
* ✅ Clean modular architecture

---

## 🏗️ Project Structure

```
trading-bot/
│── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   ├── exceptions.py
│
│── main.py
│── ui.py
│── requirements.txt
│── .env
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone <your-repo-url>
cd trading-bot
```

---

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Setup Environment Variables

Create a `.env` file:

```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_SECRET_KEY=your_testnet_secret_key
```

---

### 5. Get Binance Testnet API Keys

1. Go to: https://testnet.binancefuture.com
2. Login
3. Open **API Management**
4. Create API key
5. Enable:

   * TRADE
   * USER_DATA

---

## ▶️ Running the Application

---

# 💻 CLI Usage

---

## ✅ MARKET ORDER

```
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

---

## ✅ LIMIT ORDER

```
python main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.004 --price 30000
```

---

## ✅ STOP-LIMIT ORDER

```
python main.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.002 --price 67000 --stop_price 66000
```

---

## 💬 Interactive Mode

```
python main.py
```

Follow prompts in terminal.

---

# 🌐 UI Usage (Streamlit)

---

## Run UI

```
streamlit run ui.py
```

Open browser:

```
http://localhost:8501
```

---

## UI Features

* Place MARKET / LIMIT / STOP-LIMIT orders
* Real-time validation
* Success and error display

---

# 📊 Logs

Logs are stored in:

```
trading.log
```

Includes:

* API requests
* API responses
* Errors

---

# ⚠️ Assumptions & Constraints

* Uses **Binance Futures Testnet (USDT-M)** only
* Minimum order value must be ≥ **100 USDT**
* API keys must be from **Futures Testnet**, not live Binance

---

# ❗ Common Errors & Fixes

### 1. Invalid API Key

```
APIError(code=-2015)
```

✔ Use correct **testnet API key**

---

### 2. Minimum Notional Error

```
Order's notional must be no smaller than 100
```

✔ Increase quantity or price

---

### 3. Stop-Limit Trigger Error

```
Order would immediately trigger
```

✔ Ensure:

* BUY → stop_price > market price
* SELL → stop_price < market price

---

# 🧪 Example Test Cases

| Type       | Command              |
| ---------- | -------------------- |
| Market Buy | `--type MARKET`      |
| Limit Buy  | `--price 30000`      |
| Stop Limit | `--stop_price 66000` |

---





## 👨‍💻 Author

Tanishq Pal

---
