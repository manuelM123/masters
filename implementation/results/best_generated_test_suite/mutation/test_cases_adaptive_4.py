from cut import *

def test_case_0():
	cut = calorie_intake_calc(149.46,186.75,76,'M',-0.35,'V')

def test_case_1():
	cut = calorie_intake_calc(64.17,171.44,32,'F',0.08,'E')
	cut.bodyfat = -0.02
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 193.3
	cut.gender = 'M'
	cut.age = 56

