from utility.time_logger import TimeLogger
from services.trade_history import TradeHistory
from utility.utilities import Utilities
from data.exchange_data import exchange_data
class Trade(Utilities, TradeHistory, TimeLogger):
    """This class helps to maintain trade related functionalities

    Methods
    -------
    record_trade:
        This method helps to log and record the trade
        
    """
    def record_trade(self, symbol:str, quantity:float | int, price:float | int, order:str = "Buy"):
        
        """This method records a trade, with timestamp, quantity, buy or sell indicator and price and store in a dictionary
        
         Args:
            symbol (str): This is the symbol of stocks
            quantity(float | int): This is the quantity of stocks traded
            price (float | int): This is the price of stock in pennies
            order (str): This is the trade type, whether the trade performed is sell order or buy order

        Returns:
            dict: This method returns a dictionary with trade data (timestamp, order, quantity, traded_price)
        """
        
        # validating all the arguments provided to this method
        symbol = self.validate_stock_symbol(symbol,exchange_data)
        quantity = self.str_to_float(quantity)
        price = self.str_to_float(price)
        order = self.validate_order(order)
        
        trade_data = {
        "time": self.get_current_time(),
        "order": "buy" if order=="buy" else "sell",
        "quantity": quantity,
        "traded_price": price
        }
        
        if symbol not in self.trades:
            self.trades[symbol] = [trade_data]
        else:
            self.trades[symbol].append(trade_data)
        
        return trade_data