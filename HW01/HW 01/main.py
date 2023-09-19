import unittest
import brand

def classifyTriangle(a,b,c):
    if a + b > c and b + c > a and a + c > b and min(a, b, c) > 0:
        if a == b == c:
            return "Equilateral"
        elif a == b or a == c or b == c:
            return "Isoceles"
        elif max(a, b, c) ** 2 == ((a + b + c) - max(a, b, c) - min(a, b, c)) ** 2 + min(a, b, c) ** 2:
                return 'Right'
        else:
            return "Scalene"
    else:
        return "NotATriangle"
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")
class TestTriangles(unittest.TestCase):
    def testInvalidInputs(self):
        self.assertEqual(classifyTriangle(3,2,1), 'NotATriangle')
        self.assertNotEqual(classifyTriangle(3,3,3), 'NotATriangle')
    def testEqulateral(self):
        self.assertEqual(classifyTriangle(3,3,3), 'Equilateral')
        self.assertNotEqual(classifyTriangle(5,4,3), 'Equilateral')
    def testIsoceles(self):
        self.assertEqual(classifyTriangle(3,3,2), 'Isoceles')
        self.assertNotEqual(classifyTriangle(5,4,3), 'Isoceles')
    def testScalene(self):
        self.assertEqual(classifyTriangle(2,4,3), 'Scalene')
        self.assertNotEqual(classifyTriangle(3,3,3), 'Scalene')
    def testRight(self):
        self.assertEqual(classifyTriangle(5,4,3), 'Right')
        self.assertNotEqual(classifyTriangle(3,3,3), 'Right')
if __name__ == '__main__':
    brand.my_brand('HW 01 - Testing Triangle Classification')
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(5,4,3)
    runClassifyTriangle(2,4,3)
    runClassifyTriangle(3,3,4)
    unittest.main(exit=False)
    brand.my_brand('HW 01 - Testing Triangle Classification')



