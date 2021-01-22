#Testing is a process of analysing a software item to detect the differences 
# between existing and required conditions (i.e. defects) and to evaluate the features of the software item'

#1.test and code should be seperated into diffrent python folder

#2.filenames for testing folder should be:
# test_[name].py
# or [name]_test.py.


#3.name of the function must be in the form 
# def [name]_test(): 
# or def test_[name]():



# import pytest
# from ..exercise1 import shopping_items

# def test_class_items_id():
#     #arrange
#     underTest = shopping_items('Clothes', 'nike', '100', 'None')
#     #act
#     #assert
#     assert underTest.id == 'Clothes-nike-100-None'

# def test_class_items_id_priceIsNone():
#     #arrange
#     underTest = shopping_items('meat', 'beef',None, '19012020')
#     #act
#     #assert
#     assert underTest.id == 'meat-beef--19012020'

# def test_class_itemsexpirylog_works():
#     #arrange
#     underTest = shopping_items('Clothes', 'nike', '100', 'None')
#     #act
#     result = underTest.itemsexpirylog()
#     #assert
#     assert result == 'nike None'

