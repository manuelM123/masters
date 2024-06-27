from cut import *

def test_case_0():
	cut = calorie_intake_calc(182.87,166.14,7,'M',0.69,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'

def test_case_1():
	cut = calorie_intake_calc(168.94,224.73,40,'M',0.23,'L')
	cut.age = 44
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(130.06,181.31,36,'F',0.09,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 218.38

def test_case_3():
	cut = calorie_intake_calc(37.04,217.57,54,'M',0.17,'S')

def test_case_4():
	cut = calorie_intake_calc(204.52,139.73,75,'F',0.17,'S')

