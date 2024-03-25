from cut import *

def test_case_0():
	cut = calorie_intake_calc(123.75,182.41,54,'M',0.12,'N')
	cut.bodyfat = 0.12
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.2
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(54.36,184.78,58,'M',0.0,'S')
	cut.age = 22
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 151.44
	cut.weight = 154.33
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(194.56,216.32,35,'F',0.04,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 55.21
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'L'

def test_case_3():
	cut = calorie_intake_calc(151.6,214.18,18,'N',0.06,'L')
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 209.82
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.19
	cut.age = 42
	cut.amount_exercise = 'E'

