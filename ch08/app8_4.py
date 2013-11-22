'''
Created on 22/11/2013

@author: wingfei.seiw
'''

class SingleList(object):
    
    def __init__(self, initialList = None):
        self.__list = []
        
        if initialList:
            for value in initialList:
                if value not in self.__list:
                    self.__list.append(value)
                    
    def __str__(self, *args, **kwargs):
        tempString = ''
        i = 0
        
        for i in range(len(self)):
            tempString += '%12d' % self.__list[i]
            
            if (i + 1) % 4 == 0:
                tempString += '\n'
                
        return tempString
    
    def __len__(self):
        return len(self.__list)
    
    def __getitem__(self, index):
        return self.__list[index]
    
    def __setitem__(self, index, value):
        if value in self.__list:
            raise ValueError, 'List already contains value %s' % str(value)
        
        self.__list[index] = value
        
    def __eq__(self, other):
        if len(self) != len(other):
            return 0
        
        for i in range(0, len(self)):
            if self.__list[i] != other.__list[i]:
                return 0
            
        return 1
    
    def __ne__(self, other):
        return not (self == other)
    
    def append(self, element):
        if element in self.__list:
            raise ValueError, 'List already contains value %s' % str(element)
        
        self.__list.append(element)
        
    def count(self):
        return len(self)
    
    def index(self, element):
        return self.__list.index(element)
    
    def insert(self, index, element):
        if element in self.__list:
            raise ValueError, 'List already contains value %s' % str(element)
        
        self.__list.insert(index, element)
        
    def pop(self):
        self.__list.pop()
        
    def remove(self, value):
        self.__list.remove(value)
        
    def reverse(self):
        self.__list.reverse()
        
    def sort(self):
        self.__list.sort(cmp=None, key=None, reverse=False)
        
    def __delitem__(self, index):
        del self.__list[index]
        
    def __contains__(self, element):
        return element in self.__list
        
k = SingleList([8, 5, 3, 9])
del k[2]
print k