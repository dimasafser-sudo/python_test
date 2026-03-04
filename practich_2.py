# Задание 1:
# s = "Python Programming"
# # words = s.split()
# # for word in words:
# #     print(word)


# Задание 2:
# s1 = input()
# cleaned_s1 = s1.replace(" ", "").lower()
# if cleaned_s1 == cleaned_s1[::-1]:
#     print("True")
# else:
#     print("False")


# Задание 3:
# s3 = input()
# result = ""
# for char in s3:
#     if char not in result:
#         result += char
# print(result)


# Задание 4:
# s4 = input("Введите строку: ")
# max_subs = ""
# for i in range(len(s4)):
#     curr_subs = ""
#     for j in range(i, len(s4)):
#         if s4[j] in curr_subs:
#             break
#         curr_subs += s4[j]

#     if len(curr_subs) > len(max_subs):
#         max_subs = curr_subs

# print(max_subs)


# Задание 5:
# s5 = input("Введите строку: ")
# zip_s5 = ""
# c = 1
# for i in range(1, len(s5)):
#     if s5[i] == s5[i - 1]:
#         c += 1
#     else:
#         zip_s5 += s5[i - 1] + str(c)
#         c = 1
# zip_s5 += s5[-1] + str(c)
# if len(zip_s5) < len(s5):
#     print(zip_s5)
# else:
#     print(s5)
