fruits=['Mango','Apple','Coconut','Apple']
vegetables=['Tomato','drumsticks']
fruits.extend(vegetables)
print(f'after extend :{fruits}')
#del delete the element in specified index
del fruits[0]
print(f'after del :{fruits}')
#pop delete last element if index not defined
fruits.pop()
print(f'after pop :{fruits}')
#remove delete the first occurrence of specified value
fruits.remove('Apple')
print(f'after remove :{fruits}')
#slicing each alternative location
print(f'slicing each alternative location :{fruits[::2]}')
#sort
fruits.sort(reverse=False)
print(f'after sorting :{fruits}')
if 'Apple' in fruits:
    print('Apple is in fruits')
else:
    print('Apple is not in fruits')
setOfFruits=set(fruits)
print(f'after storing as set :{setOfFruits}')
setOfFruits.add('Potato')
print(f'after adding {setOfFruits}')
setOfPlants=setOfFruits.copy()
print(f'after copying from another set: {setOfPlants}')
#by using assignment operation, two sets uses same memory location , if one set value changes other set value also get changes
setOfPlants=setOfFruits
print(f'after assigning {setOfPlants}')
setOfFruits.add('duplicate')
print(f'after adding {setOfFruits}')
print(setOfPlants)