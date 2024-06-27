from cut import *

def test_case_0():
	cut = calorie_intake_calc(83.11,209.38,55,'M',0.19,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.73

def test_case_1():
	cut = calorie_intake_calc(200.93,204.58,60,'M',-0.11,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 210.15

