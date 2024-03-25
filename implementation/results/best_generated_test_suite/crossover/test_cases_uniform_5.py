from cut import *

def test_case_0():
	cut = calorie_intake_calc(109.39,164.59,79,'M',0.26,'N')
	cut.height = 208.54
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.21
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.17
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(140.98,155.21,24,'N',0.22,'E')
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 214.08
	cut.amount_exercise = 'V'

def test_case_2():
	cut = calorie_intake_calc(152.49,171.35,54,'M',0.25,'E')
	cut.weight = 143.22
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 49
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	cut.age = 65

