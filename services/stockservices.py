from data.exchange_data import exchange_data
from utility.utilities import Utilities

class StockServices(Utilities):
    
    """This class provide stockmarket services such as dividend, P/E ratio calculation
     
    Methods
    -------
    calculate_dividend_yield:
        Method to calculate dividend yield of stock
    
    calculate_pe_ratio:
        Method to calculate P/E ratio of stock
    
    """
    
    def calculate_dividend_yield(self, symbol:str, price:float | int) -> float | int:
        
        """Given any symbol and price as input, this method calculates the dividend yield

        Args:
            symbol (str): This is the symbol of stocks
            price (float | int): This is the price of stock in pennies

        Raises:
            ValueError: if price provided as argument is zero or less than zero, this ValueError is raised. This prevents the method 
            to have price value as zero or negative

        Returns:
            float | int: returns the calculated dividend yield in integer or float format depending on stock type is 'Common' or 'Preferred'
        """
        
        # validating all the arguments provided to this method
        symbol = self.validate_stock_symbol(symbol,exchange_data)
        price = self.str_to_float(price)
        
        stock = exchange_data[symbol]
        if price<=0:
            raise ValueError("Price is invalid")
        return stock["last_dividend"] / price if (stock["type"]=="Common") else stock["fixed_dividend"] * stock["par_value"] / price
    
    
    def calculate_pe_ratio(self, symbol:str, price:float | int) -> float | int:
        
        """Given any price as input, this method calculate the P/E Ratio
        
         Args:
            symbol (str): This is the symbol of stocks
            price (float | int): This is the price of stock in pennies

        Raises:
            ValueError: if the dividend value of a stock is zero, then P/E ratio cannot be find out. So, cannot divide by zero ValueError 
            is raised in cases where dividend becomes zero 

        Returns:
            float| int: returns the calculated P/E ratio in float or integer format.
        """
        
        # validating all the arguments provided to this method
        symbol = self.validate_stock_symbol(symbol,exchange_data)
        price = self.str_to_float(price)
        
        dividend = self.calculate_dividend_yield(symbol, price)
        if dividend == 0:
            raise ValueError("Cannot divide by zero")
        return price/dividend
    
   