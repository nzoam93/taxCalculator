# def numbers_of_letters(n):
#     str = ""
#     resultArr = []
#     lettersDict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
#     arr = str(n).split()
#     for ele1 in arr:
#         for ele2 in lettersDict:
#             if ele1 == ele2:
#                 str += lettersDict[ele2]
#                 resultArr << str
#     return resultArr

# print(numbers_of_letters(6))

n = 100
arr = list(str(n))
a2 = arr.replace('"','')
print(a2)
if arr[0] == "1":
    print("WOOHOO")
