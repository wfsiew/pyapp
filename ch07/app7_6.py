'''
Created on 22/11/2013

@author: wingfei.seiw
'''

class Rectangle(object):
    '''
    classdocs
    '''

    def __init__(self, length = 1, width = 1):
        '''
        Constructor
        '''
        self.__length = length
        self.__width = width
        
    def setLength(self, length):
        if 0.0 < length < 20.0:
            self.__length = length
            
        else:
            raise ValueError, 'Invalid length: %.1f', length
        
    def setWidth(self, width):
        if 0.0 < width < 20.0:
            self.__width = width
            
        else:
            raise ValueError, 'Invalid width: %.1f', width
        
    def getLength(self):
        return self.__length
    
    def getWidth(self):
        return self.__width
        
    def perimeter(self):
        return self.getLength() * 2 + self.getWidth() * 2
    
    def area(self):
        return self.getLength() * self.getWidth()