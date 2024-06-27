from cut import *

def test_case_0():
	cut = calorie_intake_calc(182.87,166.14,7,'M',0.69,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'

def test_case_1():
	cut = calorie_intake_calc(56.2,213.18,56,'M',0.08,'M')
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(129.48,144.63,11,'F',0.04,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 10

def test_case_3():
	cut = calorie_intake_calc(47.79,197.33,36,'F',-0.33,'M')
	cut.weight = 93.24
	result_tdee_calculation = cut.tdee_calculation()

