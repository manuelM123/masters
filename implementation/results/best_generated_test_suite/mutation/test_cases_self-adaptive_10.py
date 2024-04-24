from cut import *

def test_case_0():
	cut = calorie_intake_calc(144.08,206.05,69,'M',0.16,'E')
	cut.age = 17
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	cut.bodyfat = 0.03

def test_case_1():
	cut = calorie_intake_calc(106.75,181.42,45,'M',0.03,'M')
	cut.bodyfat = 0.25
	cut.bodyfat = 0.19
	cut.height = 209.99
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 110.83

def test_case_2():
	cut = calorie_intake_calc(159.48,167.3,77,'N',0.25,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'

def test_case_3():
	cut = calorie_intake_calc(84.49,170.95,55,'F',0.09,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 201.04
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(115.3,216.37,57,'N',0.12,'M')
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 100.0
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	cut.gender = 'N'

def test_case_5():
	cut = calorie_intake_calc(175.27,197.08,77,'F',0.24,'S')
	cut.height = 146.68
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.03
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_6():
	cut = calorie_intake_calc(58.32,203.39,55,'M',0.01,'L')
	cut.weight = 94.5
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 57
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.3
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 40

