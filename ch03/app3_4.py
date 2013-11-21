'''
Created on 21/11/2013

@author: wingfei.seiw
'''

if __name__ == '__main__':
    a = raw_input('Enter 5 digit integer: ')
    x = int(a)
    
    y = x / 10000
    if y < 1 or y > 9:
        print 'Invalid integer'
        
    else:
        x1 = x / 10000
        r1 = x % 10000
        x2 = r1 / 1000
        
        y1 = x % 10
        m1 = x / 10
        y2 = m1 % 10
        
        if x1 == y1 and x2 == y2:
            print 'The integer %d is palindrome' % x
            
        else:
            print 'The integer %d is not palindrome' % x