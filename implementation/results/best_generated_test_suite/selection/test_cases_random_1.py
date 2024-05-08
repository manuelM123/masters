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
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 212.97
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(159.17,203.5,71,'M',0.35,'E')
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 208.12
	cut.bodyfat = 0.51
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'
	cut.gender = 'F'

def test_case_3():
	cut = calorie_intake_calc(183.45,186.26,43,'F',0.79,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 10
	cut.height = 138.46
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 164.51

def test_case_4():
	cut = calorie_intake_calc(58.97,212.46,38,'N',-0.36,'E')

def test_case_5():
	cut = calorie_intake_calc(198.03,135.41,35,'M',-0.15,'N')
	cut.height = 166.14
	cut.amount_exercise = 'L'
	cut.height = 200.76
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	cut.gender = 'M'
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.63
	result_determine_calorie_intake = cut.determine_calorie_intake()

