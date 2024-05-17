from cut import *

def test_case_0():
	cut = calorie_intake_calc(135.44,220.83,16,'M',0.79,'E')
	cut.gender = 'F'
	cut.bodyfat = -0.17
	cut.bodyfat = -0.43
	cut.amount_exercise = 'L'

def test_case_1():
	cut = calorie_intake_calc(179.16,205.92,41,'F',-0.4,'E')
	cut.gender = 'M'
	cut.height = 183.24
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	cut.height = 196.74
	cut.bodyfat = 0.08
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

