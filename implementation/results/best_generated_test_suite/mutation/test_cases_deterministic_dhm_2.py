from cut import *

def test_case_0():
	cut = calorie_intake_calc(103.21,213.38,10,'M',0.62,'S')

def test_case_1():
	cut = calorie_intake_calc(183.13,196.58,38,'F',-0.35,'N')

def test_case_2():
	cut = calorie_intake_calc(180.25,165.61,13,'M',-0.42,'E')
	cut.weight = 129.39
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.0
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 194.71
	cut.bodyfat = 0.05

