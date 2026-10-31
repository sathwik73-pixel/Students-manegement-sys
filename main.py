expenses = []
total = 0
while True :
        print("1.Add expense:")
        print("2.show all expenses:")
        print("3.Highest expenses:")
        print("4.lowest expenses:")
        print("5.total amount:")
        print("6.exit")
        choice= int(input("enter your choice:"))
        if choice == 1:
                print("Add expense:")
                name = input("enter your expense name:")
                amount= float(input("enter amount of expense:"))
                total += amount
                expenses.append([name,amount])
                print("added successfully ")
        elif choice == 2:
                for expense in expenses:
                        print(expense[0],"=",expense[1])
        elif choice == 3:
                if len(expenses) == 0:
                        print("expeses are not added")
                else:
                        
                     largest = expenses[0] 
                     for x in expenses:
                             if x[1] > largest[1]:
                                      largest = x
                                
                     print("Highest expenses = ",largest [0], "=",largest [1])
        elif choice == 4:
                if len(expenses) == 0:
                        print("expenses are not added")
                else:
                        
                     lowest = expenses[0]
                     for x in expenses:
                             if x[1] < lowest[1]:
                                     lowest = x
                     print("lowest expenses = ",lowest[0], "=",lowest[1])
        elif choice == 5:
                print("Total amount:",total)
        elif choice == 6:
                print("Thanks!")
                break
        else:
            print("invalid choice")
                
                
        
                
