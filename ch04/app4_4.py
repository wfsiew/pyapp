'''
Created on 21/11/2013

@author: wingfei.seiw
'''

def is_prime(x):
    arr = (2, 3, 5, 7)
    ret = False
    
    if x in arr:
        ret = True
        
    else:
        for i in arr:   
            q = x % i
            if q == 0:
                ret = 1
                break
            
        if ret == 1:
            ret = False
            
        else:
            ret = True
            
    return ret

if __name__ == '__main__':
    k = 0
    for i in range(2, 1001):
        b = is_prime(i)
        if b == True:
            k = k + 1
            print i,
            
            if k % 10 == 0:
                print