# from numpy import numpy
import random

MAX_LINES=3
MAX_DEPOSIT=1000
MIN_DEPOSIT=1

rows = 3
cols=3
symbols={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbols_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}


def deposit():
    while True:
        amount = input("Enter the amount ? $")

        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                 break
            else:
                print("enter the amount greater than 0")
        else:
            print("enter the amount in numbers dont fuck with me")
    return amount


def check_winning(columns,lines,bet,values):
     winnings=0
     winning_lines=[]
     for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] *bet
            winning_lines.append(line+1)
     
     return winnings,winning_lines

def get_lines():
    while True:
        lines = input("Enter the amount of lines you wanna bet? ")
        if lines.isdigit():
            lines = int(lines)
            if 0<=lines<=MAX_LINES:
                break
            else:
                print("enter the lines between 0 to {MAX_LINES}")
        else:
            print("Enter the lines in digits")

    return lines

def get_bet():
    while True:
        bet= input("Enter the total amount of bet? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_DEPOSIT<=bet<=MAX_DEPOSIT:
                break
            else:
                print(f"enter the AMOUNT between ${MIN_DEPOSIT} to ${MAX_DEPOSIT}")
        else:
            print("Enter the bet in digits")
    return bet

def get_slot_machine_spin(rows,cols,symbols ):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
            
# columns = get_slot_machine_spin()

def print_slot(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)- 1:
                print(column[row], end=" | ")
            else:
                print(column[row])
        print()

def game(amount):
    lines = get_lines()
    bet = get_bet()
    total_bet  = lines*bet 

    while True:
        if total_bet>amount:
            print(f"you do not have enough amount to bet")
            break
        else:
            break
    
    
    slots = get_slot_machine_spin(rows,cols,symbols)
    print_slot(slots)
    winnings,winning_lines = check_winning(slots,lines,bet,symbols_value)
    print(f"you won {winnings}")
    print(f"you won on lines :",*winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while balance>0:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance+=game(balance)



 
main()



