# from os import system, name



# # import sleep to show output for some time period
# from time import sleep

# # define our clear function
# def clear():

#     # for windows
#     if name == 'nt':
#         _ = system('cls')

#     # for mac and linux(here, os.name is 'posix')
#     else:
#         _ = system('clear')

# # print out some text
# print('hello geeks\n'*10)

# # sleep for 2 seconds after printing output
# sleep(2)

# # now call function we defined above
# clear()

for x in range(1, 11):
    for y in range(1, 11):
        print('%d * %d = %d' % (x, y, x*y))
