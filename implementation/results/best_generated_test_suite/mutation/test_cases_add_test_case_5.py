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
	cut = calorie_intake_calc(72.14,218.2,42,'M',0.14,'N')
	cut.amount_exercise = 'L'
	cut.gender = 'N'
	cut.bodyfat = 0.27
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(52.91,217.0,52,'N',0.15,'E')
	cut.age = 14
	cut.height = 218.76
	cut.gender = 'F'

def test_case_5():
	cut = calorie_intake_calc(163.05,172.32,79,'M',0.1,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 195.83
	cut.height = 140.17
	cut.age = 33
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.15
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.22
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

