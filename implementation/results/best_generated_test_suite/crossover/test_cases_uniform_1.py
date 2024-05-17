from cut import *

def test_case_0():
	cut = calorie_intake_calc(120.97,217.04,70,'M',-0.21,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(207.82,176.65,21,'F',-0.45,'V')
	cut.age = 41
	cut.age = 21
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.6

