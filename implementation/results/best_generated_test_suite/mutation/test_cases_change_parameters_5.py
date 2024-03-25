from cut import *

def test_case_0():
	cut = calorie_intake_calc(67.89,148.87,76,'N',0.16,'L')
	cut.weight = 173.24
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'

def test_case_1():
	cut = calorie_intake_calc(123.48,191.05,37,'F',0.12,'L')
	cut.bodyfat = 0.27
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(115.56,195.68,80,'F',0.24,'N')
	cut.weight = 94.33
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 204.94
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 190.71
	cut.height = 183.18

def test_case_3():
	cut = calorie_intake_calc(134.41,152.8,63,'F',0.13,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.02
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.08
	cut.height = 213.5
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(108.51,169.42,19,'M',0.18,'E')
	cut.age = 79
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.gender = 'M'
	cut.weight = 52.13
	cut.weight = 162.53
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

