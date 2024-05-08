from cut import *

def test_case_0():
	cut = calorie_intake_calc(86.58,199.82,61,'M',-0.25,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.bodyfat = 0.46
	cut.height = 139.19
	cut.height = 151.46
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(178.67,150.09,29,'N',-0.01,'V')

