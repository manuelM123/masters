from cut import *

def test_case_0():
	cut = calorie_intake_calc(45.27,204.37,80,'F',0.27,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(122.39,141.01,78,'N',0.08,'S')
	cut.height = 162.57
	cut.bodyfat = 0.09
	cut.gender = 'M'
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'V'
	cut.age = 35

def test_case_2():
	cut = calorie_intake_calc(107.78,143.31,27,'F',0.23,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(71.58,166.78,74,'N',0.24,'M')
	cut.weight = 144.53
	cut.gender = 'F'
	cut.weight = 121.73
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 166.48

def test_case_4():
	cut = calorie_intake_calc(41.61,169.12,29,'M',0.04,'L')
	cut.weight = 177.9
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(134.35,148.48,49,'M',0.22,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 192.74
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()

