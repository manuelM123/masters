from cut import *

def test_case_0():
	cut = calorie_intake_calc(143.61,205.96,34,'F',0.28,'V')
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 203.1
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(198.08,213.11,77,'M',0.27,'L')
	cut.weight = 153.9
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.age = 40
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 204.65

def test_case_2():
	cut = calorie_intake_calc(155.05,161.27,44,'F',0.2,'E')
	cut.age = 24
	cut.height = 161.38
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 197.12

def test_case_3():
	cut = calorie_intake_calc(121.37,167.3,24,'M',0.14,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 67
	cut.bodyfat = 0.17
	cut.weight = 151.71
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.bodyfat = 0.24

