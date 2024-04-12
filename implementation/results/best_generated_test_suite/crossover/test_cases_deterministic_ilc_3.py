from cut import *

def test_case_0():
	cut = calorie_intake_calc(208.56,204.97,10,'M',0.24,'E')
	cut.height = 174.85
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.27
	cut.weight = 100.19
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 40
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(151.88,171.88,71,'N',0.05,'N')
	cut.amount_exercise = 'N'
	cut.age = 78
	cut.bodyfat = 0.28

