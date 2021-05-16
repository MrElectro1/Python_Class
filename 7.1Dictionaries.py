#Eric Hayden 05/02/2021
try:
    #Dictionary
    price= {
        'TSLA': '710',
        'NIO': '40',
        'PLUG': '30',
        'UBER': '55',
        'TLRY': '20',
        'PLTR': '23',
        'LYFT': '56',
        'AAPL': '132',
        'LAZR': '23',
        'PFE': '39'
    }
    Ticker= input('Please enter the ticker symbol you would like to learn the value of:')
    print(f"The value for {Ticker} is {price[Ticker]} dollars.")
except:
    print("Sorry we where unable to look up the requested ticker symbol.")