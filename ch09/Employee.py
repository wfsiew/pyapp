'''
Created on Nov 22, 2013

@author: wfsiew
'''

from Date import Date

class Employee(object):
    '''
    classdocs
    '''


    def __init__(self, first, last, bdt, deptcode):
        '''
        Constructor
        '''
        if self.__class__ == Employee:
            raise NotImplementedError, 'Cannot create object of class Employee'
        
        self.firstName = first
        self.lastName = last
        self.birthDate = bdt
        self.departmentCode = deptcode
        
    def __str__(self):
        return '%s %s' % (self.firstName, self.lastName)
    
    def _checkPositive(self, value):
        if value < 0:
            raise ValueError, 'Attribute value (%s) must be positive' % value
        
        else:
            return value
        
    def earnings(self):
        raise NotImplementedError, 'Cannot call abstract method'
    
class Boss(Employee):
    def __init__(self, first, last, salary, bdt, deptcode):
        super(Boss, self).__init__(first, last, bdt, deptcode)
        self.weeklySalary = self._checkPositive(float(salary))
        
    def earnings(self):
        return self.weeklySalary
    
    def __str__(self):
        return '%17s: %s' % ('Boss', Employee.__str__(self))
    
class CommissionWorker(Employee):
    def __init__(self, first, last, salary, commission, quantity, bdt, deptcode):
        super(CommissionWorker, self).__init__(first, last, bdt, deptcode)
        self.salary = self._checkPositive(float(salary))
        self.commission = self._checkPositive(float(commission))
        self.quantity = self._checkPositive(quantity)
        
    def earnings(self):
        return self.salary + self.commission * self.quantity
    
    def __str__(self):
        return '%17s: %s' % ('Commission Worker', Employee.__str__(self))

class PieceWorker(Employee):
    def __init__(self, first, last, wage, quantity, bdt, deptcode):
        super(PieceWorker, self).__init__(first, last, bdt, deptcode)
        self.wagePerPiece = self._checkPositive(float(wage))
        self.quantity = self._checkPositive(quantity)
        
    def earnings(self):
        return self.quantity * self.wagePerPiece
    
    def __str__(self):
        return '%17s: %s' % ('Piece Worker', Employee.__str__(self))

class HourlyWorker(Employee):
    def __init__(self, first, last, wage, hours, bdt, deptcode):
        super(HourlyWorker, self).__init__(first, last, bdt, deptcode)
        self.wage = self._checkPositive(float(wage))
        self.hours = self._checkPositive(float(hours))
        
    def earnings(self):
        if self.hours <= 40:
            return self.wage * self.hours
        
        else:
            return 40 * self.wage + (self.hours - 40) * self.wage * 1.5
         
    def __str__(self):
        return '%17s: %s' % ('Hourly Worker', Employee.__str__(self))

bdt = Date(22, 11, 1988)
employees = [Boss("John", "Smith", 800.00, bdt, '0001'),
             CommissionWorker("Sue", "Jones", 200.0, 3.0, 150, bdt, '0002'),
             PieceWorker("Bob", "Lewis", 2.5, 200, bdt, '0003'),
             HourlyWorker("Karen", "Price", 13.75, 40, bdt, '0004')]

for employee in employees:
    earnings = employee.earnings()
    
    if employee.birthDate.month == 11:
        earnings += 100
        
    print "%s earned $%.2f" % (employee, earnings)