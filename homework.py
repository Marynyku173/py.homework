# import os, re


# def phone_format(n):  
#     n = n.removeprefix("+")
#     n = re.sub("[ ()-]", "", n)
#     return format(int(n[:-1]), ",").replace(",", "-") + n[-1]


# def printData(data):  
#     phoneBook = []
#     splitLine = "=" * 49
#     print(splitLine)
#     print(" №  Lastname        Name          Phone Numbers")
#     print(splitLine)
#     personID = 1

#     for contact in data:
#         lastName, name, phone = contact.rstrip().split(",")
#         phoneBook.append(
#             {
#                 "ID": personID,
#                 "lastName": lastName,
#                 "name": name,
#                 "phone": phone_format(phone),
#             }
#         )
#         personID += 1

#     for contact in phoneBook:
#         personID, lastName, name, phone = contact.values()
#         print(f"{personID:>2}. {lastName:<15} {name:<10} -- {phone:<15}")

#     print(splitLine)


# def showContacts(fileName):  
#     os.system("cls")
#     phoneBook = []
#     with open(fileName, "r", encoding="UTF-8") as file:
#         data = sorted(file.readlines())
#         printData(data)
#     input("\n--- press any key ---")


# def addContact(fileName):  
#     os.system("cls")
#     with open(fileName, "a", encoding="UTF-8") as file:
#         res = ""
#         res += input("Input a Surname of Contact: ") + ","
#         res += input("Input a Name of Contact: ") + ","
#         res += input("Input a Phone Number of Contact: ")

#         file.write(res + "\n")

#     input("\nContact was successfully added!\n--- press any key ---")


# def findContact(fileName):  
#     os.system("cls")
#     target = input("Input item of contact for searching: ")
#     result = []
#     with open(fileName, "r", encoding="UTF-8") as file:
#         data = file.readlines()
#         for person in data:
#             if target in person:
#                 result.append(person)
#                 # break

#     if len(result) != 0:
#         printData(result)
#     else:
#         print(f"There is no contact with this item '{target}'.")

#     input("--- press any key ---")


# def changeContact(fileName):  
#     os.system("cls")
#     phoneBook = []
#     with open(fileName, "r", encoding="UTF-8") as file:
#         data = sorted(file.readlines())
#         printData(data)

#         numberContact = int(
#             input("Input number of contact for changing or 0 for return main menu: ")
#         )
#         print(data[numberContact - 1].rstrip().split(","))
#         if numberContact != 0:
#             newLastName = input("Input new Lastname: ")
#             newName = input("Input new Name: ")
#             newPhone = input("Input new Phone: ")
#             data[numberContact - 1] = (
#                 newLastName + "," + newName + "," + newPhone + "\n"
#             )
#             with open(fileName, "w", encoding="UTF-8") as file:
#                 file.write("".join(data))
#                 print("\nContact was successfully changed!")
#                 input("\n--- press any key ---")
#         else:
#             return


# def deleteContact(fileName):  
#     os.system("cls")
#     with open(fileName, "r+", encoding="UTF-8") as file:
#         data = sorted(file.readlines())
#         printData(data)

#         numberContact = int(
#             input("Input number of contact for deleting or 0 for return main menu: ")
#         )
#         if numberContact != 0:
#             print(f"Deleting record: {data[numberContact-1].rstrip().split(',')}\n")
#             data.pop(numberContact - 1)
#             with open(fileName, "w", encoding="UTF-8") as file:
#                 file.write("".join(data))

#         else:
#             return

#     input("--- press any key ---")


# def drawInterface():  
#     print("#####   PHONE BOOK   #####")
#     print("=" * 26)
#     print(" 1 -- Show contacts")
#     print(" 2 -- Add contacts")
#     print(" 3 -- Find contacts")
#     print(" 4 -- Change contacts")
#     print(" 5 -- Delete contacts")
#     print("\n 0 -- Exit")
#     print("=" * 26)


# def main(file_name):  
#     while True:
#         os.system("cls")
#         drawInterface()
#         userChoice = int(input("Input a number for 1 to 5 or 0 for exit: "))

#         if userChoice == 1:
#             showContacts(file_name)
#         elif userChoice == 2:
#             addContact(file_name)
#         elif userChoice == 3:
#             findContact(file_name)
#         elif userChoice == 4:
#             changeContact(file_name)
#         elif userChoice == 5:
#             deleteContact(file_name)
#         elif userChoice == 0:
#             print("Thank you!")
#             return


# path = "phonebook.txt"

# main(path)


