'''
Created on Nov 21, 2013

@author: wfsiew
'''

def get_sum(x):
    v = 0
    for i in range(1, x):
        a = x % i
        if a == 0:
            v = v + i
            
    return v

def is_perfect(x):
    s = get_sum(x)
    if x == s:
        return True
    
    else:
        return False

if __name__ == '__main__':
    for i in range(1, 1001):
        if is_perfect(i):
            print i