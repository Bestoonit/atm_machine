#ATM machine python code
class Atm:
    def __init__(self, withdrawal, insert, balance):
        self.withdrawal = withdrawal
        self.insert = insert
        self.balance = balance

    def balance_(self):
        print('Your balance now is: {}'.format(self.balance))

    def insert_(self):
        insert = int(input("How much money you want to insert: "))
        self.balance = insert + self.balance
        print('Your balance now is: {}'.format(self.balance))

    def withdrawal_(self):
        withdrawal = int(input("How much money you want to take out: "))
        self.balance = self.balance - withdrawal
        print('Your balance now is: {}'.format(self.balance))

atm = Atm(0, 0, 0)

def main():
    choice = [1, 2, 3, 4]
    while True:
        print("\nSelect an option: \n")
        print("1- Show balance")
        print("2- Insert money")
        print("3- Take out money")
        print("4- Cancel ")
        try:
            val = int(input(": "))
            if val == 1:
                atm.balance_()
            elif val == 2:
                atm.insert_()
            elif val == 3:
                atm.withdrawal_()
            elif val == 4:
                break
            elif val not in choice:
                print("Choose a number between 1, 2, 3, 4 as an option. ")
                main()

        except ValueError:
            print("Choose a number between 1, 2, 3, 4 as an option. ")
            main()

if __name__ == "__main__":
    main()

