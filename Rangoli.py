# Create a rangoli using python
# print index one first a to z
# n = 5

# def print_rangoli(size):
#     l = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
#     for i in range(1,n):
#         for j in range(1,n-i+1):
#             print(end= "--")
#         for j in range(i,0,-1):
#             print(l[j],end = '-')
#         for j in range(2,i+1):
#             print(l[j],end = '-')
#         for j in range(1,n-i+1):
#             print(end="--")
#         print()
#     for i in range(n,0,-1):
#         for j in range(1,n-i+1):
#             print(end="--")
#         for j in range(i,0,-1):
#             print(l[j],end = '-')        
#         for j in range(2,i+1):
#             print(l[j],end = '-')
#         for j in range(1,n-i+1):
#             print(end="--")
#         print()
# print_rangoli(n) 

# Rangoli for hacker rank 

n = 5

def print_rangoli(size):
    l = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
    for i in range(1,n):
        for j in range(0,n-i):
            print(end= "--")
        for j in range(n,n-i,-1):  #    i = 1,  
            print(l[j],end = '-')
        for j in range(n-i+2,6):
            print(l[j],end = '-')
        for j in range(0,n-i):
            print(end="--")
        print()
    for i in range(n,0,-1):
        for j in range(0,n-i):
            print(end="--")
        for j in range(n,n-i,-1):
            print(l[j],end = '-')        
        for j in range(n-i+2,6):
            print(l[j],end = '-')
        for j in range(0,n-i):
            print(end="--")
        print()
print_rangoli(n) 

