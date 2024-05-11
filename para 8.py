# try:
#     print(123)
#     print("Hello")
#     print(10 / 0)
# except NameError:
#     print("Помилка написання тексту")
# except ZeroDivisionError as error:
#     print(error)
#
# try:
#     print(10)
# except:
#     print("Якась помилка")
# finally:
#     print("Не має помилок, все виконалося успішно")


# def checker(var):
#     if (var < 10):
#         raise TypeError("Число має бути більше або дорівнювати 10")
#     else:
#         return var
#
# number = 3
# print(checker(number))

class BuildingError(Exception):
    def __stf__(self):
        return f"Введені не вірні параметри"

def checker(material_count, limit):
    if material_count < limit:
        raise BuildingError("Матеріалів не достатньо")
    else:
        print("Матеріалів достатньо")

material = 450
checker(material,450)