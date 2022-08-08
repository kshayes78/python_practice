# for letter in "supercalifragilisticexpialidocious":
#     #Print all letters until it gets to letter "c" using break
#     if letter == "c":
#         break
#     print(letter)

# message = input("say hi:")
# #keep prompting infinitely (while True) until user enters the word "hi" , then stop and print "please say hi"
# while True:
#     if message == "hi":
#         break
#     message = input("please say hi:")
# print("Thank you for saying hi!")

for char in "FATCAT":
    #skip the letter "A" and print the other letters
    if char == "A":
        continue
    print(char)
#print after the loop is finished
print("After Loop")

for letter in "supercalifragilisticexpialidocious":
    #skip all of the vowels in the string
    if letter in "aeiou":
        continue
    print(letter)