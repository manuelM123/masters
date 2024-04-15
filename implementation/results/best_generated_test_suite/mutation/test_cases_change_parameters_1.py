from cut import *

def test_case_0():
	cut = calorie_intake_calc(169.07,197.8,16,'M',0.21,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(41.34,180.41,71,'M',0.27,'V')
	cut.bodyfat = 0.07

