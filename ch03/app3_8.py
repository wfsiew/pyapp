'''
Created on 21/11/2013

@author: wingfei.seiw
'''

if __name__ == '__main__':
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                total = i ** 2 + j ** 2
                hyp = k ** 2
                if total == hyp:
                    print 'side1 = %d, side2 = %d, hyp = %d' % (i, j, k)