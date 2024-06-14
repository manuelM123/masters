from cut import *

def test_case_0():
	cut = calorie_intake_calc(190.54,148.81,62,'M',0.77,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(162.87,208.49,65,'M',-0.35,'S')
	cut.age = 33
	result_determine_calorie_intake = cut.determine_calorie_intake()

