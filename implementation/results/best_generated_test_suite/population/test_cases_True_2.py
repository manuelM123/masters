from cut import *

def test_case_0():
	cut = calorie_intake_calc(139.04,204.32,24,'N',0.13,'M')
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(153.58,155.44,58,'M',0.06,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

