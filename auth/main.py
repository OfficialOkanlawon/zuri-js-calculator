user = input('enter username \n')
allowedUsers = ['Toba', 'Oyin', 'Debby']
allowedPassword = ['toba', '0yin', 'debby']

if (user in allowedUsers): 
    password = input("Enter password \n")
    userid = allowedUsers.index(user)

    if (password == allowedPassword[userid]):
        print('Welcome ' + user + ' select an option')
        print('1. Withdrawal')
        print('2. Cash deposit')
        print('3. Cash Transfer')
        option = int(input("Pick an option \n"))
        balance = 10000
        if (option == 1):
            
            amount = int(input("How much do you want to withdraw? \n"))
            print("Are you sure you want to withdraw %s"  %amount)
            answer = input("Type yes to proceed and no to cancel \n")
            if(answer == 'yes'):
                if (amount > balance):
                    print("Transaction can't be completed your account balance is %s" %balance)
                else:
                    print("Transaction in Progress .....")
            elif (answer == 'no'):
                print("Ending Transaction ....")
        
        elif (option == 2):
            amount = int(input("How much do you want to deposit? \n"))
            print("Do you want to continue with the deposit of %s" %amount)
            answer = input("Type yes to proceed and no to cancel \n")
            if(answer == 'yes'):
                print("Transaction in progress ....")
                total = amount + balance
                print("Transaction completed your new account balance is now %s" %total)
            elif (answer == 'no'):
                print("Ending Transaction ....")
        
        elif (option == 3):
            amount = int(input("How much do you want to transfer? \n"))
            print("Do you want to continue with the deposit of %s" %amount)
            answer = input("Type yes to proceed and no to cancel \n")
            if(answer == 'yes'):
                if (amount > balance):
                    print("Transfer failed as your balance is insufficient to complete this transaction")
                else:
                    print("Transaction in progress ....")
                    total = balance - amount
                    print("Transaction completed your new account balance is now %s" %total)
            
            elif (answer == 'no'):
                print("Ending Transaction ....")

    else:
        print("Wrong password")

else:
    print('user not found')
