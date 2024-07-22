"""
Progettare un semplice sistema bancario con i seguenti requisiti:

Classe del Account:
Attributi:
account_id: str - identificatore univoco per l'account.
balance: float - il saldo attuale del conto.
Metodi:
deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
get_balance(): restituisce il saldo corrente del conto.
Classe Bank:
Attributi:
accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
Metodi:
create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
"""

class Account:

    def __init__(self, account_id: str, balance: float) -> None:
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount: float):
        self.balance+=amount
        return self.balance
    
    def get_balance(self):
        if self.balance != 0:
            return self.balance
        else:
            return 0
    
class Bank:

    def __init__(self) -> None:
        self.accounts: dict[str, Account] = {}
    
    def create_account(self, account_id): 
        if account_id not in self.accounts.keys():
            self.accounts[account_id]= Account(account_id, 0)
            return self.accounts[account_id]
    
    def deposit(self, account_id, amount):
        self.accounts[account_id].deposit(amount)

    def get_balance(self, account_id):
        return self.accounts[account_id].balance

class2


	
bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())


bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))

bank = Bank()
account2 = bank.create_account("456")
bank.deposit("456",200)
print(bank.get_balance("456"))



"""
Progettare un semplice sistema bancario con i seguenti requisiti:

    Classe del Account:
        Attributi:
            account_id: str - identificatore univoco per l'account.
            balance: float - il saldo attuale del conto.
        Metodi:
            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
            get_balance(): restituisce il saldo corrente del conto.
    Classe Bank:
        Attributi:
            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        Metodi:
            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
            get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
"""


class Account:

    def __init__(self, account_id: str, balance: float) -> None:
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount: float):

        if amount!= 0:
            self.balance+=amount
        
    def get_balance(self):
        if self.balance != 0:
            return self.balance
        else: 
            return 0
    
class Bank:

    def __init__(self) -> None:
        self.accounts: dict[str, Account] = {}

    def create_account(self, account_id):
        if account_id not in self.accounts.keys():
            self.accounts[account_id]=Account(account_id, 0)
            return self.accounts[account_id]
        elif account_id in self.accounts.keys():
            print ("Account with this ID already exists")
    
    def deposit(self, account_id, amount):
        if account_id in self.accounts.keys():
            self.accounts[account_id].deposit(amount)
        else:
            print("Account not found")
    
    def get_balance(self, account_id):
        if account_id in self.accounts.keys():
            return self.accounts[account_id].get_balance()
        else:
            print ("Account not found")






    


