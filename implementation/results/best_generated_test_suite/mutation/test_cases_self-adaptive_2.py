from cut import *

def test_case_0():
	cut = calorie_intake_calc(152.77,192.23,10,'F',0.21,'S')
	cut.height = 146.4
	cut.gender = 'M'
	cut.height = 211.07
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(144.6,146.12,79,'F',0.17,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 188.65
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 164.32
	cut.bodyfat = 0.11
	cut.gender = 'N'
	cut.bodyfat = 0.22

