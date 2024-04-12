from cut import *

def test_case_0():
	cut = calorie_intake_calc(203.57,160.75,55,'F',0.2,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(83.75,214.91,74,'M',0.1,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.bodyfat = 0.11
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(177.03,163.8,27,'M',0.09,'L')
	cut.weight = 144.08
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 166.11
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 110.23

def test_case_3():
	cut = calorie_intake_calc(182.32,161.39,46,'F',0.13,'M')
	cut.weight = 49.02
	cut.weight = 104.31
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 196.73
	cut.weight = 75.82
	cut.weight = 153.06
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

