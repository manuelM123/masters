from cut import *

def test_case_0():
	cut = calorie_intake_calc(123.65,171.62,49,'F',0.07,'E')

def test_case_1():
	cut = calorie_intake_calc(156.3,198.29,59,'F',0.22,'L')
	cut.bodyfat = 0.24
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(72.78,144.17,15,'M',0.24,'V')
	cut.bodyfat = 0.0
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 21
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 173.68
	cut.age = 59
	cut.gender = 'N'

