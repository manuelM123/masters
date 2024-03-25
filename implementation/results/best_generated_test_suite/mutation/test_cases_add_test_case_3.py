from cut import *

def test_case_0():
	cut = calorie_intake_calc(126.81,204.62,46,'F',0.04,'N')
	cut.amount_exercise = 'E'

def test_case_1():
	cut = calorie_intake_calc(118.96,194.06,33,'M',0.24,'E')

def test_case_2():
	cut = calorie_intake_calc(195.22,174.58,58,'M',0.17,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 151.46
	cut.weight = 189.12

