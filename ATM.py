bal=2000
password='1234'
chance=3
while chance>0:
    code=input("enter password")
    if code == password:

            print("check bal")
            print("withdraw")
            print("statement")
            print("credit cards")
            option=input("enter the options")
        if option == "1":
         print("your bal is:",bal)

        if option == "2":
            withdraw=int(input("enter amount"))
            bal=bal-withdraw
            print("amount withdraw:", withdraw)
            break

    else:
     chance -='1'
     if chance==0:
        print("Acc Blocked")

#isinstance(bal,float)
#raise AssertionError("only INT allowed")
