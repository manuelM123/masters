from cut import *

def test_case_0():
	cut = calorie_intake_calc(67.9,140.88,58,'F',0.01,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.05
	cut.age = 51
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(82.63,169.72,10,'M',0.22,'V')
	cut.height = 162.84
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

