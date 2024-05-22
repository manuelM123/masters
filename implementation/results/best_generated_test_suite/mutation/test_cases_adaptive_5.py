from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.39,157.64,80,'F',0.15,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 151.11
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 19
	cut.age = 22

def test_case_1():
	cut = calorie_intake_calc(71.87,178.85,36,'M',-0.33,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 162.77
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 171.14
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.19
	cut.age = 55

def test_case_2():
	cut = calorie_intake_calc(95.74,157.96,34,'M',-0.03,'V')
	cut.age = 24
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 85
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(100.64,176.31,53,'M',-0.02,'M')
	cut.bodyfat = -0.23
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 137.16

def test_case_4():
	cut = calorie_intake_calc(195.59,213.47,18,'M',0.36,'M')
	cut.height = 154.66
	cut.amount_exercise = 'S'
	cut.age = 74
	cut.amount_exercise = 'E'

def test_case_5():
	cut = calorie_intake_calc(60.99,199.5,36,'N',-0.42,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 55
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'V'

