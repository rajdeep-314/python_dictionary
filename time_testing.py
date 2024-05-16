# To test the time it takes to look up the number 'n' in three data structures each with elements 1,2,...,k (n <= k, of course)

from dictionary import dictionary
import time

n = 1000000
k = 1000000

def list_():
    l = [i+1 for i in range(k)]
    
    st = time.time()
    x = n in l
    et = time.time()

    return et-st


def dict_():
    d = {i+1:None for i in range(k)}

    st = time.time()
    x = n in d
    et = time.time()

    return et-st


def dictionary_():
    d = dictionary([(i+1, None) for i in range(k)])

    st = time.time()
    x = d.key_membership(n)
    et = time.time()

    return et - st


t_list = list_()
t_dict = dict_()
t_dictionary = dictionary_()

print("List :\t", t_list)
print("Python's dictionary :\t", t_dict)
print("My dictionary :\t", t_dictionary)
