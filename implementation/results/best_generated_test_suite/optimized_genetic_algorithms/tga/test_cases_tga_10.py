from cut import *

def test_case_0():
	cut = calorie_intake_calc(70.98,210.25,69,'M',0.19,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'

def test_case_1():
	cut = calorie_intake_calc(56.21,189.68,78,'M',-0.35,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 78.44

def test_case_2():
	cut = calorie_intake_calc(151.01,159.56,52,'F',-0.47,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'
	cut.age = 32

