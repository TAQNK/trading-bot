from bot.exceptions import ValidationError

def validate_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    if not symbol:
        raise ValidationError("Symbol is required")

    if side not in ["BUY", "SELL"]:
        raise ValidationError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValidationError("Order type must be MARKET, LIMIT, or STOP_LIMIT")

    if quantity <= 0:
        raise ValidationError("Quantity must be greater than 0")

    if order_type == "LIMIT" and price is None:
        raise ValidationError("Price is required for LIMIT orders")

    if order_type == "STOP_LIMIT":
        if price is None or stop_price is None:
            raise ValidationError("Price and Stop Price are required for STOP_LIMIT")

def validate_notional(order_type, price, quantity):
    if order_type in ["LIMIT", "STOP_LIMIT"] and price:
        if price * quantity < 100:
            raise ValidationError("Order value must be at least 100 USDT")

def validate_stop_limit(side, price, stop_price, current_price):
    if side == "BUY" and stop_price <= current_price:
        raise ValidationError("For BUY, stop_price must be above market price")

    if side == "SELL" and stop_price >= current_price:
        raise ValidationError("For SELL, stop_price must be below market price")