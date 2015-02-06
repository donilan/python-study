#!/usr/bin/env python

class A(object):
    def method1(self):
        print "A.method1"

old_method = A.method1
def new_method(self):
    print 'new_method'
    return old_method(self)

A.method1 = new_method
if __name__ == '__main__':
    A().method1()
