from cut import *

def test_case_0():
	cut = calorie_intake_calc(64.85,182.46,36,'M',-0.3,'V')
	cut.age = 50
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(170.73,203.68,36,'N',0.18,'L')
	cut.age = 52

def test_case_2():
	cut = calorie_intake_calc(67.69,141.52,22,'F',-0.11,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 176.92
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

