# main.py

from question_c import Stock

def main():
    # Create instances of Stock class
    stocks = [
        Stock("AAPL", "Apple Inc"),
        Stock("CAT", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft")
    ]
    
    # Display symbol and company name for each stock
    for stock in stocks:
        print(f"Symbol: {stock.get_symbol()}, Company Name: {stock.get_company_name()}")

if __name__ == "__main__":
    main()
#add import