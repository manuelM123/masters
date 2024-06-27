from cut import *

def test_case_0():
	cut = calorie_intake_calc(182.87,166.14,7,'M',0.69,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'

def test_case_1():
	cut = calorie_intake_calc(142.51,187.51,66,'M',-0.03,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(130.06,181.31,36,'F',0.09,'E')
	cut.bodyfat = 0.44
	cut.height = 218.38

def test_case_3():
	cut = calorie_intake_calc(37.04,217.57,54,'M',0.17,'S')

