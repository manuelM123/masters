from cut import *

def test_case_0():
	cut = calorie_intake_calc(82.67,166.62,75,'N',0.29,'M')
	cut.age = 66
	cut.bodyfat = 0.05
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 169.04
	cut.weight = 90.85
	cut.height = 187.31
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(145.49,220.24,72,'F',0.17,'M')
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 205.86
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(141.65,203.16,49,'F',0.08,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 161.81
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 199.77

def test_case_3():
	cut = calorie_intake_calc(165.26,158.52,73,'M',0.26,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 117.27
	cut.weight = 179.9
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 126.88
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 189.15

