import streamlit as st
from bot.orders import OrderService
from bot.logging_config import get_logger
from bot.validators import validate_order
from bot.exceptions import ValidationError, APIError

logger = get_logger()
service = OrderService(logger)

st.title("📈 Trading Bot")

symbol = st.text_input("Symbol", "BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Type", ["MARKET", "LIMIT", "STOP_LIMIT"])
quantity = st.number_input("Quantity", min_value=0.0)

price = None
stop_price = None

if order_type in ["LIMIT", "STOP_LIMIT"]:
    price = st.number_input("Price", min_value=0.0)

if order_type == "STOP_LIMIT":
    stop_price = st.number_input("Stop Price", min_value=0.0)

if st.button("Place Order"):
    try:
        validate_order(symbol, side, order_type, quantity, price, stop_price)

        response = service.place_order(
            symbol, side, order_type, quantity, price, stop_price
        )

        if not response or "orderId" not in response:
            st.error("❌ Order Failed")
            st.write(response)
        else:
            st.success("✅ Order Placed")
            st.write(response)

    except ValidationError as ve:
        st.error(str(ve))
    except APIError as ae:
        st.error(str(ae))
    except Exception as e:
        st.error(str(e))