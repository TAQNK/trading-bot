import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.client = Client(
            os.getenv("BINANCE_API_KEY"),
            os.getenv("BINANCE_SECRET_KEY"),
            testnet=True   # ✅ IMPORTANT FIX
        )

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "quantity": str(quantity),  # ✅ FIX
                "recvWindow": 5000
            }

            if order_type == "MARKET":
                params["type"] = "MARKET"

            elif order_type == "LIMIT":
                params["type"] = "LIMIT"
                params["price"] = str(price)
                params["timeInForce"] = "GTC"

            elif order_type == "STOP_LIMIT":
                params["type"] = "STOP"
                params["price"] = str(price)
                params["stopPrice"] = str(stop_price)
                params["timeInForce"] = "GTC"
                params["workingType"] = "MARK_PRICE"

            response = self.client.futures_create_order(**params)

            print("RAW BINANCE RESPONSE:", response)  # debug

            return response

        except Exception as e:
            print("❌ BINANCE ERROR:", str(e))
            raise