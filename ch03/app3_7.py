'''
Created on 21/11/2013

@author: wingfei.seiw
'''

def show_space(x):
    for i in range(x):
        print ' ',
        
def show_star(x):
    for i in range(x):
        print '*',

def show_singleline():
    for i in range(1, 11):
        show_star(i)
        show_space(10 - i)
        
        show_star(11 - i)
        show_space(i - 1)
        
        show_space(i - 1)
        show_star(11 - i)
        
        show_space(10 - i)
        show_star(i)
        
        print

def show_multiline():
    for i in range(1, 11):
        show_star(i)
        print
        
    print
    
    for i in range(10, 0, -1):
        show_star(i)   
        print
        
    print
        
    for i in range(10):
        show_space(i)
        show_star(10 - i) 
        print
        
    print
    
    for i in range(1, 11):
        show_space(10 - i)
        show_star(i) 
        print

if __name__ == '__main__':
    show_multiline()
    print
    show_singleline()