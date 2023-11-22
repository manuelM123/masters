from cut import *

def test_case_0():
	cut = calorie_intake_calc(55.16,154.7,71,'M',0.04,'S')
	cut.height = 166.32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 202.39
	cut.weight = 90.38

def test_case_1():
	cut = calorie_intake_calc(95.45,182.62,23,'M',0.15,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'

def test_case_2():
	cut = calorie_intake_calc(61.04,141.08,59,'F',0.16,'E')
	cut.bodyfat = 0.13
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 57

def test_case_3():
	cut = calorie_intake_calc(171.52,158.54,58,'M',0.29,'V')
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.28
	cut.bodyfat = 0.03
	cut.bodyfat = 0.13

