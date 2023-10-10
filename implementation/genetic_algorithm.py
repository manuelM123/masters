from cut import *
import utilities as util
from solution import *

class_test = calorie_intake_calc(83.9,189,22,'M',None,'S')

test_suite = Solution()
print("Constructor: " + str(test_suite.generate_constructor(util.read_metadata("metadata.json"))))
print("------------------------------------------")
print("Functions: " + str(test_suite.generate_other_functions(util.read_metadata("metadata.json"))))