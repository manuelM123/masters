from cut import *

def test_case_0():
	cut = calorie_intake_calc(205.28,206.37,70,'M',0.02,'E')

def test_case_1():
	cut = calorie_intake_calc(41.8,199.05,75,'F',0.28,'N')
	cut.age = 78
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(125.87,193.26,29,'M',0.27,'S')
	cut.bodyfat = 0.13
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.07
	result_tdee_calculation = cut.tdee_calculation()

