BALANCE = 1000

def checkOperation():
   print("Which operation do you want to perform? \n1. Check Balance \n2. Deposit\n3. Withdraw\n4. Exit")
   Operation = int(input(" :"))

   if Operation !=1 and Operation !=2 and Operation != 3 and Operation != 4:
       print("Invalid operation. Please try again.")
       return checkOperation()
   else:
       return Operation    


def doDeposite():
    deposite= float (input("Enter the amount you want to deposite: "))
    newBalance = BALANCE + deposite
    print("Your new balance is : ", newBalance)
    return newBalance

def checkBalance():
    print("Your current balance is : ", BALANCE)

def doWithdraw():
    withdrawal = float(input("Enter the amount you want to withdraw: "))
    newBalance = BALANCE - withdrawal
    if newBalance < 0:
        print("Insufficient funds. Your current balance is : ", BALANCE)
        checkOperation()
    else:
        print("Your new balance is : ", newBalance)

    return newBalance




    
def main():

    print("Welcome!")
    userOperation = checkOperation()
    if userOperation == 4:
        print("Thank you for using our service!")
    else:
        if userOperation == 1:
            checkBalance()
        else:
            if userOperation == 2:
                doDeposite()
            else:
                doWithdraw()

    






main()
