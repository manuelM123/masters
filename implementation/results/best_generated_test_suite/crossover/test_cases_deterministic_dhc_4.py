from cut import *

def test_case_0():
	cut = calorie_intake_calc(206.24,142.12,77,'M',0.26,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(111.51,177.98,58,'F',0.13,'L')
	cut.height = 207.52
	cut.bodyfat = 0.19

def test_case_2():
	cut = calorie_intake_calc(145.87,211.2,48,'F',0.04,'L')
	cut.age = 81
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 141.96
	cut.bodyfat = 0.14
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 69
	cut.bodyfat = 0.15
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 49.27

def test_case_3():
	cut = calorie_intake_calc(187.48,218.06,33,'M',0.2,'E')
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.23
	cut.bodyfat = 0.26
	cut.weight = 110.31
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

