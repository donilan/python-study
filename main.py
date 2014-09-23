#!/usr/bin/env python

def add_properties(clazz):
  clazz.a = 1
  clazz.b = 2
  clazz.c = 3

class A:
  pass

add_properties(A)



if __name__ == '__main__':
  a = A()
  print a.a, a.b, a.c
