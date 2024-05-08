from cut import *

def test_case_0():
	cut = calorie_intake_calc(39.68,170.51,13,'F',0.77,'E')

def test_case_1():
	cut = calorie_intake_calc(43.15,144.96,67,'N',0.75,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 190.4
	cut.height = 222.1
	cut.age = 82
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(84.97,187.8,37,'M',-0.15,'E')
	cut.bodyfat = -0.41
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.54
	cut.amount_exercise = 'E'
	cut.weight = 173.92
	cut.age = 35
	result_tdee_calculation = cut.tdee_calculation()

