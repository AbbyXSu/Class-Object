# getters, setters and deleters

#Getter - property methods - update all attribute assocaite with an updated data without changing coding of the class
class shopping_item:
    def __init__(self,type,name,price):
        self.type = type
        self.name=name
        self.price = price if price else ''
    @property
    def describe(self):
        return f'{self.type} > {self.name}'
    @property
    def itemspricelog (self):
        return f'{self.name} {self.price}'
#Setter : use the full decribption of the item to replace /reset item's original attribute
#without changing the code in the class
    @itemspricelog.setter
    def itemspricelog(self,updatedPricelog):
        name, price = updatedPricelog.split()
        self.name= name
        self.price =price

item1=shopping_item('fruit','watermalon',3.6)

item1.itemspricelog = 'orange 4.7'


print(item1.price)
print(item1.describe)
print(item1.itemspricelog)