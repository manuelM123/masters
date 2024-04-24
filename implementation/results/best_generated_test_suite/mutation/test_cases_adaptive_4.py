from cut import *

def test_case_0():
	cut = calorie_intake_calc(177.85,220.91,48,'N',0.24,'E')

def test_case_1():
	cut = calorie_intake_calc(151.44,201.52,61,'N',0.14,'S')
	cut.bodyfat = 0.14
	cut.amount_exercise = 'L'
	cut.gender = 'M'

def test_case_2():
	cut = calorie_intake_calc(185.16,218.78,42,'M',0.09,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 160.25
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 218.09

def test_case_3():
	cut = calorie_intake_calc(156.0,187.98,61,'F',0.29,'L')
	cut.weight = 50.39
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(124.76,144.83,74,'F',0.21,'E')
	cut.height = 163.27
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.age = 18
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.16
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.14
	cut.gender = 'M'

