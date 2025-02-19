ticker_symbols = {
    "GM": "General Motors",
    "CAT": "Caterpillar",
    "EK": "Eastman Kodak",
    "CRK": "Circle K",
    "WMT": "Walmart Inc",
    "F": "Ford Motor Company",
    "MRCY": "Mercury Systems Inc",
    "DOV": "Dover Corp",
}

trader_info = [
    ("GM", 64, "15-aug-1968", 48),
    ("EK", 247, "08-mar-1985", 0.55),
    ("CRK", 10, "06-oct", 18),
    ("DOV", 71, "27-nov-1995", 202),
    ("DOV", 75, "14-sep-1935", 202),
    ("CAT", 90, "09-apr-1983", 353),
    ("WMT", 18, "18-jan-1995", 104),
    ("WMT", 13, "25-aug-1980", 48),
    ("GM", 85, "13-feb-1964", 48),
    ("CAT", 98, "06-jun-2010", 353),
    ("F", 385, "05-jan-1984", 9),
    ("MRCY", 98, "16-dec-1986", 44),
    ("F", 804, "17-feb-2024", 9),
]


# Finds total cost of shares for all companies
def total_share_costs_per_purchase():
    print(" List of all purchases \n ========================== \n")
    # destructuring all values per tuple.
    for ticker_symbol, shares, date, share_cost in trader_info:
        # finding company's full name by their market ticker
        if ticker_symbol in ticker_symbols:
            company_name = ticker_symbols[ticker_symbol]
        else:
            print(f"Company {ticker_symbol} not found in purchase history")
        # calculating cost of each purchase for which company
        total_cost = shares * share_cost
        print(f"Company: {company_name} stock bought for ${total_cost}")


total_share_costs_per_purchase()

# Grouping Stock Purchases and Total Value
# I need to create a new way of organizing the presented data
# Instead of finding the total cost for each purchase,
# I must group together purchases made from each company.
# The ticker for a company should be a key, it is unique to a
# company. The value of each key, will be all purchases relating
# to that company
# I will be working with the data that is already created, but sorting it by
# company. I do not want my other function to be responsible for this algorithm.

organized_purchases_by_ticker_symbol = {}


def purchases_per_company():
    # I have all possible companies from which a customer might buy.
    # I can begin this process by iterating through that dictionary.

    for company_ticker, company_name in ticker_symbols.items():
        # I forgot to initialize an empty list value for each company.
        # This allows for me to update the list instead of creating a new list through each iteration
        organized_purchases_by_ticker_symbol[company_ticker] = []
        # As I begin a new iteration,
        # I will know which company I should be looking for in the purchase history.
        for purchase in trader_info:
            # When I find a purchase made from a company corresponding
            # to the ticker that is iterating I can store that purchase in the new dictionary
            if company_ticker == purchase[0]:
                # creates a new key value pair in the new dictionary.
                organized_purchases_by_ticker_symbol[company_ticker].append(purchase)
                # how can I update a list value stored in a dictionary?

        # This is the first half of the problem completed,
        # and what this function is responsible for doing.


purchases_per_company()


# Now, I have a dictionary that groups together purchases in a list, associated with
# the company from which the purchases were made.
# The goal now is to display the total holdings that this customer has at each company
# I can destructure the dictionary's key value pairs
# The keys in the listings will be the company's ticker
# The values of the keys will be a list of tuples representing unique purchases made.


def display_customer_holdings():
    print("Your purchase by company")
    # I need to destructure the key value pairs
    for company, customer_purchases in organized_purchases_by_ticker_symbol.items():
        # initializes variable, resets when new company begins to iterate
        customer_shares = 0
        company_share_cost = 0
        # company is a string, customer_purchases is the list of tuples
        # I cannot access the properties of the tuples directly they must be destructered as well
        for company_ticker, shares, date, share_cost in customer_purchases:
            # compares outer loops company to tuples to company_ticker
            if company == company_ticker:
                # reassignes outer level variables
                customer_shares += shares
                company_share_cost = share_cost
        company_share_cost *= customer_shares
        print(
            f"*{company} holdings: {company_share_cost}"
        )


display_customer_holdings()
