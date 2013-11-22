'''
Created on 22/11/2013

@author: wingfei.seiw
'''

class Time(object):
    
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.setTime(hour, minute, second)
        
    def setTime(self, hour, minute, second):
        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)
        
    def setHour(self, hour):
        if 0 <= hour < 24:
            self.__hour = hour
            
        else:
            raise ValueError, 'Invalid hour value: %d' % hour
        
    def setMinute(self, minute):
        if 0 <= minute < 60:
            self.__minute = minute
            
        else:
            raise ValueError, 'Invalid minute value: %d' % minute
        
    def setSecond(self, second):
        if 0 <= second < 60:
            self.__second = second
            
        else:
            raise ValueError, 'Invalid second value: %d' % second
        
    def getHour(self):
        return self.__hour
    
    def getMinute(self):
        return self.__minute
    
    def getSecond(self):
        return self.__second
    
    def tick(self):
        second = self.getSecond() + 1
        second = second % 60
        self.setSecond(second)
        
        if second == 0:
            self.tickMinute()
            
    def tickMinute(self):
        minute = self.getMinute() + 1
        minute = minute % 60
        self.setMinute(minute)
        
        if minute == 0:
            self.tickHour()
            
    def tickHour(self):
        hour = self.getHour() + 1
        hour = hour % 24
        self.setHour(hour)

    def printMilitary(self):
        print '%.2d:%.2d:%.2d' % \
        (self.getHour(), self.getMinute(), self.getSecond()),
        
    def printStandard(self):
        standardTime = ''
        
        if self.getHour() == 0 or self.getHour() == 12:
            standardTime += '12:'
            
        else:
            standardTime += '%d:' % (self.getHour() % 12)
            
        standardTime += '%.2d:%.2d' % (self.getMinute(), self.getSecond())
        
        if self.getHour() < 12:
            standardTime += ' AM'
            
        else:
            standardTime += ' PM'
            
        print standardTime,
        
t = Time(23, 59, 59)
t.tick()
t.printStandard()