from cut import *

def test_case_0():
	cut = calorie_intake_calc(149.8,158.66,22,'F',0.27,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	cut.age = 60

def test_case_1():
	cut = calorie_intake_calc(175.52,146.04,45,'M',0.04,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.04
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 25
	cut.height = 140.19
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(197.01,194.49,37,'M',0.01,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

