from cut import *

def test_case_0():
	cut = calorie_intake_calc(145.9,161.8,41,'M',0.51,'L')

def test_case_1():
	cut = calorie_intake_calc(82.0,168.49,52,'F',-0.45,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(60.64,142.91,74,'M',0.19,'L')
	cut.bodyfat = -0.15
	cut.weight = 48.37
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 135.27
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'

