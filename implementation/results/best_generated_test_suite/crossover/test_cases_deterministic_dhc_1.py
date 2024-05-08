from cut import *

def test_case_0():
	cut = calorie_intake_calc(86.3,208.27,38,'N',0.51,'L')

def test_case_1():
	cut = calorie_intake_calc(60.11,175.5,11,'F',0.01,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.45
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 141.18
	cut.bodyfat = 0.48
	cut.gender = 'F'
	cut.weight = 187.73

def test_case_2():
	cut = calorie_intake_calc(80.78,174.86,69,'M',0.04,'E')
	cut.weight = 129.03
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.5
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 185.12
	cut.age = 58
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

