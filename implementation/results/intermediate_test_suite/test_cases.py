from cut import *

def test_case_0():
	cut = calorie_intake_calc(100.19,163.2,71,'M',0.16,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(173.94,196.52,13,'F',0.3,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

