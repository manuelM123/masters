from cut import *

def test_case_0():
	cut = calorie_intake_calc(78.11,160.54,61,'F',0.04,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 10
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.28
	cut.age = 48
	cut.bodyfat = 0.1
	cut.bodyfat = 0.26
	cut.weight = 98.63

def test_case_1():
	cut = calorie_intake_calc(173.85,153.43,59,'N',0.17,'V')

def test_case_2():
	cut = calorie_intake_calc(188.41,173.71,39,'M',0.04,'S')
	cut.age = 80
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 37
	cut.height = 186.0
	cut.age = 50
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 155.76
	cut.weight = 175.86

def test_case_3():
	cut = calorie_intake_calc(101.06,197.64,81,'F',0.16,'L')
	cut.height = 142.41
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 208.49
	cut.height = 198.7
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

