money = 100
price = 10
print("You have "..money.." money")
print("You can buy a thing but it will cost you "..price.." money each")
print("How many do you buy?")

quantity = io.read()

money = money - price * quantity
print("You bought "..quantity.." things, it costed you "..price * quantity.." money")
print("You now have "..money.." money")