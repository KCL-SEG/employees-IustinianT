"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Contract:
    def __init__(self, type, amount):
        self.type = type.lower()
        self.amount = amount

    def get_type(self):
        return self.type

    def get_amount(self):
        return self.amount
class Employee:
    def __init__(self, name, contract, hours, contracts, bonus):
        self.name = name
        self.contract = contract
        self.hours_worked = hours
        self.contracts = contracts
        self.bonus = bonus
        self.pay_string = ""

    def get_pay(self):
        self.pay_string = f"^{self.name} works on a "
        total_pay = 0
        if self.contract.get_type() == "hourly":
            total_pay += self.contract.get_amount()*self.hours_worked
            self.pay_string += f"contract of {self.hours_worked} hours at {self.contract.get_amount()}/hour"
        elif self.contract.get_type() == "monthly":
            total_pay += self.contract.get_amount()
            self.pay_string += f"monthly salary of {self.contract.get_amount()}"
        if self.contracts:
            total_pay += self.contracts[0]*self.contracts[1]
            self.pay_string += f" and receives a commission for {self.contracts[0]} contract(s) at {self.contracts[1]}/contract"
        if self.bonus:
            total_pay += self.bonus
            self.pay_string += f" and receives a bonus commission of {self.bonus}"

        self.pay_string += f".\s+Their total pay is {total_pay}.$"

        return total_pay

    def __str__(self):
        # to generate pay_string
        self.get_pay()
        return self.pay_string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Contract("monthly", 4000), hours=False, contracts=False, bonus=False)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', Contract("hourly", 25), hours=100, contracts=False, bonus=False)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', Contract("monthly", 3000), hours=False, contracts=(4, 200), bonus=False)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', Contract("hourly", 25), hours=150, contracts=(3, 220), bonus=False)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', Contract("monthly", 2000), hours=False, contracts=False, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', Contract("hourly", 30), hours=120, contracts=False, bonus=600)