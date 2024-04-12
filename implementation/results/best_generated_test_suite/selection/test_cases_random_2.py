from cut import *

def test_case_0():
	cut = calorie_intake_calc(60.67,145.04,51,'F',0.03,'N')
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.16
	cut.amount_exercise = 'L'

def test_case_1():
	cut = calorie_intake_calc(48.47,211.09,70,'M',0.17,'E')
	cut.height = 182.9
	cut.bodyfat = 0.13
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	cut.age = 56
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(62.39,176.05,37,'N',0.26,'L')

def test_case_3():
	cut = calorie_intake_calc(48.79,178.49,50,'M',0.27,'L')
	cut.age = 37
	result_determine_calorie_intake = cut.determine_calorie_intake()

