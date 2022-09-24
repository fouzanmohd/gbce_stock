from data.exchange_data import exchange_data
from utility.time_logger import TimeLogger
class TradeHistory(TimeLogger):
    """This class helps to maintain trade history and calculation associated with it
    
    Attributes
    ----------
    trades: dict
        this dictionary holds the trade history including timestamp, quantity, price and order type (buy or sell)

    Methods
    -------
    calculate_vws_price:
        this method calculate volume weighted stock price
    
    calculate_gbce:
        this method calculate GBCE All Share Index price
    """
    # dict to hold trade history data
    trades={}
    
    def calculate_vws_price(self, symbol:str) -> float | int:
        
        """This method calculate Volume Weighted Stock Price based on trades in past 5 minutes
        
         Args:
            symbol (str): This is the symbol of stocks

        Raises:
            ValueError: if total traded quantity is zero in any case, a ValueError is raised

        Returns:
            int | float: returns the calculated volume weighted price in integer or float format
        """
        
        # validating all the arguments provided to this method
        symbol = self.validate_stock_symbol(symbol,exchange_data)
        
        time_before_5_min = self.get_time_window(5).timestamp()
        total_trade_amount = 0
        total_qty = 0
        if symbol in self.trades.keys():
            for trades in self.trades[symbol]:
                if self.convert_date_to_timestamp(trades["time"])>=time_before_5_min:
                    total_trade_amount += trades["traded_price"] * trades["quantity"]
                    total_qty += trades["quantity"]
        
            if total_qty==0:
                raise ValueError("No result - because total traded quantity is 0")
            return total_trade_amount/total_qty
        return 0
    
    def calculate_gbce(self) -> int | float:
        
        """This method calculate the GBCE All Share Index using the geometric mean of the Volume Weighted Stock Price for all stocks

        Returns:
            int | float: returns the calculated GBCE value in integer or float format with maximum 3 decimals
        """
        
        total_vws_price = 1
        if self.trades:
            for symbol in self.trades.keys():
                total_vws_price*= self.calculate_vws_price(symbol)
        gbce = total_vws_price**(1/len(self.trades.keys()))
        return round(gbce,3)
           