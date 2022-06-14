def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):
    print(f"입금이 완료되었습니다. 잔액은 {balance+money}원입니다.")
    return balance + money


def withdraw(balance, money):  # 출금
    if balance >= money:
        print(f"출금이 완료되었습니다. 잔액은 {balance-money}원입니다.")
        return balance - money
    else:
        print(f"출금이 완료되지 않았습니다. 잔액은 {balance}원입니다.")
        return balance


def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 2000)
balance = withdraw(balance, 4000)
commission, balance = withdraw_night(balance, 500)
print(balance)
