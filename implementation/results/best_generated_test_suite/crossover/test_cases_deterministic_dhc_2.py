from cut import *

def test_case_0():
	cut = calorie_intake_calc(162.97,147.68,50,'M',-0.41,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 55
	cut.gender = 'N'
	cut.age = 16
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(173.61,224.66,23,'F',0.79,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 150.63

def test_case_3():
	cut = calorie_intake_calc(78.03,170.43,18,'M',0.05,'L')
	cut.gender = 'F'
	cut.height = 155.48
	cut.weight = 147.99
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

