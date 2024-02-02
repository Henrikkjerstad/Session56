name=input("Whats your name?")
age=input("How old are you?")
# print("Hello,", name, "!", sep="")
age = int(age) # Convert string to integer
birth_year = 2024 - age
print(name, ", you were born in ", birth_year, ".", sep="")
