from cut import *

def test_case_0():
	cut = calorie_intake_calc(79.96,167.84,31,'M',-0.41,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 195.86
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'L'
	cut.weight = 75.52

def test_case_1():
	cut = calorie_intake_calc(89.47,216.08,6,'F',-0.01,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.height = 213.81
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 163.66
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 163.02

