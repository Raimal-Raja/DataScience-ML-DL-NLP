# class Computer:
    # def __init__(self, cpu, ram):
    #     self.cpu = cpu
    #     self.ram = ram
        
    # def config(self):
    #     print(self.cpu, self.ram)
        
        
    # def __init__(self, age, name):
    #     self.name = name
    #     self.age = age
        
    # def compare(self, obj):
    #     if self.age == obj.age:
    #         return True
    #     else:
    #         return False
       




# comp1 = Computer('i5', '8GB')
# comp2 =  Computer('Ryzen', '32GB')

# comp1.config()
# comp2.config()


# c1 = Computer(20, 'Raimal')
# c1.age = 23
# c2 = Computer(20, 'Raimal')

# if c1.compare(c2):
#     print("they are same")
# else:
#     print('They are different')




# ## instance variables and class variable
# class Car:
#     wheel = 4
    
#     def __init__(self):
#         self.modl = 23
#         self.compy =  "BMW"
        

# cr1 = Car()

# cr1.compy = 'Corola'

# cr2 = Car()

# print(cr1.compy, cr1.modl, cr1.wheel)
# print(cr2.compy, cr2.modl, cr2.wheel)


# class Student:
#     school = 'Telusko'
    
#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
        
#     def avg(self):
#         return (self.m1 + self.m2 + self.m3)/3
    
#     @classmethod
#     def get_school(cls):
#         return cls.school
    
    
#     @staticmethod
#     def info():
#         print("This is a static method")
    

# s1 =  Student(23,23,34)
# s2 =  Student(11,45,78)

# print(s1.avg())
# print(Student.get_school())
# Student.info()

# class X:
#     def __init__(self):
#         print('this class x')

# class A(X):
#     def __init__(self):
#         print('i am inside A init')
        
#     def hello():
#         print('Hello')
    
# class B(X):
#     def __init__(self):
#         super().__init__()
#     print('i am inside B')
#     def welcome():
#         print("Welcome to learn OOP")
        
# class C(A,B):
#     def __init__(self):
#         print('i am inside c')
        
        
# b = B()
# # a= A()

class Pycharm:
    def ide(self):
        print("ide")
class Myeditor:
    def execute(self):
        print("Ide executed")
        

class laptop:
    def code(self, ide):
        ide.execute()
        
ide = Myeditor()
lap1 = laptop()
lap1.code(ide)
