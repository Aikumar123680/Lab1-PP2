import os
path='\\Users\\Bekarys\\Desktop\\python\\Lab-5'
def f(path):
    if os.path.exists(path):
        print(f"{path} exists")

        d=os.path.dirname(path)
        print(f"{d} is a directory portion")

        f_n=os.path.basename(path)
        print(f"{f_n} is a file name")
    else:
        print("The file does not exists")

f(path)