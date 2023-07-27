import os

bank_file = 'Bank Data.txt'
log_file = 'Transaction Log.txt'

def display_balance():
    with open(bank_file, 'r') as f:
        balance = float(f.readline())
        print('Your current balance is: {:.2f}'.format(balance))

def deposit(amount):
    with open(bank_file, 'r+') as f:
        balance = float(f.readline())
        f.seek(0)
        f.write(str(balance + amount) + '\n')
        f.truncate()

    with open(log_file, 'a') as f:
        f.write('Deposit: +{:.2f}\n'.format(amount))

def withdraw(amount):
    with open(bank_file, 'r+') as f:
        balance = float(f.readline())
        if balance < amount:
            print('Insufficient funds')
            return
        f.seek(0)
        f.write(str(balance - amount) + '\n')
        f.truncate()

    with open(log_file, 'a') as f:
        f.write('Withdrawal: -{:.2f}\n'.format(amount))

def is_valid_input(prompt, valid_responses):
    response = input(prompt)
    while response not in valid_responses:
        print('You provided an invalid input')
        response = input(prompt)
    return response

def is_valid_amount(prompt):
    amount = input(prompt)
    while not amount.isdigit():
        print('You provided an invalid input')
        amount = input(prompt)
    return float(amount)

def main():
    if not os.path.exists(bank_file):
        with open(bank_file, 'w') as f:
            f.write('0\n')

    display_balance()

    make_transaction = is_valid_input('Would you like to make a transaction? (Yes/No):\n', ['Yes', 'No'])

    while make_transaction == 'Yes':
        deposit_or_withdraw = is_valid_input('Would you like to make a deposit or withdrawal? (Deposit/Withdrawal):\n', ['Deposit', 'Withdrawal'])

        if deposit_or_withdraw == 'Deposit':
            amount = is_valid_amount('How much would you like to deposit?:\n')
            deposit(amount)
        else:
            amount = is_valid_amount('How much would you like to withdraw?:\n')
            withdraw(amount)

        display_balance()
        make_transaction = is_valid_input('Would you like to make another transaction? (Yes/No):\n', ['Yes', 'No'])

    print('Thank you for using our bank application!')

if __name__ == '__main__':
    main()
