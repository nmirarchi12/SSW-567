import unittest

def classify_side_angle(side_a, side_b, side_c):
	while True:
		try:
			side_a = int(side_a)
			side_b = int(side_b)
			side_c = int(side_c)
		except ValueError:
			return "Invalid entries. Please try again"
		else:
			if side_a == 0 or side_b == 0 or side_c == 0:
				return "Not a side_ange"
			if side_a == side_b and side_b == side_c:
				return "Equilateral"
			if side_a != side_b:
				if side_a in (side_c, side_b):
					return "Isoceles"
				if pow(side_a, 2) + pow(side_b, 2) == pow(side_c, 2):
					return "Right"
				if side_a != side_c:
					return "Scalene"

def runClassifyside_angle(side_a, side_b, side_c):
    """ invoke classifyside_angle with the specified arguments and print the result """
    print('classify_side_angle(', side_a, ', ', side_b, ', ', side_c, ')=', classify_side_angle(side_a, side_b, side_c), sep="")

class Testside_angles(unittest.TestCase):
    def testSet1(self): # test invalid inputs
        self.assertEqual(classify_side_angle(3, 4, 5), 'Right', '3, 4, 5 is a Right side_angle')
        self.assertEqual(classify_side_angle('hello', 1, 2), 'Invalid entries. Please try again', 'hello, 1, 2 Invalid entries. Please try again')
        self.assertNotEqual(classify_side_angle(1, 2, 3), 'Isoceles', 'Should be Scalene')
        self.assertNotEqual(classify_side_angle(0, 0, 0), 'Equilateral', 'Should be Not a side_ange')
    def testMyTestSet2(self):
        self.assertEqual(classify_side_angle(1, 1, 1), 'Equilateral', '1, 1, 1 should be equilateral')
        self.assertNotEqual(classify_side_angle(10, 10, 10), 'Isoceles', 'Should be Equilateral')
        self.assertEqual(classify_side_angle(10, 15, 30), 'Scalene', 'Should be Isoceles')

if __name__ == '__main__':
    # examples of running the code
    runClassifyside_angle(1, 2, 3)
    runClassifyside_angle(1, 1, 1)
    runClassifyside_angle(0, 0, 0)
    runClassifyside_angle('hello', 1, 2)
    runClassifyside_angle(3, 4, 5)

    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
