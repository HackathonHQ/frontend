from tkinter import *   
  
top = Tk()
  
top.geometry("100x100")  
  
def fun():
            if (b1["text"]=="Hahahahaha"):
                b1["text"]="Yo" 
            else:
                b1["text"]="Hahahahaha"
                
b1 = Button(top, text = "Hahahahaha", command = fun, pady=10)  

b1.pack(side = TOP)
  
top.mainloop()
