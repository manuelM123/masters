from cut import *

def test_case_0():
	cut = calorie_intake_calc(57.01,163.62,14,'M',0.46,'M')
	cut.weight = 67.87
	cut.age = 54
	cut.bodyfat = 0.54
	cut.height = 167.09
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 35
	cut.amount_exercise = 'V'

def test_case_1():
	cut = calorie_intake_calc(204.68,216.11,19,'M',-0.45,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 135.35
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 193.86

