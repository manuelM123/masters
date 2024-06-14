from cut import *

def test_case_0():
	cut = calorie_intake_calc(102.28,178.42,18,'M',0.8,'N')
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(162.87,208.49,65,'M',-0.35,'S')
	cut.age = 33
	result_determine_calorie_intake = cut.determine_calorie_intake()

