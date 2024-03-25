from cut import *

def test_case_0():
	cut = calorie_intake_calc(50.36,195.05,81,'M',0.28,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.weight = 176.08
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 83.65

def test_case_1():
	cut = calorie_intake_calc(119.2,169.72,74,'F',0.08,'E')
	cut.bodyfat = 0.03
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 158.57
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 169.8
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(177.66,203.06,10,'N',0.12,'N')
	cut.weight = 199.65
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.bodyfat = 0.19

