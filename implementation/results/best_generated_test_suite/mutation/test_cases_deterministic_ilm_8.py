from cut import *

def test_case_0():
	cut = calorie_intake_calc(86.58,199.82,61,'M',-0.25,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.bodyfat = 0.46
	cut.height = 139.19
	cut.height = 151.46
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(167.72,173.6,8,'F',0.48,'M')
	cut.gender = 'F'
	cut.age = 76
	cut.height = 212.97
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(209.54,219.29,23,'N',-0.33,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 199.03
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 144.77
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(186.99,153.4,72,'M',0.15,'L')

