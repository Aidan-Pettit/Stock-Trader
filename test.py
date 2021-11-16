import time
import random


def analyze():
    initial_cash = 1000
    cash = 1000
    initial = 10.00
    last_price = 10.00
    current_price = 10.00
    bought = False
    bought_price = 0
    i = 0

    while i < 200:
        time.sleep(1)
        last_price = current_price
        current_price = round(initial + (random.random() - 0.5) / 10, 2)

        print(current_price)
        difference = current_price - last_price

        if difference < -0.05 and not bought:
            print('Buy')
            bought = True
            bought_price = current_price
            cash -= 10
        if difference > 0.05 and bought:
            print('Sell')
            cash = round(cash + cash * difference, 2) - 10
            print('Cash: ', cash)
            bought = False
        i += 1

    print('Cash: $', cash)
    print('Total Profit: $', cash - initial_cash)
    print('Well Done!')


analyze()
