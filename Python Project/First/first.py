# # def greeting(name, age):
# #     print("welcome, " + name + " my age is " + str(age))
# #
# #
# # greeting("mike!", 18)
# #
# #
# # def print_seconds(hours, minutes, seconds):
# #     print((hours * 60 * 60) + (minutes * 60) + seconds)
# #
# #
# # print_seconds(1, 2, 3)
# #
# #
# # def convert_second(seconds):
# #     hours = seconds / 3600
# #     minutes = (seconds - hours * 3600) / 60
# #     remain_seconds = seconds - hours * 3600 - minutes * 60
# #     return hours, minutes, remain_seconds
# #
# #
# # hour, minute, second = convert_second(3661)
# # print(hour, minute, second)
#
# # 1) Complete the function to return the result of the conversion
# # def convert_distance(miles):
# # 	return (miles * 1.6)  # approximately 1.6 km in 1 mile
# #
# #
# # my_trip_miles = 55
# #
# # print(convert_distance(my_trip_miles))
# #
# # round_trip = convert_distance()
# # print("The round-trip in kilometers is " + str((convert_distance(my_trip_miles)/1.6))*2)
# #
# #
# # # 2) Convert my_trip_miles to kilometers by calling the function above
# # my_trip_km = 55
# #
# # # 3) Fill in the blank to print the result of the conversion
# # print("The distance in kilometers is " + ___)
# #
# # # 4) Calculate the round-trip in kilometers by doubling the result,
# # #    and fill in the blank to print the result
# # print("The round-trip in kilometers is " + ___)
#
# # def calculate_storage(filesize):
# #     block_size = 4096
# #     # Use floor division to calculate how many blocks are fully occupied
# #     full_blocks = filesize // block_size
# #     # Use the modulo operator to check whether there's any remainder
# #     partial_block_remainder = filesize % block_size
# #     # Depending on whether there's a remainder or not, return
# #     # the total number of bytes required to allocate enough blocks
# #     # to store your data.
# #     if partial_block_remainder > 0:
# #         return (full_blocks + 1) * block_size
# #     return full_blocks * block_size
# #
# # print(calculate_storage(1))    # Should be 4096
# # print(calculate_storage(4096)) # Should be 4096
# # print(calculate_storage(4097)) # Should be 8192
# # print(calculate_storage(6000)) # Should be 8192
# #
# # print("A dog" > "A mouse")
# # print(100*100)
# # print(9999+8888)
# #
# # print(26**6)
#
# # x = 0
# # while x < 5:
# #     print("HELLO " + str(x))
# #     x += 1
# #
# # print(x)
#
# # def attempts(n):
# #     x = 1
# #     while (x <= n):
# #         print("Attempt " + str(x))
# #         x += 1
# #         if x == 3:
# #             break
# #     print("Done")
# #
# # attempts(5)
#
# # def is_power_of_two(n):
# #   while n % 2 == 0:
# #       return True
# #   else
# #       return False
#
# # for x in range(0,100):
# #     if (x % 7 == 0):
# # print(str(x) + "\n")
#
# # count = 0
# # for i in range(10):
# #     for y in range(i):
# #         count += 1
# #         print(y, end=" ")
# #
# # print(count)
#
#
# # def votes(params):
# #     for vote in params:
# #         print("Possible option:" + vote)
# # votes(["yes", "no", "maybe"])
#
# old_email = "visa12333@laughing.com"
#
#
# # print(old_email.index("@"))
# # print(old_email[:9])
#
#
# # def replace_domain(email, olddomain, newdomain):
# #     if "@" + olddomain in email:
# #         index = old_email.index("@")
# #         newemail = email[:index] + "@" + newdomain
# #         return newemail
# #     return False
#
#
# # print(replace_domain(old_email, "laughing.com", "visa.com"))
#
#
# # def initials(phrase):
# #     words = phrase.split()
# #     result = ""
# #     for word in words:
# #         result += word[0]
# #     return result
# #
# #
# # def to_celsius(x):
# #     return (x - 32) * 5 / 9
#
#
# # for x in range(0,101,10):
# #     print("{:>3} F | {:>6.2f} C".format(x,to_celsius(x)))
#
# # word = "This is a lesson about lists"
# # lists = word.split()
# # lists.append("sas")
# # lists.remove("sas")
# #
# #
# # def skip_elements(elements):
# #     # code goes here
# #     new_list = []
# #     for index, item in enumerate(elements):
# #         if index % 2 == 0:
# #             new_list.append(elements[index])
# #             index += 1
# #     return new_list
#
#
# # print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
#
# # elements = ["a", "b", "c", "d", "e", "f", "g"]
# # new_list = []
# # for index, item in enumerate(elements):
# #     print(str(index) + " " + item)
# # print(initials("Universal Serial Bus"))  # Should be: USB
# # print(initials("local area network"))  # Should be: LAN
# # print(initials("Operating System"))  # Should be: OS
#
#
# # filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # newfilenames = []
# # for i in filenames:
# #     if "." + "hpp" in i:
# #         index = i.index(".")
# #         newstring = i[:index] + ".h"
# #         newfilenames.append(newstring)
# #     else:
# #         newfilenames.append(i)
# #
# #
# # def pig_latin(text):
# #     say = ""
# #     words = text.split()
# #     for word in words:
# #         # Create the pig latin word and add it to the list
# #         say += word[1:] + word[0] + "ay" + " "
# #         # Turn the list back into a phrase
# #     return say
# #
# #
# # def octal_to_string(octal):
# #     result = ""
# #     value_letters = [(4, "r"), (2, "w"), (1, "x")]
# #     # Iterate over each of the digits in octal
# #     for i in [int(n) for n in str(octal)]:
# #         # Check for each of the permissions values
# #         for value, letter in value_letters:
# #             if i >= value:
# #                 result += letter
# #                 i -= value
# #             else:
# #                 result += "-"
# #     return result
#
#
# # def group_list(group, user):
# #     s = group + ": "
# #     for i in range(len(user)):
# #         if i == len(user) - 1:
# #             s += user[i]
# #         else:
# #             s += user[i] + ", "
# #     return s
#
# # print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))
#
# # def guest_list(guests):
# #     for i in guests:
# #         name, age, profession = i
# #         print("{} is {} years old and works as {}. ".format(name,age,profession))
#
#
# # guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
# # print(octal_to_string(755))
# # value_letters = [(4,"r"),(2,"w"),(1,"x")]
# # for i in [int(n) for n in str(655)]:
# #     for value, letter in value_letters:
# #         for i >= value:
# #             print(i, letter)
# #
# # for value, letter in value_letters:
# #     print(value, letter)
#
# # def count_letters(text):
# #     result = {}
# #     for letter in text:
# #         if letter not in result and letter != " ":
# #             result[letter] = 0
# #             result[letter] += 1
# #
# #     return result
#
# # print(count_letters("a long string with a lot of letters"))
#
# # email_lists = {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"],"yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}
#
# # for i in email_lists:
# #     for j in email_lists[i]:
# #         print(j + "@" + i)
#
# # groups_list = {"local": ["admin", "userA"], "public":  ["admin", "userB"], "administrator": ["admin"] }
# # admin:[local,public,adminstration],
#
# # def groups_per_user(group_dictionary):
# #     user_groups = {}
# #     # Go through group_dictionary
# #     for :
# #         # Now go through the users in the group
# #         for ___:
# #
# #     return (user_groups)
# # user_groups = {}
# #
# # for i in groups_list: #i for local j for user
# #     for j in groups_list[i]:
# #         if j not in user_groups:
# #             user_groups[j] = [i]
# #         elif i not in user_groups[j]:
# #             user_groups[j].append(i)
# #
# # print(user_groups)
#
# # wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# # new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# # wardrobe.update(new_items)
# # print(wardrobe)
#
# # def format_address(address_string):
# #     house = ""
# #     street = ""
# #     s = address_string.split()
# #     for i,j in enumerate(s):
# #         if i == 0:
# #             house = s[i]
# #         else:
# #             street += s[i] + " "
# #     return house,street
# # print(format_address("123 Main Street"))
#
# # s = "Have a nice day"
# # s1 = "nice"
# #
# # def highlight_word(sentence, word):
# #     return sentence.replace(word,word.upper())
#
# # print(highlight_word("Have a nice day", "nice"))
#
# Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
#
# # def combine_lists(list1,list2):
# #     new_list = []
# #     for i in lists:
# #         new_list.append(i)
# #     list1.reverse()
# #     for j in list1:
# #         new_list.append(j)
# #     return new_list
#
# # def squares(start,end):
# #     return [i*i for i in range(start,end+1)]
#
# # print(squares(2,3))
#
# # def car_listing(car_prices):
# #   result = ""
# #   for i in car_prices:
# #     result += "{} costs {} dollars".format(i,car_prices[i]) + "\n"
# #   return result
# #
# # print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))
#
# def combine_guests(guests1, guests2):
#     guests2.update(guests1)
#     for i in guests2:
#         if i not in guests1:
#             guests1[i] = guests2[i]
#     return guests1
#
#
# Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
# Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
# print(combine_guests(Rorys_guests, Taylors_guests))
#
#
#
# # def count_letters(text):
# #   result = {}
# #   for i in text.lower():
# #     if i not in result and i.isalpha() and i != " ":
# #         result[i] = 0
# #         result[i] += 1
# #     elif i in result:
# #         result[i] += 1
# #   return result
#
#
# # print(count_letters("AaBbCc "))
# # print(count_letters("Math is fun 224"))
#
#
# # animal = "Hippopotamus"
# # print(animal[3:6])
# # print(animal[-5])
# # print(animal[10:])
# #
# # colors = ["red", "white", "blue"]
# # colors.insert(2, "yellow")
# # print(colors)
# #
# # host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
# #
# # print(host_addresses.values())

import binascii


file_hex = open('Lakhon_Sbek','r').read()
file_hex = binascii.a2b_hex(file_hex)
with open('image.png','w') as image_file:
    image_file.write(file_hex)