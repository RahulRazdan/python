import sys
import random

if len(sys.argv) < 2:
    print("minimum 2 args required")
    exit(1)
else:
    print(sys.argv)
    
print(sys.args())
result = int(sys.argv[1]) * int(sys.argv[2]) 
print("your answer is " + str(result))

def testFunction(name):
    print(name)

def start_with_a_vowel(word):
    return word[0] in "AEIOU"

testFunction("Rahul Razdan")
print(start_with_a_vowel("Adssdfg"))
print(start_with_a_vowel("Rahul"))
