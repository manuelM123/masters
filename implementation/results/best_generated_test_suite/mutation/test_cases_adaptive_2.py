from cut import *

def test_case_0():
	cut = calorie_intake_calc(166.58,146.82,79,'F',0.15,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 96.41
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(137.89,165.36,45,'F',0.03,'M')
	cut.gender = 'M'
	cut.age = 28

def test_case_2():
	cut = calorie_intake_calc(204.09,175.14,68,'M',0.09,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

