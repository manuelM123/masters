from cut import *

def test_case_0():
	cut = calorie_intake_calc(116.69,222.4,39,'M',0.79,'E')
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 124.81
	cut.gender = 'N'
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.08
	cut.bodyfat = 0.14
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.4

def test_case_1():
	cut = calorie_intake_calc(78.89,187.12,55,'N',-0.36,'N')
	cut.age = 47
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(74.34,224.56,19,'F',0.24,'S')
	cut.age = 44
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 91.02

def test_case_3():
	cut = calorie_intake_calc(42.63,224.96,50,'M',0.41,'M')
	cut.gender = 'N'
	cut.amount_exercise = 'E'
	cut.weight = 89.56
	cut.amount_exercise = 'N'

def test_case_4():
	cut = calorie_intake_calc(118.02,214.33,82,'N',0.46,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.weight = 129.74
	cut.age = 5

def test_case_5():
	cut = calorie_intake_calc(202.92,159.86,29,'M',0.64,'E')
	cut.age = 64
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

