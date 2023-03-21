import os;  
os.remove("D:\\file.txt")
fileptr = open("D:\\file.txt","w+");   
fileptr.write(input('What to write into file: \n'))
fileptr.close()
input('\nPress ENTER to exit')
