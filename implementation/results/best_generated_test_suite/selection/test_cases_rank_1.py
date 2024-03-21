from cut import *

def test_case_0():
	cut = calorie_intake_calc(132.47,205.39,17,'M',0.24,'V')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(137.66,180.93,74,'M',0.05,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.07

def test_case_2():
	cut = calorie_intake_calc(106.36,178.23,49,'N',0.17,'S')

