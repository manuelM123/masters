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
	cut = calorie_intake_calc(201.93,185.73,26,'F',0.08,'M')
	cut.gender = 'M'
	cut.height = 161.51
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.height = 162.94

def test_case_3():
	cut = calorie_intake_calc(84.49,170.95,55,'F',0.09,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 201.04
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(128.08,198.81,64,'M',0.05,'L')
	cut.age = 41
	cut.gender = 'M'
	cut.gender = 'M'
	cut.height = 198.37
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 57
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.19
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

