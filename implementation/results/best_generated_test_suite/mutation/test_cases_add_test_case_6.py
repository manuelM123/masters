from cut import *

def test_case_0():
	cut = calorie_intake_calc(134.35,144.7,8,'M',-0.43,'L')

def test_case_1():
	cut = calorie_intake_calc(139.24,213.07,83,'N',0.41,'V')
	cut.gender = 'F'
	cut.age = 50
	cut.age = 42
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(74.7,201.94,52,'F',-0.04,'L')
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 38
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 74
	cut.amount_exercise = 'M'
	cut.age = 35
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(126.63,177.3,61,'F',0.06,'E')
	cut.bodyfat = -0.16
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.25

