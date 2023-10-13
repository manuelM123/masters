from cut import *
from solution import *
import utilities as util

configuration = util.read_configuration_file("config.ini")
print(configuration)

class_test = calorie_intake_calc(83.9,189,22,'M',None,'S')
metadata = util.read_metadata("metadata.json")
solution = Solution()

#print("Constructor: " + str(solution.generate_constructor(util.read_metadata("metadata.json"))))
#print("------------------------------------------")
#print("Functions: " + str(solution.generate_other_functions(util.read_metadata("metadata.json"))))

print(solution.generate_test_suite(util.read_metadata("metadata.json"), 5, 10))
print("---------------------------------------------------")
util.write_metadata("results/generated_test_cases", solution.generate_test_suite(metadata, 5, 10), metadata)