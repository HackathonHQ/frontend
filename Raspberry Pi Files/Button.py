from gpiozero import Button
b1 = Button(2)
b2 = Button(3)

s = ''
a = 0

def save():
       print (a) 
    
def hello():
    a = a + 1
    
b1.when_pressed = hello
b2.when_pressed = save
