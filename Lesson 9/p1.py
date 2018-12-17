import time
print("-" * 80)
print("Locker Bot:")

password = input("What is your password: ")
tries = 0
if password.lower() == "open sesame":
	time.sleep(1)
	print("Valid Password")
	time.sleep(1)
	print("Access Granted")
else:
	print("Access Denied")
	time.sleep(1)
	print(". . .")
	time.sleep(1)
	print("Please try again")
while password.lower() != "open sesame" and tries < 2:
		password = input("What is your password: ")
		tries = tries + 1
		if tries >= 2:
			time.sleep(1)
			print("Out of tries.")
			print(" ")
			time.sleep(1)
			print("Come back later.")
		else:
			if password.lower() == "open sesame":
				time.sleep(1)
				print(" ")
				print("Valid Password")
				print(" ")
				time.sleep(1)
				print("Access Granted")
			else:
				print("Access Denied")
				time.sleep(1)
				print(". . .")
				time.sleep(1)
				print("Please try again")
