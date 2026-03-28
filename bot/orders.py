from bot.client import BinanceClient
from bot.exceptions import APIError

class OrderService:
    def __init__(self, logger):
        self.client = BinanceClient()
        self.logger = logger

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            self.logger.info(f"Order Request: {symbol} {side} {order_type}")

            response = self.client.place_order(
                symbol, side, order_type, quantity, price, stop_price
            )

            self.logger.info(f"Order Response: {response}")

            return response

        except Exception as e:
            self.logger.error(f"API Error: {str(e)}")
            raise APIError(str(e))