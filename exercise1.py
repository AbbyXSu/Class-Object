# Python Object- Oriented Programming 
# objective : allow us to group data(attributes) and fucntions(methods) in a way that it is more efficeint to reuse it 
# in the future without rewriting the same code or build upon it.

# shopping cart case - where we have an shopping cart full of items:

# Naturally items contain its type, name and expirydate , these are the attribute of the object

# Concept 1:A Class is like an object constructor, or a "blueprint" for creating objects with its data and information
# create class format: 
# class [class_name]

# Concept 2. each instances in the class contains unique data, as you see in the output, 
# they has its own unique location and memory, they are called Instance Variable/Attribure
# -------------------------------------------------------------------------------------------
# class shopping_item:
#    pass
# item1 = shopping()
# item2 =shopping()

# print(item1)
# print(item2)

# <__main__.shopping object at 0x0000021EFE5DA280>
# <__main__.shopping object at 0x0000021EFE5DA550>
# --------------------------------------------------------------------------------------------

# long code needing to be write everytime we put one more items in your shopping cart,
# instead , an __init__ function can summarise your code under one reusable methods/function.(at as a contructor)
# class shopping_item:
#     pass
#     def __init__(self,type,name,price,expiry):
#         self.type = type
#         self.name=name
#         self.expiry=expiry
#         self.price = price if price else ''
#         self.id = self.type + '-' + self.name + '-' + str(self.price) + '-' + self.expiry
#     def itemsexpirylog (self):#all the method in class, automatically takes the instance self as the first argument 
#         return f'{self.name} {self.expiry}'

# item1=shopping_item('fruit','watermalon',3.5,'21012021')
# item2=shopping_item('catergory','product',50,'expiryby')

# print(item1.id)
# print(item2.id)
# print (item1.itemsexpirylog())#to simplify and avoid typing each time , we can create a function within the class
# as it is a method, when calling it , remember to add the () 
# alternatively: you can call the fuction via class, but needing to put the object name in the ()
# print (shopping_items.itemsexpirylog(item1))

# -----------------------------------------------------------------------------------------------
# before:

# class shopping_items:
#     pass
# item1=shopping_item()
# item2=shopping_item()

# item1.type='furit'
# item1.name='watermelon'
# item1.expiry='21012021'
# item1.price = 3.5
# item1.id='furit-watermelon-3.5-21012021'

# item2.type='category'
# item2.name='product'
# item2.expirydate ='expiryBy'
# _____________________________________________________________________________

# #Class Variable

# #class shopping_items:
#     #number_of_items =0
#     #discount=0.50 
    
# # this is a variabe that defined at the class level, 
# # therefore it is called class variable
# # it helps you to avoid hardcoding it a fixed amount in fuctions
#     # create an __init__method: it runs everytime you create a object
#     #def __init__(self,type,name,price,expiry):
#         self.type = type
#         self.name=name
#         self.expiry=expiry
#         self.price = price if price else ''
#         self.id = self.type + '-' + self.name + '-' + str(self.price) + '-' + self.expiry
#         shopping_items.number_of_items +=1

#     #all the method in class, automatically takes the instance self as the first argument 
#     def itemsexpirylog (self):
#         return f'{self.name} {self.expiry}'
        
#     def apply_discount(self):
#         self.price = float(self.price *self.discount)
#         # you can you class_name.attribute format, 
#         # but if you use self.atrribute format, it allows subclass to override the attribute

# item1=shopping_items('fruit','watermalon',3.6,'21012021')
# item2=shopping_items('catergory','product',50,'expiryby')

# print (shopping_items.number_of_items)

# print(shopping_items.discount)
# print(item1. discount)
# print (item2.discount)

#how to applu discount on item
# print(item1.price)
# item1.apply_discount()
# print(item1.price)

#when discount is set as a class varaible, you see it apply to all item automatically,
#however, it is not the arttibute to the instances, but the attribute to the class.
#print(shopping_items.__dict__)
#print(item1.__dict__)

#print(shopping_items.discount)
#print(item1. discount)
#print (item2.discount)
#__________________________________________________________________________________________________________________
# class shopping_items:
#     number_of_items =0
#     discount=0.50 

#     def __init__(self,type,name,price,expiry):
#         self.type = type
#         self.name=name
#         self.expiry=expiry
#         self.price = price if price else ''
#         self.id = self.type + '-' + self.name + '-' + str(self.price) + '-' + self.expiry
#         shopping_items.number_of_items +=1
#     def itemsexpirylog (self):
#         return f'{self.name} {self.expiry}'
        
#     def apply_discount(self):
#         self.price = float(self.price *self.discount)

#The classmethod() is an inbuilt function in Python, 
# which returns a class method for a given function, 
# It is a decorator, A decorator is a design pattern in Python that allows a user 
# to add new functionality to an existing object without modifying its structure
# It must  take a [cls] parameter that points to the class—and not the object instance—when the method is called
#     @classmethod 
#     def set_discount(cls,rate):
#         cls.discount=rate

# item1=shopping_items('fruit','watermalon',3.6,'21012021')
# item2=shopping_items('catergory','product',50,'expiryby')

# shopping_items.set_discount(0.8)

# print (shopping_items.discount)
# print (item1.discount)
# print (item2.discount)
#______________________________________________________________________________________________________________________________

# another way to use class method
# class shopping_items:
#     number_of_items =0
#     discount=0.50 

#     def __init__(self,type,name,price,expiry):
#         self.type = type
#         self.name=name
#         self.price = price if price else ''
#         self.expiry=expiry
#         self.id = self.type + '-' + self.name + '-' + str(self.price) + '-' + self.expiry
#         shopping_items.number_of_items +=1
#     def itemsexpirylog (self):
#         return f'{self.name} {self.expiry}'
        
#     def apply_discount(self):
#         self.price = float(self.price *self.discount)

#     @classmethod 
#     def set_discount(cls,rate):
#         cls.discount=rate

# # classmethod () also allows you to seprate the attribute of the object into defined format
#     @classmethod
#     def from_string(cls,new_items_string):
#         type,name,price,expiry = new_items_string.split('-')
#         return cls(type,name,price,expiry)

# item1=shopping_items('fruit','watermalon',3.6,'21012021')
# item2=shopping_items('catergory','product',50,'expiryby')

# new_str1='drink-tea-2.5-21012022'
# new_str2='veg-tomato-10-25012021'

# new_item1=shopping_items.from_string(new_str1)
# new_item2 =shopping_items.from_string(new_str2)

# print(new_item1.price)
# print(shopping_items.number_of_items)
#-----------------------------------------------------------------------------------------------------------
# staticmethod
# class shopping_items:
#     number_of_items =0
#     discount=0.50 

#     def __init__(self,type,name,price,expiry):
#         self.type = type
#         self.name=name
#         self.price = price if price else ''
#         self.expiry=expiry
#         self.id = self.type + '-' + self.name + '-' + str(self.price) + '-' + self.expiry
#         shopping_items.number_of_items +=1
#     def itemsexpirylog (self):
#         return f'{self.name} {self.expiry}'
        
#     def apply_discount(self):
#         self.price = float(self.price *self.discount) 

#     @classmethod
#     def set_discount(cls,rate):
#         cls.discount=rate

#     @classmethod
#     def from_string(cls,new_items_string):
#         type,name,price,expiry = new_items_string.split('-')
#         return cls(type,name,price,expiry)
    
# #This type of method takes neither a self nor a cls parameter, 
# # it does not modify class or instance, nor making any reference to them
#     @staticmethod
#     def is_ShopOpen(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return 'shop is closed'
#         return 'shop is open'

# import datetime
# # today=datetime.date(2021,1,23)
# # print(shopping_items.is_ShopOpen(today))

# #___________________________________________________________________________________________________________________________________________________________

# class shopping_items:
#     number_of_items =0
#     discount=0.50 

#     def __init__(self,type,name,price,expiry):
#         self.type = type
#         self.name=name
#         self.price = price if price else ''
#         self.expiry=expiry
#     def itemsexpirylog (self):
#         return f'{self.name} {self.expiry}'
        
#     def apply_discount(self):
#         self.price = float(self.price *self.discount) 

# class techProduct(shopping_items):
#     discount =0.9
    
#     def __init__(self,type,name,price,expiry,version):
#         super().__init__(type,name, price,expiry)
#         self.version=version
        
# # the subclass inherent all methods from the class it refered to 
# #subclass can set its own attribute without affecting or being affested by the attribute of the main/parent class
# #print(help(techProduct))can show what functions has been inherented from parent class
# techitem1=techProduct('computer','Mac_mini',1500,'none','2021')
# techitem2=techProduct('phone','oneplus',300,'none','3T')

# print(techitem2.version)
# print(techitem2.price)
# techitem2.apply_discount()
# print(techitem2.price)

#__________________________________________________________________________________________________________________________________
class shopping_item:
    number_of_items =0
    discount=0.50 

    def __init__(self,type,name,price):
        self.type = type
        self.name=name
        self.price = price if price else ''

    def itemspricelog (self):
        return f'{self.name} {self.price}'
        
    def apply_discount(self):
        self.price = float(self.price *self.discount) 
class techProduct(shopping_item):
    discount =0.9
    
    def __init__(self,type,name,price,version):
        super().__init__(type,name, price)
        self.version=version
        
class techShopping(shopping_item):
    def __init__(self, type, name, price,techShopping=None):
        super().__init__(type, name, price)
        if techShopping == None:
            self.techShoppings=[]
        else:
            self.techShopping=techShopping

    def add_techitem_toShopping(self, techitem):
        if techitem not in self.techShopping:
            self.techShopping.append(techitem)
        
    def remove_techitem_fmShopping(self, techitem):
        if techitem in self.techShopping:
            self.techShopping.remove(techitem)
        
    def print_techShopping(self):
        for techitem in self.techShopping:
            print('You have these items in your techShopping--->',techitem.itemspricelog())

techitem1=techProduct('phone','oneplus',300,'3T')
techitem2=techProduct('TV','philip',999,'4KWide')
techshp1=techShopping('Shopping','Bags',0,[techitem1])

techshp1.add_techitem_toShopping(techitem2)
techshp1.print_techShopping()


# print(techitem2.version)
# print(techitem2.price)
# techitem2.apply_discount()
# print(techitem2.price)
