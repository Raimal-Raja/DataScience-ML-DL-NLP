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




## instance variables and class variable
class Car:
    wheel = 4
    
    def __init__(self):
        self.modl = 23
        self.compy =  "BMW"
        

cr1 = Car()

cr1.compy = 'Corola'

cr2 = Car()

print(cr1.compy, cr1.modl, cr1.wheel)
print(cr2.compy, cr2.modl, cr2.wheel)

