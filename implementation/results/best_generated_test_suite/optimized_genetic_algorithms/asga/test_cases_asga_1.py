from cut import *

def test_case_0():
	cut = calorie_intake_calc(152.66,219.91,38,'M',0.11,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'

def test_case_1():
	cut = calorie_intake_calc(55.47,182.85,52,'N',0.32,'N')
	cut.weight = 154.47
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(49.97,171.11,65,'F',-0.49,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.28

def test_case_3():
	cut = calorie_intake_calc(154.05,151.87,79,'M',0.56,'M')

