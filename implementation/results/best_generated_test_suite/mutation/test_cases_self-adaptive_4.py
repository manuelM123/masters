from cut import *

def test_case_0():
	cut = calorie_intake_calc(53.01,189.95,58,'F',0.07,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 55
	cut.amount_exercise = 'L'
	cut.height = 220.8
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(49.9,161.44,11,'M',0.17,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.08
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(96.01,197.28,20,'M',0.07,'M')
	cut.weight = 110.3
	cut.age = 28
	cut.height = 142.72
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.26
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 62.7

def test_case_3():
	cut = calorie_intake_calc(117.15,142.43,79,'N',0.27,'L')
	cut.age = 45
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.29
	cut.height = 147.58
	cut.weight = 89.4
	cut.amount_exercise = 'E'

