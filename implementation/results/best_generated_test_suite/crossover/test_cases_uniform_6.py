from cut import *

def test_case_0():
	cut = calorie_intake_calc(72.33,146.42,80,'M',-0.12,'L')
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(119.54,190.45,9,'M',0.21,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

