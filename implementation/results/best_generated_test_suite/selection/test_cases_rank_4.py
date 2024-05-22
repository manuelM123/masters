from cut import *

def test_case_0():
	cut = calorie_intake_calc(53.53,192.85,82,'N',0.22,'M')
	cut.amount_exercise = 'N'
	cut.age = 71

def test_case_1():
	cut = calorie_intake_calc(129.39,200.26,44,'F',0.3,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 178.53
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(71.87,178.85,36,'M',-0.33,'V')
	cut.gender = 'M'
	cut.amount_exercise = 'E'
	cut.height = 173.88
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 171.14
	cut.age = 15
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.19
	result_determine_calorie_intake = cut.determine_calorie_intake()

