''' 
SHAPE CLASS WITH AREA METHOD
'''

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width=width
    def area(self):
        return self.length*self.width
        

class Circle:
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return math.pi*(self.radius**2)

if __name__ == '__main__':  
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()










'''
MISSING CHARACTERS
'''
import math
import os
import random
import re
import sys

def missingCharacters(s):
    # Write your code here
    
    l=[0]*123
    result=" "
    for i in range(len(s)):
        x=ord(s[i])
        l[x]+=1
    for i in range(48,58):
        if(l[i]==0):
            result+=chr(i) 
    for i in range(97,123):
        if (l[i]==0):
            result+= chr(i)
    
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
