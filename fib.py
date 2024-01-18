

def fib(n):
    if n<0:
        raise ValueError('Value must be positive')
    else:
        
        res=[0] if n==0 else [0,1]
        a=0
        b=1
        for i in range(n-2):
            c=a+b
            a,b=b,c
            res.append(c)
        return res
    
