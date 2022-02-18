

from os import sep
import math
import numpy as np

#############################
def deneme(a:int):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    print(abs(a))
    

help(deneme)

##########################
print(1,2,3 , sep = " < ")
##########################

def deneme1(x):
    return 5*x
def deneme2(fn,arg):
    return fn(arg) 

print(deneme2(deneme1,2))   

############################

def mod_5(x):
    return x % 5
###########################
print('Which number is biggest?\n',max(5,2,3),"\n",
"Which number is the biggest modulo 5?\n",max(5,2,3,key=mod_5))
#############################
Alphabet = ["A","B","C","D","E","F","G"]

print(Alphabet[0:3])

###############################

squares = [n**2 for n in range(10)]
print(squares)

###############################
planets = ["Dunya","Neptun","Uranüs","galgarafa"]
short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)
################################
y = [9,1,2,3,4,5]
x = np.array([9,1,2,3,4,5])  #Numpy array ile oluşturulmuş bir listenin python listesinden farkları vardır.
print(x+10)
print(x <= 5)
##############################

a = [[9,1,2],[3,4,5]]
b = np.asarray(a)
print(b)
print(type(b))
print(b[1,2]) # matris index