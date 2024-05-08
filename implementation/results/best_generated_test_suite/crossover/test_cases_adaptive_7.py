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
	cut = calorie_intake_calc(142.79,145.85,10,'F',0.36,'S')
	cut.height = 149.61
	cut.bodyfat = 0.26
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(130.16,184.59,8,'N',0.4,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'

def test_case_4():
	cut = calorie_intake_calc(58.97,212.46,38,'N',-0.36,'E')

