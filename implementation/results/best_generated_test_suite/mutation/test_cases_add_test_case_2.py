from cut import *

def test_case_0():
	cut = calorie_intake_calc(40.53,206.11,28,'M',0.42,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.43
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 137.75
	cut.amount_exercise = 'L'
	cut.weight = 64.34

def test_case_1():
	cut = calorie_intake_calc(117.22,192.18,20,'N',0.65,'N')
	cut.weight = 59.96
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(182.46,183.02,34,'F',-0.02,'N')

def test_case_3():
	cut = calorie_intake_calc(111.84,196.11,49,'M',-0.42,'V')
	cut.weight = 152.16
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()

