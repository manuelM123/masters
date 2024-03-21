from cut import *

def test_case_0():
	cut = calorie_intake_calc(206.71,202.13,34,'M',0.22,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'

def test_case_1():
	cut = calorie_intake_calc(192.92,195.72,36,'M',0.15,'E')
	cut.height = 154.99
	cut.height = 144.07
	cut.age = 42

def test_case_2():
	cut = calorie_intake_calc(106.61,161.56,46,'N',0.21,'L')
	cut.age = 68
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.16

