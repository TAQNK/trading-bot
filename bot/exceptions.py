class ValidationError(Exception):
    """Raised when input validation fails"""
    pass

class APIError(Exception):
    """Raised when Binance API fails"""
    pass