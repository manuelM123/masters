from cut import *

def test_case_0():
	cut = calorie_intake_calc(74.51,207.17,45,'N',0.08,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 184.22
	cut.amount_exercise = 'S'

def test_case_1():
	cut = calorie_intake_calc(184.38,165.51,37,'M',0.18,'E')
	cut.gender = 'F'
	cut.weight = 191.11
	result_determine_calorie_intake = cut.determine_calorie_intake()

