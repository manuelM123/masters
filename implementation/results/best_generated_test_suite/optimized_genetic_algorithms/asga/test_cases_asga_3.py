from cut import *

def test_case_0():
	cut = calorie_intake_calc(119.43,168.08,50,'F',0.22,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 117.65

def test_case_1():
	cut = calorie_intake_calc(199.52,194.04,14,'M',-0.24,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.47
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

