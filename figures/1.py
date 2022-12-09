import os

l = os.listdir('.')
for i in l:
    if i[-5] == ')':
        nn = i.replace('(','_').replace(')','').replace(' ','')
        print(i, nn)
