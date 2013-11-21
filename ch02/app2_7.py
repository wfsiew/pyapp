'''
Created on 21/11/2013

@author: wingfei.seiw
'''

if __name__ == '__main__':
    a = raw_input('Enter number 1: ')
    b = raw_input('Enter number 2: ')
    x = int(a)
    y = int(b)
    
    v = x % y
    
    if v == 0:
        print '%d is multiple of %d' % (x, y)
        
    else:
        print '%d is not multiple of %d' % (x, y)