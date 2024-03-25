from cut import *

def test_case_0():
	cut = calorie_intake_calc(86.96,172.06,56,'F',0.18,'E')
	cut.height = 209.31
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 16
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(65.88,198.22,32,'F',0.09,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(168.77,162.06,14,'F',0.08,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(199.63,165.96,53,'N',0.03,'L')
	cut.age = 20
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 41
	cut.age = 56
	cut.age = 23
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(175.55,214.23,62,'F',0.2,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 177.83
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'

