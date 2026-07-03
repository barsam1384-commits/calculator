import random
import string

print("=== Password Generator Pro ===")

length = int(input("Enter password length: "))
count = int(input("How many passwords do you want? "))

print("\nChoose password type:")
print("1 - Letters only")
print("2 - Letters + Numbers")
print("3 - Strong (Letters + Numbers + Symbols)")

choice = input("Select (1/2/3): ")

if choice == "1":
    characters = string.ascii_letters
elif choice == "2":
    characters = string.ascii_letters + string.digits
elif choice == "3":
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice!")
    exit()

print("\nGenerated Passwords:\n")

for i in range(count):
    password = ""

    for j in range(length):
        password += random.choice(characters)

    print(f"{i+1}: {password}")