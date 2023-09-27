# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangleA(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual(classifyTriangle(3,3,3), 'Equilateral', '3,3,3 should be equilateral')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(2,3,4), 'Scalene', '2,3,4 should be scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(5,12,9), 'Scalene', '5,12,9 should be scalene')

    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(5,5,7), 'Isoceles', '5,5,7 should be isoceles')

    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(2,3,2), 'Isoceles', '2,3,2 should be isoceles')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(200, 200, 200), 'InvalidInput', '200,200,200 should be invalid')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(0,0,0), 'InvalidInput', '0,0,0 should be invalid')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(1,2,1.2), 'InvalidInput', '1,2,1.2 should be invalid')

    def testNotTriangle(self):
        self.assertEqual(classifyTriangle(1,2,3), 'NotATriangle', '1,2,3 should not be a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

