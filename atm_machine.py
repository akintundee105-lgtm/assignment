balance = 5000000000000

print("=====ATM MACHINE=====")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice"))

if choice == 1:
    print("Your balance is Naira", balance)
elif choice == 2:
    amount = float(input("Enter amount to deposit: Naira"))
    balance += amount
    print("Deposit successful.")
    print("New balance: Naira", balance)
elif choice == 3:
    amount = float(input("Enter amount to withdraw: Naira"))

    if amount <= balance:
        balance -= amount
        print("Withdrawal successful.")
        print("Remaining balance: Naira", balance)
    else:
        print("Insuficient balance.")

elif choice == 4:
    print("Thank you for using our ATM.")
else: 
    print("Invalid choice.")