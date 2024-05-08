from cut import *

def test_case_0():
	cut = calorie_intake_calc(203.05,204.76,50,'M',-0.21,'N')

def test_case_1():
	cut = calorie_intake_calc(66.23,180.05,28,'N',0.02,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 159.35

