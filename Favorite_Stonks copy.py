favorite_stocks = {
    'TSLA': '$1,140.00',
    'AAPL': '$160.99',
    'AMZN': '$3,676.57',
    'FB': '$345.45',
    'MSFT': '$343.51',
    'TWTR': '$48.50',
    'SBUX': '$110.88',
    'DIS': '$154.10',
    'AMC': '$41.09',
    'NFLX': '$677.50',
    }

print("Welcome, I have a list here with ten of my favorite stocks. "
    "Give a guess of what you think is one of my favorites. "
    "If you get it right I'll tell you how much it's worth.")

guess = input("\nWhich stock do I like?: ")
guess = guess.upper()

if guess in favorite_stocks:
    print("That's right!", guess, "is worth", favorite_stocks[guess],".")
else:
    print("Sorry, that is not one of my favorite stocks:(")