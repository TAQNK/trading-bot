import argparse
from bot.validators import validate_order
from bot.orders import OrderService
from bot.logging_config import get_logger
from bot.exceptions import ValidationError, APIError

def main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol")
    parser.add_argument("--side", choices=["BUY", "SELL"])
    parser.add_argument("--type", choices=["MARKET", "LIMIT", "STOP_LIMIT"])
    parser.add_argument("--quantity", type=float)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop_price", type=float)

    args = parser.parse_args()
    logger = get_logger()

    # Interactive mode
    if not args.symbol:
        args.symbol = input("Symbol: ")
    if not args.side:
        args.side = input("Side (BUY/SELL): ").upper()
    if not args.type:
        args.type = input("Type (MARKET/LIMIT/STOP_LIMIT): ").upper()
    if not args.quantity:
        args.quantity = float(input("Quantity: "))
    if args.type in ["LIMIT", "STOP_LIMIT"] and not args.price:
        args.price = float(input("Price: "))
    if args.type == "STOP_LIMIT" and not args.stop_price:
        args.stop_price = float(input("Stop Price: "))

    try:
        validate_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price,
            args.stop_price
        )

        service = OrderService(logger)

        print("\n📊 Order Summary:")
        print(vars(args))

        response = service.place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price,
            args.stop_price
        )

        # ✅ FIX: Validate response
        if not response or "orderId" not in response:
            print("\n❌ Order Failed")
            print("Full Response:", response)
            return

        print("\n✅ SUCCESS")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

    except ValidationError as ve:
        print(f"\n❌ Validation Error: {ve}")

    except APIError as ae:
        print(f"\n❌ API Error: {ae}")

    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")

if __name__ == "__main__":
    main()