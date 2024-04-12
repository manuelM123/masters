from cut import *

def test_case_0():
	cut = calorie_intake_calc(71.14,154.3,10,'M',0.16,'L')
	cut.height = 173.67
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.22
	cut.height = 216.67
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.1
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(94.93,204.04,78,'F',0.01,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 181.11
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 43
	cut.gender = 'F'

