'''
Created on 21/11/2013

@author: wingfei.seiw
'''

def to_fahrenheit(c):
    f = (9 / 5.0) * c + 32
    return f

if __name__ == '__main__':
    print 'Celsius\tFahrenheit'
    for i in range(101):
        f = to_fahrenheit(i)
        print '%d\t%.1f' % (i, f)