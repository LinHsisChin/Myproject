import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

# mathScores = [60, 70, 10, 20, 81, 63, 4]
#
# mathScores[2]
#
# print(mathScores[2])
#
# print(mathScores[1:6])
# print(mathScores[-1])
# print(mathScores[5:])
#
# print(sum(mathScores))
# print(max(mathScores))
# print(min(mathScores))
# print(sum(mathScores) / len(mathScores))
#
# mathScores2 = []
# print(mathScores2)
# mathScores2.append(60)
# print(mathScores2)
# mathScores2.append(70)
# mathScores2.append(50)
# mathScores2.append(40)
# mathScores2.insert(2, 30)
# print(mathScores2)
#
# mathScores2[1] = 55
# print(mathScores2)
#
# mathScores2.append(70)
# mathScores2.append(40)
# print(mathScores2)
# print(mathScores2.count(40))
# print(mathScores2.index(40))
#
# print(mathScores)
# print(mathScores2)
# print(sorted(mathScores2, reverse=True))
#
# ls = [[1, 2, 3], [4, 5, 6]]
# print(ls[0][2])
#
# grades = []
# grades = [[5, 14, 7], [23, 36, 28], [88, 80, 92]]
# print(grades[2])
# print(sum(grades[0]) / len(grades[0]))
# print(sum(grades[1]) / len(grades[1]))
# print(sum(grades[2]) / len(grades[2]))
# grades.append([94, 90, 96])
# print(grades)
#
# grades[0][1] = 20
# print(grades[0])
#
# gradesTuple = ([5, 14, 7], [23, 36, 28], [88, 80, 92])
#
# print(gradesTuple[2])
# print(sum(gradesTuple[0]) / len(gradesTuple[0]), sum(gradesTuple[1]) / len(gradesTuple[1]),
#       sum(gradesTuple[2]) / len(gradesTuple[2]))
#
# family = {
#     "dad": "Homer",
#     "mom": "Marge",
#     "sos": "Bart",
#     "daghter": "Lisa"
# }
# print(family["dad"])
# print(family.get("dog"))
#
# print("dad" in family)
#
# print(family.keys())
# print(family.values())
# print(family.items())
# print(family)
#
# family2 = {}
# print(family2)
# family2["cousin"] = "Max"
# print(family2)
# family2.update({
#     "uncle": "Martin",
#     "aunt": "May"
# })
# print(family2)
#
# del family2["uncle"]
# print(family2)
# family2.pop("cousin")
# print(family2)
#
# gradesDict = {
#     "chinese": [5, 14, 7],
#     "english": [23, 36, 28],
#     "math": [88, 80, 92]
# }
# print(gradesDict.get("math"))
# print(sum(gradesDict["chinese"]) / len(gradesDict["chinese"]))
# print(sum(gradesDict["english"]) / len(gradesDict["english"]))
#
# gradesDict.update({
#     "science": [94, 90, 96]
# })
# print(gradesDict)
#
# allStudents = {"John", "Eva", "Jill", "Eric", "Andy",
#                "Albert", "Polina", "Kristin ", "Angela"}
# guitarClub = {"John", "Eva", "Jill", "Eric", "Andy"}
# danceClub = {"Andy", "Eric", "Albert", "Polina", "Kristin "}
#
# print(danceClub & guitarClub)
# print(guitarClub - danceClub)
# both = guitarClub | danceClub
# print(allStudents - both)


# import math
# print(math.sqrt(5.8))
#
# r = 3
# pi = 3.14
# area = r ** 2 * pi
# print(area)
#
# scores = [10, 30, 40, 90, 100, 61]
# average = sum(scores) / len(scores)
# print(average)
#
# average = round(average)
# print(average)

# score = 70
#
# if score >= 60:
#     print("及格了")
#     if score >= 90:
#         print("你真棒")
#     else:
#         print("ok!!")
# elif 55 <= score and score <= 60:
#     print("教授拜託給我過")
# elif 50 <= score < 55:
#     print("教授你行行好")
# else:
#     print("被當了")

# print("Hello" , "world" , "!")
# print("Hello \nworld \n!")
# print("123" , end=" ")
# print("456")
#
# x = 42
# print(f"value of x is {x}")


# mathScores = [60, 70, 10, 20, 81, 63, 4]
# print(mathScores[0])
# firstItem =f"first item in mathScores is {mathScores[0]}"
# print(firstItem)
# print(f"the mathSocres has  {len(mathScores)} items")

# for i in range(len(mathScores)):
#     print(i, mathScores[i])
#
# for i in mathScores:
#     print(i)
#
# family = {
#     "dad": "Homer",
#     "mom": "Marge",
#     "son": "Bart",
#     "daughter": "Lisa"
# }
# for member in family.items():
#     print(member)
#
# for key, value in family.items():
#     print(f"my {key} is {value}")

# import math
# mathScores = [60, 70, 10, 20, 81, 63, 4]
#
# for i in mathScores:
#     print(i**0.5*10)
# for score in mathScores:
#     print(math.sqrt(score)*10)
# for i in range(10):
#     print(i)
# [print(i) for i in range(10)]
# import math
# mathScores = [60, 70, 10, 20, 81, 63, 4]
# [print(math.sqrt(x)*10) for x in mathScores]
# count = 0
# while count <10:
#     print(count)
#     count += 1
# else:
#     print("loop end")
# mathScores = [60, 70, 10, 20, 81, 63, 4]
#
# for score in mathScores:
#     if score > 80:
#         continue
#     print(score)
# import random
# i = random.randint(1, 50)
# print(i)
#
# x = eval(input("How many rows:"))
# print(type(x))
# count = 0
# while count <= 50:
#     print("你好", end="")
#     count +=1
# else:
#     print("我說完拉")
# import random
# row = random.randint(0,100)
# columns = random.randint(0,100)


# weight =  100
# weight1 = 80
#
# def add_weight(w1, w2=1):
#     result = w1 + w2
#     result1 = w1/w2
#     return result, result1
#
# x1, x2 = add_weight(weight, weight1)
# print(x1, x2)
#
# y1, y2 = add_weight(w2=weight, w1=weight1)
# print(y1, y2)
#
#
#
# def add(x, y):
#     """
#     數字相加
#     :param x: 數字1
#     :param y: 數字2
#     :return: 相加結果
#     """
#     return x + y


# def foo(num:int) -> str:
#     """
#     function foo
#     :param num:int number
#     :return: string
#     """
#     print(num)
#     return '回傳值'
#
# print(foo())




class Pokemon:
    def __init__(self, new_name, new_weight, name_height, new_food, new_cp):
        self.__name = new_name
        self.__weight = new_weight
        self.__height = name_height
        self.__food = new_food
        self.__cp = new_cp
    def eat(self):
        print(f'The pokemon is eating {self.__food}.')
    def make_noice(self):
        print("The pokemon wow wow wow")

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_weight(self):
        return self.__weight

    def set_weight(self, new_weight):
        self.__weight = new_weight

    def get_height(self):
        return self.__height

    def set_height(self, new_height):
        self.__height = new_height

    def get_food(self):
        return self.__food

    def set_food(self, new_food):
        self.__food = new_food

    def get_cp(self):
        return self.__cp

    def set_cp(self, new_cp):
        self.__cp = new_cp


# class Student(Member):
#     def __init__(self, new_gender, new_major, new_id):
#         super().__init__(new_gender, new_major, new_id)
#
#     def join_class(self):
#         pass
#
#     def quit_class(self):
#         pass
#
#     def borrow_resources(self):
#         print('student borrow')
#
# ls = [studentA, studentB, professorA, professorB]
#
# for item in ls:
#     item.borrow_resources()
