import os
import unittest

def classify_triangle(a,b,c):
	while True:
		try:
			a = int(a)
			b = int(b)
			c = int(c)
		except ValueError:
			return "Invalid entries. Please try again"
			break
		else:
			if (a == 0 or b == 0 or c == 0):
				return "Not a Triange"
				break
			if (a == b and b == c):
				return "Equilateral"
				break 
			if (a != b):
				if (a == c or b == c):
					return "Isoceles"
					break
				if (pow(a,2) + pow(b,2) == pow(c,2)):
					return "Right"
					break
				if (a != c):
					return "Scalene"
					break

#a = 3
#b = 4
#c = 5
#result=classify_triangle(a,b,c)
#print(result)


def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classify_triangle(',a, ',', b, ',', c, ')=',classify_triangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle('hello',1,2),'Invalid entries. Please try again', 'hello,1,2 Invalid entries. Please try again')
        self.assertNotEqual(classify_triangle(1,2,3), 'Isoceles', 'Should be Scalene')
        self.assertNotEqual(classify_triangle(0,0,0), 'Equilateral', 'Should be Not a Triange')
    
    def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classify_triangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(classify_triangle(10,15,30),'Scalene','Should be Isoceles')
        

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(0,0,0)
    runClassifyTriangle('hello',1,2)
    runClassifyTriangle(3,4,5)
    
    #unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line