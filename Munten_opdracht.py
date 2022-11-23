coins_amount = {}
coins_value = {'50 euros' : 5000,'20 euros' : 2000,'10 euros': 1000,'5 euros' : 500,'2 euros' : 200,'1 euros': 100,'50 cents' : 50, '20 cents' : 20, '10 cents' : 10, '5 cents' : 5, '1 cents' : 1}

def coin_calc():
    amount = 100 * (float(input("What is the amount you want to convert? Please enter a number in euro's (xx.xx)\n")))

    for coin in coins_value:                                                            #start a loop where the program tries every coin if it fits into the amount                    

        var = int(amount / coins_value[coin])                                           #define how many times the coin fits into the amount given and round that number down
        coins_amount[coin] = var

        amount = amount - (coins_value[coin] * var)                                     #resave the amount after subtracting already calculated amount

        if var != 0:                                                                    #print if any coins were needed to make the amount
            print('amount of ' + coin + ' u need is: ' + str(var))


    answer = input('Do you want to give another input? y/n\n')                          #ask if the user wants to calculate another value
    if answer == "y":                                   
        coin_calc()
    else:
        print("thats too bad. see you next time!")

coin_calc()
