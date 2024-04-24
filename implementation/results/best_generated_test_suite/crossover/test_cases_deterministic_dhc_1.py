from cut import *

def test_case_0():
	cut = calorie_intake_calc(144.08,206.05,69,'M',0.16,'E')
	cut.age = 17
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	cut.bodyfat = 0.03

def test_case_1():
	cut = calorie_intake_calc(54.68,180.65,19,'M',0.28,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(70.98,203.57,26,'M',0.17,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.24

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

