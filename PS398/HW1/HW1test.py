import HW1
import unittest

class   TestHw1Code(unittest.TestCase):
  
    def setUp(self):
        return

    def test_one(self):
        self.assertEqual(HW1.shout("hey you"), "HEY YOU!")

    def test_two(self):
        self.assertEqual(HW1.reverse("apples"), "selppa")

    def test_three(self):
        self.assertEqual(HW1.reversewords("apples nom good"),"good nom apples")

    def test_four(self):
        self.assertEqual(HW1.reversewordletters("hey you"),"yeh uoy")

    def test_five(self):
        self.assertEqual(HW1.reversewordletters("one two three four five six seven"), "eno owt eerht ruof evif xis neves")

        #seems that reversewordletters sometiems substracts a word

    def test_six(self):
        self.assertEqual(HW1.reversecassy(
            
        
#finish piglatin 
    
if __name__ == '__main__':
    unittest.main()

#List of bugs: 
    
    # the reversewordletters function also cuts the string short by a     word sometimes

    #the reversewords adds an unecessary period
