# password carching method - 0

import random
import hashlib
import pyttsx3
import os

engine = pyttsx3.init()

def speak(text):
	os.system(f"espeak { text }")

chars = '\'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890qwertyuiopasdfghjklzxcv"bnm_!@#$%^&*()-=+<>,./?}][{\|'
insta_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.-'
numbers = '1234567890'

chartype = input("Enter i for insta password: ")
if chartype == "i" or chartype == "I":
	allchars = list(insta_chars)
else:
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
			password = input("Enter a password: ")
			# while hit_password != password:
			# 	hit_password = random.choices(allnumbers, k=len(password))
			# 	print(">>>[" + ",".join(hit_password) + "]<<<")
			# 	if hit_password == list(password):
			# 		print("The Password is: " + "".join(hit_password))
			# 		speak("Password Cracked Successfully")
			# 		break
			for i in range(len(password)):
				hit_char = ""

				while hit_char != password[i]:
					hit_char = random.choice(allnumbers)
					print("Cracking character " + str(i+1) + " of " + str(len(password)) + ": " + hit_char)

				hit_password += hit_char

				if hit_password == password[:i+1]:
					i+=1
			print("The Password is: " + hit_password)
			speak("Password Cracked Successfully")


		except ValueError:
			print("Enter a valid password")
			speak("Enter Valid Password")
	elif type == "char" or type == "characters":
		i = 0
		password = input("Enter your password: ")
		# while (hit_password != password):
		# 	hit_password = random.choices(allchars, k=len(password))
		# 	print(">>>" + str(hit_password) + "<<<")
		# 	i+=1
		# 	print(i)
		# 	if (hit_password == list(password)):
		# 		print("The Password is: " + "".join(hit_password))
		# 		speak("Password Cracked Successfully")
		# 		break
		for i in range(len(password)):
				hit_char = ""

				while hit_char != password[i]:
					hit_char = random.choice(allchars)
					print("Cracking character " + str(i+1) + " of " + str(len(password)) + ": " + hit_char)

				hit_password += hit_char

				if hit_password == password[:i+1]:
					i+=1
		print("The Password is: " + hit_password)
		speak("Password Cracked Successfully")