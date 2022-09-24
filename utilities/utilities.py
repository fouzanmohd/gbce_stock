class Utilities:
    """This class includes utility methods to validate arguments or inputs to other methods
    
    Methods
    -------
    validate_stock_symbol: 
        This method validate stock symbol input
    
    str_to_float: 
        This method convert str to float format
    
    validate_order:
        This method validates the order type input
    """
    def validate_stock_symbol(self, symbol:str, exchange_data:dict) -> str:
       
        """A method to validate whether the stock symbol is present in stock exchange data. This function prevents any wrong symbols 
           being entered to the function

        Args:
            symbol (str): unique symbol of stock 

        Raises:
            ValueError: if the symbol provided as argument does not exist in stock exchange data, a ValueError is raised

        Returns:
            str: returns the stock symbol present in stock exchange data 
        """
        
        if symbol not in exchange_data.keys():
            raise ValueError("Symbol does not exist in stock exchange")
        return symbol
    
    def str_to_float(self, value: int | float | str) -> int | float:
        
        """A method to convert string values to float. This helps to convert price and quantity to float when they '
           are provided in string format

        Args:
            value (int | float | str): It takes any value and converts to float only if the type of value is string

        Returns:
            float | int: returns the value in float or int format
        """
        
        if type(value)==str:
            return float(value)
        return value
    
    def validate_order(self, order: str) -> str:
        """This method helps to validate the order type. when this method is used for validation only 'Sell' and 'Buy' are 
           allowed to be passed as an argument

        Args:
            order (str): This is the trade type, whether the trade performed is sell order or buy order

        Raises:
            ValueError: If the input is not 'Sell' or 'Buy', a ValueError is raised

        Returns:
            str: returns 'Buy' or 'Sell'
        """
        if order.lower() != "buy" and order.lower() != "sell":
            raise ValueError("Order should be either 'Sell' or 'Buy'")
        return order