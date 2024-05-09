class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name
    
    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name

def stock_purchase_history():
    # Create instances of Stock with the given data
    stocks = {
        "AAPL": Stock("AAPL", "Apple Inc"),
        "CAT": Stock("CAT", "Caterpillar"),
        "EK": Stock("EK", "Eastman Kodak"),
        "GOOG": Stock("GOOG", "Google"),
        "MSFT": Stock("MSFT", "Microsoft")
    }
    
    # Display stock purchase history
    print("Stock purchase history:")
    print("{:<10} {:<15}".format("Symbol", "Company Name"))
    for symbol, stock in stocks.items():
        print("{:<10} {:<15}".format(stock.get_symbol(), stock.get_company_name()))

# Testing the stock_purchase_history function
stock_purchase_history()
