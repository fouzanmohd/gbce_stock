from services.stockservices import StockServices
from services.trade import Trade

class StockMarket(StockServices,Trade):
    """This is the main Class, Initiate this class to use all functionalities of the StockMarket.

        object.calculate_dividend_yield(stock_symbol, price)  --> calculates the dividend of stock with given price
        object.calculate_pe_ratio(stock_symbol, price)  --> calculates P/E ratio of stock with given price
        object.record_trade(stock_symbol,quantity,price,order_type) --> Records a trade with timestamp
        object.calculate_vws_price(stock_symbol) --> calculates volume weighted stock price
        object.calculate_gbce() --> calculates the GBCE All Share Index

    Args:
        StockServices (object): This object contains calculation methods such as calculate_dividend_yield and calculate_pe_ratio
        Trade (object): This object contains record_trade method, which can be used for recording a trade with timestamp,qty and Buy/Sell order
    """
    def __init__(self,name):
        self.name = name
        print(f"{name} StcokMarket created successfully.")

def main():
    gbce = StockMarket("GBCE")


if __name__ == "__main__":
    main()