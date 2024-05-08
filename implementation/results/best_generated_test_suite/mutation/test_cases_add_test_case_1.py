from cut import *

def test_case_0():
	cut = calorie_intake_calc(124.69,220.25,28,'N',-0.31,'M')
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(139.24,213.07,83,'N',0.41,'V')
	cut.gender = 'F'
	cut.age = 50
	cut.age = 42
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(111.31,200.62,55,'M',0.79,'N')

def test_case_3():
	cut = calorie_intake_calc(56.03,146.66,70,'M',0.27,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 17
	cut.weight = 154.61
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 178.16
	cut.weight = 38.82

