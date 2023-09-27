# 1․ Գրել ֆունկցիա, որը․
#    - տրված բառերի list-ը կֆիլտրի այնպես, որ կթողի միայն ամենաերկար բառերը
#      (այսինքն՝ կգտնի ամենաերկար բառի երկարությունը և լիստում կթողնի միայն այդ երկարության բառերը),
#    օրինակ՝ input = ["aba", "aa", "z", "ad", "vcd", "aba"]
#            output = ["aba", "vcd", "aba"],
           
#            input = ["aba", "aa", "z", "advc", "vcd", "aba"]
#            output = ["advc"],
#    - վերջում գնահատեք Ձեր գրած կոդը Big O notation-ի միջոցով։

# def longest_str(inputArray):
#     list1 = [inputArray[0]]
#     for i in inputArray[1:]:
#         if len(i) > len(list1[0]):
#             list1.clear()
#             list1.append(i)
#         elif len(i) == len(list1[0]):
#             list1.append(i)
#     return list1

# Big O = O(len(array))

# 2․ Գրել ֆունկցիա, որը․
#    - կհաշվի, թե տրված ամբողջ թվերի list-ից քանի քայլով կարելի է ստանալ մոնոտոն աճող թվերից բաղկացած list,
#      մեկ քայլի ընթացքում թույլատրվում է թվերից մեկը մեկով մեծացնել, թվերի տեղերը փոխել չի կարելի, 
#    օրինակ՝ [-10, 0, -2, 0] -> 5,
#            [1, 1, 1] -> 3:

# def monotone_func(array: list) -> int:
#     sum = 0
#     for i in range(1, len(array)):
#         if array[i] <= array[i - 1]:
#             a = ((array[i - 1]) - array[i] + 1)
#             sum += a
#             array[i] = array[i] + a
#     return sum
# print(monotone_func([-10, 0, -2, 0]))

# 3. Գրել ֆունկցիա, որը․
#    - կստանա երկու արգումենտ՝ a և b,
#    - կվերադարձնի a-ի b աստիճանի ամենավերջի թվանշանը,
#    փորձել խնդիրը լուծել այնպես, որ կոդը աշխատի շատ արագ՝ նույնիսկ շատ մեծ թվերի դեպքում։

# def exponent_func(a: int, b: int):
#     if a % 10 == 0:
#         return 0
#     elif a % 10 == 1:
#         return 1
#     else: 
#         return ((a % 10) ** (b % 10)) % 10
# print(exponent_func(156, 52))


# 4 Ceaser cipher

# encoding
# import string
# def encode_ceaser(text: str) -> str:
#     text_encoded = ''
#     d = {'w': 'a',
#          'x': 'b',
#          'y': 'c',
#          'z': 'd'}
#     for i in text:
#         if (i.lower()) in d.keys():
#             text_encoded += d[(i.lower())]
#         elif i in string.punctuation or i == ' ':
#             text_encoded += i
#         else:
#             text_encoded += string.ascii_lowercase[(string.ascii_lowercase.index(i.lower()) + 3)]
#     return text_encoded

# print(encode_ceaser('Hello World'))


# decoding
# def decode_ceaser(text: str) -> str:
#     text_decoded = ''
#     d = {'a': 'w',
#          'b': 'x',
#          'c': 'y',
#          'd': 'z'}
#     for i in text:
#         if (i.lower()) in d.keys():
#             text_decoded += d[(i.lower())]
#         elif i in string.punctuation or i == ' ':
#             text_decoded += i
#         else:
#             text_decoded += string.ascii_lowercase[(string.ascii_lowercase.index(i.lower()) - 3)]
#     return text_decoded

# print(decode_ceaser('khoor aruog'))

