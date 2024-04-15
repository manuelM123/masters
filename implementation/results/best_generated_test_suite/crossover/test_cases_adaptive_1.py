from cut import *

def test_case_0():
	cut = calorie_intake_calc(166.69,200.75,74,'N',0.22,'M')
	cut.weight = 131.69
	cut.height = 149.83

def test_case_1():
	cut = calorie_intake_calc(148.09,183.7,46,'M',0.19,'E')
	result_tdee_calculation = cut.tdee_calculation()

