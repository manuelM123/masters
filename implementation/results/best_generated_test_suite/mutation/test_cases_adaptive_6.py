from cut import *

def test_case_0():
	cut = calorie_intake_calc(125.06,173.56,61,'F',-0.21,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	cut.weight = 42.18
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(206.53,180.36,72,'M',-0.5,'E')
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'V'
	cut.age = 40
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()

