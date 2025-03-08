import os

path=os.getcwd()
os.chdir('\\Users\\Bekarys\\Desktop\\python\\Lab-5')
l=os.listdir()
for i in l:
    if os.path.isfile(i):
        print(i)