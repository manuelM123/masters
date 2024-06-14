from cut import *

def test_case_0():
	cut = calorie_intake_calc(181.34,155.69,20,'F',0.56,'E')

def test_case_1():
	cut = calorie_intake_calc(162.87,208.49,65,'M',-0.35,'S')
	cut.age = 33
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(69.72,210.88,53,'M',0.14,'S')
	cut.height = 189.31
	cut.amount_exercise = 'M'

