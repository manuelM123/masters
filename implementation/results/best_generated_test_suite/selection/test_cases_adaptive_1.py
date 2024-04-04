from cut import *

def test_case_0():
	cut = calorie_intake_calc(145.02,208.23,19,'N',0.3,'S')
	cut.amount_exercise = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(44.26,218.38,30,'F',0.08,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(49.44,204.94,45,'M',0.07,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()

