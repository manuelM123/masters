from cut import *

def test_case_0():
	cut = calorie_intake_calc(77.72,208.26,75,'N',0.22,'V')
	cut.gender = 'F'
	cut.age = 43

def test_case_1():
	cut = calorie_intake_calc(176.59,163.48,21,'N',0.22,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.26
	cut.bodyfat = 0.12
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(82.97,207.22,75,'F',0.05,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 12

