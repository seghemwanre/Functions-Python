#def greet(): 
 #  return ('Hello Solomon')
#print (greet())
#==========================

'''
functions with parameters
'''
#def greet (name):
  #'''
  #greets a person passed in as an argument 
  #name: a name of a person to greet 
  #'''
  #return f"hello {name}, Goodmorning"
#print (greet('solomon'))
#print (greet('marvin'))
#print (greet('david'))
#help(greet)

'''
arbitrary parameters
'''
#def fruit (*names):
  #'''
  #Accept a number of fruit names and print each of them 
  #*name: list of fruits
  #'''
  #for fruit in names:
  #  print (fruit)
#fruit("orange", "apple", "grapes")
#help(fruit)

'''
keyword argument 
'''
#def greet (name, msg):

 # return f'Hello {name}, {msg}'

#print (greet(name='Solomon', msg= 'Goodmorning'))
#print (greet(msg='Goodmorning', name= 'david'))

'''
arbitrary keyword 
'''
#def person (**student):
 # for key in student: 
 #   print (student[key])

#person(fname="Solomon", lname="Eghemwanre", #subject = "python")

'''
default parameters
'''
#def greet (name = "david"):
 # return f"hello, {name}"
#print (greet())
#print (greet("solomon"))

'''
pass statement
'''
#def greet ():
 # pass 

'''
Recusion
'''
def factorial_recursive(n):
  '''
    Multiply a given number by every number less than it downn to 1 in a factorial way
    e.g if n is 5 then calculate 5*4*3*2*1 = 120
    n: is the highest starting number
    '''

  if n==1:
    return True
  else:
      return n * factorial_recursive (n-1)
print (factorial_recursive(5))