name = input("Please enter your name : ")
lastname = input("Please enter your last name : ")
while True:
    if type(name or lastname) != type(str):
        print("ur name wrong")
        exit()
    else:
        exit()

taxsim = 0.3
taxper = "30%"
income = int(input("Income per month :"))
cont = input(f"Hi! {name} {lastname} do you want to calculate your tax? (y/n)")
print(f"Your tax will be calculate from your income by ${taxper} ")
while True:
    if cont == "y":
        income = int(input("Income per month :"))
        print(f"Your tax will be calculate from your income by {taxper} and u need to pay ${income * taxsim}")
        cont = input(f"Hi! {name} {lastname} do you want to calculate your another tax of income? (y/n)")
    else:
        print("thank you for use tax calculatord ")
        break