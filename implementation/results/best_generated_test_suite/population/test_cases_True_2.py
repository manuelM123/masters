from cut import *

def test_case_0():
	cut = calorie_intake_calc(166.27,168.01,76,'F',0.01,'V')
	cut.height = 207.43
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(114.17,207.31,28,'M',0.08,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 180.91

