money = 50

def update_money():
	global money
	money = 3

update_money()

print(money) # now it's 3 because we modified the global money

