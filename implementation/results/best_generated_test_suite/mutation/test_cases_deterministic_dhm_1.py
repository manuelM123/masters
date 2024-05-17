from cut import *

def test_case_0():
	cut = calorie_intake_calc(65.33,215.78,59,'M',-0.16,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 50
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 12
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 44.87
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(107.69,179.69,45,'N',0.33,'S')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 31
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.bodyfat = 0.67
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(180.64,181.57,42,'M',-0.4,'S')
	cut.age = 18
	cut.age = 35
	cut.weight = 197.48
	cut.weight = 37.62
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 203.47
	result_determine_calorie_intake = cut.determine_calorie_intake()

