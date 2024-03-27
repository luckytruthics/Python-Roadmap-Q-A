''' 1.Write a Python program that takes a list of numbers as input and returns a new list containing only the even numbers from the original list. '''

even_number = [i for i in range(1,21) if i%2 == 0]
print(even_number)

# Q2 Write a Python program that takes a list of strings as input and returns a new list containing the lengths of the strings in the original list.

strings_len = [len(i) for i in ["apple", "banana", "orange", "strawberry"]]
strings_len

# Q3 Write a Python program that takes a list of numbers as input and returns a new list containing only the unique elements from the original list, preserving their original order.


empty_list = []
for i in input('Enter the elments: ').split():
   if i not in empty_list:
      empty_list.append(i)


print(empty_list)

# Q4 Write a function that reverses a list in-place, modifying the original list instead of creating a new one.

list1 = [1,2,3,4][2:0:-1][1:3]
print(list1)

# different method
def reverse_list(arg):
  arg = arg[::-1]
  return arg

# Q5 Write a function that flattens a nested list of arbitrary depth into a single-level list.

newlist = []
def flatten_list(list1):
  for element in list1:
      if type(element) == list:
         flatten_list(element)
      else:
        newlist.append(element)
  return newlist

print(flatten_list([1,2,[3,4,5,[6,7]],6]))

# Q6 Write a function given a target value target_num, return the index of an elements inside a list that adds up to the target_num

def target_index(list1,target):
   get_indices = [(indx,ind2) for indx,element in enumerate(list1) for ind2, element2 in enumerate(list1[indx+1:],start=indx+1) if element + element2 == target]
   return get_indices

inp = [1,2,7,5]
target_index(inp,8)

"""# Dictionary Questions"""

# Q1 Write a Python program that takes a dictionary as input and prints all the keys and their corresponding values in the dictionary.

input_dict = {'a': 1, 'b': 2, 'c': 3}
print('OUTPUT')
for key,value in input_dict.items():
  print(f"{key}: {value}",end=' ')

# Q2 Write a function that counts the frequency of each word in a given string and returns a dictionary mapping words to their counts.

from collections import Counter

def count_char_frequency(word):
    return dict(Counter(word))

print(count_char_frequency(input('Enter string: ')))

# Different method
string = input('Enter string: ')
dict1 = {i:string.count(i) for i in string}
print(dict1)

# Q3 Create a function that merges two dictionaries, handling duplicate keys and choosing appropriate conflict resolution strategies

def merge_dict(dict1,dict2):
  new_dict = {}
  for key1,key2 in zip(dict1.keys(),dict2.keys()):
    if key1 == key2 and dict1[key1] != dict2[key2]:
      new_dict[key1] = [dict1[key1],dict2[key2]]
    elif key1 == key2 and dict1[key1] == dict2[key2]:
      new_dict[key1] = dict1[key1]
    else:
      new_dict[key1] = dict1[key1]
      new_dict[key2] = dict2[key2]
  return new_dict

dict([('a',(1,2))])




dict1={'a': 1, 'b': 2, 'c': 3,'d':5}
dict2={'a': 5, 'b': 2, 'c': 3,'e':7}

print(merge_dict(dict1,dict2))

#Q4 Implement a function that reverses a dictionary (swapping keys and values) preserving the orginal structure.

input1 = {'a': 1, 'b': 2, 'c': 3}
reversed_dictionary = dict(sorted(input1.items(),key=lambda x:x[1],reverse=True))
print(reversed_dictionary)
