from cut import *

def test_case_0():
	cut = calorie_intake_calc(87.07,199.93,72,'M',0.11,'E')
	cut.height = 166.32
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(85.88,180.77,80,'N',0.16,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

