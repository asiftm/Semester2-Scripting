def add_percentage(price, percentage=15):
    total = price + (price*(percentage/100))
    return(total)

def add_tip(price):
    tip_input = input('How much tip would you like to give? ')
    while not tip_input.isdigit():
        tip_input = input('How much tip would you like to give? ')
    total = price + (price*(int(tip_input)/100))
    return total

def calulations(sum):
    price_with_tax = add_percentage(sum)
    price_with_tip = add_tip(price_with_tax)
    round_price = round(price_with_tip,2)
    return(round_price)

def main():
    manu_and_prices_list = ['1. Habbeer ($3.50)','2. Wine ($4.00)','3. Java Coffee ($2.50)','4. Apple Juice ($6.00)','5. Root Access Beer ($1.75)']
    for i in manu_and_prices_list:
        print(i)
    price_list = []
    for item in manu_and_prices_list:
        price_str = item.split("$")[1].split(")")[0]
        price_list.append(price_str)
    order = input('Please write down your order: ')
    if order.isnumeric():
        sum=0
        for i in order:
            sum=sum+float(price_list[int(i)-1])
        round_price=calulations(sum)
        print(f'Total price: ${round_price}')
    else:
        print(f'Total price: $0.0')
        exit()

if __name__ == "__main__":
    main()


