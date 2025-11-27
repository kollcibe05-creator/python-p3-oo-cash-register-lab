#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.total_list = []
        self.trasaction_history = []

    def add_item(self, item, price , quantity = 1):
        self.total += price * quantity
        transaction_cost = price * quantity
        self.trasaction_history.append({
            "item": item,
            "quantity": quantity,
            "cost": transaction_cost
        })
        for i in range (1, quantity + 1):
            self.items.append(item) 
            self.total_list.append(price)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = self.total * (100 - self.discount )/100 
            print(f"After the discount, the total comes to ${int(self.total)}.") 
    def void_last_transaction(self):
        # removed_transaction = self.total_list.pop()
        # self.items.pop()
        # self.total -= removed_transaction
        removed_last_transaction = self.trasaction_history.pop()
        last_transaction_cost = removed_last_transaction["cost"]
        self.total -= last_transaction_cost
        # return sum(self.total_list)
        # return (self.total_list[-1])
        
                  


    pass


# for i in range (1, 3+1):
#     print("yeah")