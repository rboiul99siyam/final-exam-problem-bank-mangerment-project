class User:
    accounts = []

    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        User.accounts.append(self)
        self.transactions = []
        self.loan = 0


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(amount)
        else:
            print("\n\n\tsorry, invalid \n")


    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(amount)
        else:
            print("\n\n\tWithdrawal amount exceeded”!!!")



    def transaction_history(self):
        print(f"\n\n\tDeposit money , Withdraw , loan : {self.transactions} ")



    def available_balance(self):
        print(f"\n\n\tavailable balance: {self.balance}")

  
  
    def bank_loan(self, amount):
        if amount > 0 and amount <= self.balance and self.loan < 2:
            self.loan += 1
            self.balance += amount
            self.transactions.append(amount)
        else:
            print("\n\tSir ,You have taken loan twice !!")



    def transfer(self, r_name, amount):
        sender = None
        for user in User.accounts:
            if user.name == r_name:
                sender = user
                break
        
        if sender is not None and amount <=self.balance:
            self.balance -= amount
            sender.balance +=amount
            self.transactions.append(f'transfer :{amount} to {sender.name}')
            sender.transactions.append(f'accepect : {amount} from {self.name}')
        else:
            print("\n\n\tDon,t match !!")

       


class Admin(User):


    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address, account_type)
        self.users = []
        self.total_balance = 0
        self.loan_running = True



    def create_account(self, name, address, email, account_type):
        user = User(name, email, address, account_type)
        self.users.append(user)




    def delete_account(self, user):
        if user in self.users:
            self.users.remove(user)
            print("\n\n\tRemoved account successfully !!!")


    def list_account_show(self):
        for user in self.users:
            print(f"Name: {user.name}, Address: {user.address}, Email: {user.email}, Account Type: {user.account_type}")



    def total_available_balance(self):
        total_balance = sum(user.balance for user in User.accounts)
        print(f"Total available balance: {total_balance}")


    def total_loan_balance(self):
        total_loan = sum(user.loan for user in User.accounts)
        print(f"Total loan balance: {total_loan}")
 
    
    def loan_f(self, d):
        if d == 'running':
            self.loan_running = True
            print("\n\n\tLoan is running!!")
        elif d == 'closed':
            self.loan_running = False
            print("\n\n\tLoan is closed.")
        else:
            print("\n\n\tInvalid status! Use 'running' or 'closed'.")





user = Admin('admin', 'admin@gmail.com', 'admin_address', 'admin_account_type')



current_user = None  
changeUser = True

while True:
    if current_user is None:
        print("\n\tNo login user !")
        ch = input("\n\nLogin or Register (L/R): ")
        if ch == 'L':

            em = input("email : ")           
            ac_type = input("account type : ")
            flag = False
            for u in user.accounts:
                if u.email == em:
                    flag = True
                    current_user = u
                    break
            
            if flag == False:
                print("\n\n\tUser Not found !!")

        elif ch == 'R':
            name = input("Name : ")
            em = input("email : ")
            ad = input("address : ")
            ac_type = input("account type : ")
            ac = User(name,em,ad,ac_type)
            current_user = ac
            changeUser = True
            
        else:
            print("\n\tPlease enter 'L' for login or 'R' for registration.")
    else:
        print("\n------------------------------------>")
        print(f"\n\tWelcome to {current_user.name}")
        print("------------------------------------->")

        if current_user.name == 'admin':
            print("1.create account ")
            print("2.delete account ")
            print("3.all user list ")
            print("4.total avaliable balance ")
            print("5.total loan balance ")
            print('6.loan (closed / running) ')
            print('7.logout ')

            oh = int(input("\n\noh ,sure choice your option : "))
            if oh == 1:
                name = input('Name : ')
                ad = input("address : ")
                em = input("Email : ")
                ac_type = input("account type : ")
                user.create_account(name,ad,em,ac_type)
            
            
            elif oh == 2:
                name = input("Name : ")
                for u in user.users:
                    if u.name == name:
                        user.delete_account(u)
                        break
            elif oh == 3:
                user.list_account_show()
            elif oh == 4:
                user.total_available_balance()
            elif oh == 5:
                user.total_loan_balance()
            elif oh == 6:
                d = input("loan (closed/running)")
                user.loan_f(d)
            elif oh == 7:
                current_user=None
            else:
                print("\n\n\tsorry Invalid number !!")
        else:
            print("1.Deposit ")
            print("2.Withdraw ")
            print("3.Bank loan")
            print("4.Transation ")
            print("5.Avaliable Balance ")
            print("6.Trnasfar balance ")
            print("7.Logout ")

            oh = int(input("\nEnter choice a option : "))
            if oh == 1:
                am = int(input("amount : "))
                current_user.deposit(am)
                print("\n\n\tcurrent balance : ",current_user.balance)
            elif oh == 2:
                am = int(input("amount : "))
                current_user.withdraw(am)
                print("\n\n\tcurrent balance : ",current_user.balance)
            elif oh == 3:
                am = int(input("amount : "))
                current_user.bank_loan(am)
                print("\n\n\tcurrent balance : ",current_user.balance)

            elif oh == 4:
                current_user.transaction_history()
            elif oh == 5:
                current_user.available_balance()
            elif oh == 6:
                r_name = input("revier name : ")
                am = int(input("Amount  : "))
                current_user.transfer(r_name,am) 
                print("\n\n\tTransfer Successfully !!")   
            elif oh == 7:
                current_user = None
            else:
                print("\n\n\tsorry Invalid number !!")

    