from cut import *

def test_case_0():
	cut = calorie_intake_calc(118.31,188.6,67,'M',-0.34,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(150.17,191.32,36,'F',-0.32,'M')
	cut.bodyfat = -0.04
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'
	cut.weight = 106.09
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 182.82
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(133.51,167.59,64,'F',-0.36,'S')
	cut.age = 71
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.bodyfat = -0.41
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 60.77
	cut.weight = 35.59
	cut.bodyfat = 0.67
	cut.height = 176.83

