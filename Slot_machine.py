import random


#Global Constant and variables
MAX_LINES = 3
MAX_BET = 1000000
MIN_BET = 100

ROWS =3
COLS =3

symbol_count ={
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value ={
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


# NOTE: MAIN LOGIC - this how we are gonna generate the items that are going to be in our slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []  # this list here gives us every interior list gives us the value of the items inside of our columns      
    for _ in range(cols): # here _ = col because we don't need it here now
        column = []
        current_symbols = all_symbols[:] # making ta copy here and not affecting the main file
        for _ in range(rows): # here _ = row  because we don't it here now
            value = random.choice(current_symbols)  # this picks random values from the list
            current_symbols.remove(value) # removing the value from the list so it can't be picked again get rid of it.
            column.append(value)  # we add the value to our columns 

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()


# We wrote a functions for money deposit.
def deposit():
    while True:
        amount = input("What amount of money(₹) would you like to deposit? ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break 
            else: 
                print("Amount must be greater then 0.")
        else:
            print("Please enter the a valid amount of money.")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ") #method 1 to put variables in string
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break 
            else: 
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("What amount of money(₹) would you like to bet on each lines? ₹")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break 
            else: 
                print(f"Amount must be between ₹{MIN_BET} - ₹{MAX_BET}.") #method 2 to put variables in string USING "f" strings.
        else:
            print("Please enter the a valid amount of money.")

    return amount
    
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bets = bet * lines

        if total_bets > balance:
            print(f"You don't have enough money to bet that amount, Your current balance is: ₹{balance} ")
        else:
            break

    print(f"You are betting ₹{bet} on {lines} lines. Total bet is equal to: ₹{total_bets}.")

    # print(balance,lines)

    slots = get_slot_machine_spin(ROWS , COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ₹{winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bets


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ₹{balance}.")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
        
    print(f"You left with ₹{balance}")


main()
