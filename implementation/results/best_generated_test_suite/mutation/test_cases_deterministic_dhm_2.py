from cut import *

def test_case_0():
	cut = calorie_intake_calc(94.87,186.11,6,'N',0.05,'E')
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 125.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 57
	cut.weight = 99.81

def test_case_1():
	cut = calorie_intake_calc(62.42,190.47,69,'F',0.34,'M')
	cut.bodyfat = -0.31
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(149.77,212.14,73,'F',-0.11,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 9
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	cut.weight = 87.47

def test_case_3():
	cut = calorie_intake_calc(67.14,191.12,69,'M',-0.32,'N')
	cut.height = 179.98
	cut.height = 171.98
	cut.bodyfat = 0.73
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(78.22,155.87,78,'M',0.06,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.07
	cut.bodyfat = -0.06
	cut.age = 54
	cut.age = 83
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.11
	cut.gender = 'F'
	cut.gender = 'N'

def test_case_5():
	cut = calorie_intake_calc(200.76,177.96,7,'N',-0.03,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 183.27
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_6():
	cut = calorie_intake_calc(168.58,171.62,74,'F',-0.26,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_7():
	cut = calorie_intake_calc(140.6,157.81,33,'F',-0.32,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 149.38
	cut.gender = 'M'
	cut.weight = 194.4
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 214.19

def test_case_8():
	cut = calorie_intake_calc(111.48,169.49,39,'N',-0.47,'V')
	cut.weight = 182.87
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

