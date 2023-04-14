# password carching method - 0

import random
import hashlib
import pyttsx3

engine = pyttsx3.init()

def speak(text):
	print(text)
	engine.say(text)
	engine.runAndWait()
	engine.stop()

chars = '\'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890qwertyuiopasdfghjklzxcv"bnm_!@#$%^&*()-=+<>,./?}][{\|'
numbers = '1234567890'

allchars = list(chars)
allnumbers = list(numbers)

hashed = input("Hashed y/n: ")

if hashed == "y" or hashed == "Y" or hashed == "YES" or hashed ==  "yes":
	_password = input("Enter hashed password: ")
	enc = _password.encode('utf-8')
	hash_word = hashlib.md5(enc.strip())
	digest = hash_word.hexdigest()
	if digest == _password:
		print("Password: ", digest)
		speak("Password Cracked Successfully")
else:
	type = input("Enter type of password: ")

	hit_password =  ""

	if type == "number":
		try:
			password = int(input("Enter an password: "))
			while (hit_password != password):
				hit_password = random.choices(allnumbers, k=len(str(password)))
				print(">>>" + str(hit_password) + "<<<")
				if (hit_password == list(str(password))):
					print("The Password is: " + "".join(hit_password))
					speak("Password Cracked Successfully")
					break

		except ValueError:
			print("Enter a valid password")
			speak("Enter Valid Password")
	elif type == "char" or type == "characters":
		password = input("Enter your password: ")
		while (hit_password != password):
			hit_password = random.choices(allchars, k=len(password))
			print(">>>" + str(hit_password) + "<<<")
			if (hit_password == list(password)):
				print("The Password is: " + "".join(hit_password))
				speak("Password Cracked Successfully")
				break