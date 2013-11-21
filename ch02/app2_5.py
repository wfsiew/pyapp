'''
Created on 21/11/2013

@author: wingfei.seiw
'''

if __name__ == '__main__':
    a = raw_input('Enter readius: ')
    x = int(a)
    pi = 3.14159
    
    print 'Diameter = %d' % (2 * x)
    print 'Circumference = %.2f' % (2 * pi * x)
    print 'Area = %.2f' % (pi * x * x)