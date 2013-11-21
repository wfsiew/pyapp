'''
Created on 21/11/2013

@author: wingfei.seiw
'''

if __name__ == '__main__':
    n = 0
    total = 0
    avg = 0
    
    x = 0
    
    while x != -1:
        a = raw_input('Enter the gallons used (-1 to end): ')
        x = float(a)
        
        if x == -1:
            break
        
        b = raw_input('Enter the miles driven: ')
        y = int(b)
        
        miles_per_gallon = y / x
        n = n + 1
        total = total + miles_per_gallon
        
        print 'The miles / gallon for this tank was %f' % (miles_per_gallon)
        
    if n > 0:
        avg = total / n
        print 'The overall average miles/gallon was %f' % (avg)
        
    else:
        print 'The overall average miles/gallon was 0'