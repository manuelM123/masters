from cut import *

def test_case_0():
	cut = calorie_intake_calc(210.02,214.89,55,'N',0.1,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(203.12,140.12,48,'M',0.08,'N')

