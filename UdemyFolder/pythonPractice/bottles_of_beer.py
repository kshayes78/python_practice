#using a for loop for each number within the range of 99-0
# for num in range (99, 0, -1):
#     print(f"{num} bottles of beer on the wall.")
#     print(f"{num} bottles of beer.")
#     if num == 1:
#         print(f"Take one down and pass it around, no more bottles of beer on the wall.")
#     else:
#      print(f"Take one down and pass it around {num - 1} bottles of beer on the wall.")
#     print("*" * 50)

#set num variable to 99, while num > 0, print messages, decrement by 1
num = 99
while num > 0:
   print(f"{num} bottles of beer on the wall.")
   print(f"{num} bottles of beer.")
   if num == 1:
        print(f"Take one down and pass it around, no more bottles of beer on the wall.")
   else:
     print(f"Take one down and pass it around {num - 1} bottles of beer on the wall.")
   print("*" * 50)
   num -= 1
   