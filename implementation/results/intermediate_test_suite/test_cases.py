from cut import *

def test_case_0():
	cut = calorie_intake_calc(65.13,189.7,78,'F',0.29,'S')
	cut.amount_exercise = 'L'

def test_case_1():
	cut = calorie_intake_calc(163.8,148.9,79,'M',0.14,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(83.02,169.88,45,'F',0.17,'S')
	cut.gender = 'M'
	cut.bodyfat = 0.11

def test_case_3():
	cut = calorie_intake_calc(148.0,177.0,13,'N',0.09,'E')
	cut.bodyfat = 0.11

def test_case_4():
	cut = calorie_intake_calc(47.78,154.47,69,'M',0.24,'S')
	cut.height = 184.05

def test_case_5():
	cut = calorie_intake_calc(149.5,210.65,23,'F',0.14,'V')
	result_tdee_calculation = cut.tdee_calculation()

