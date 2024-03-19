def fib(n):
    list=[]
    if n==1:
        list= [0]
    elif n==2:
        list=[0,1]
    else:
        list=[0,1]
        for i in range(n-2):
            list.append(list[len(list)-2]+list[len(list)-1])
         
    return list
        
        
        
print(fib(10))
