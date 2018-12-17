import time
print("-" * 80)
print("Alien Greeter Bot:")

password = input("What planet are you from? ")
time.sleep(1)
if password.lower() == "mars":
	time.sleep(1)
	print("Welcome!")
	time.sleep(1)
	print("Please do not kill us")
else:
	print("Damnnnnnnnnn.")
	time.sleep(1)
	print("Your face was so ugly I thought you were an alien.")
	time.sleep(1)
	print("Anyway... have a good day")