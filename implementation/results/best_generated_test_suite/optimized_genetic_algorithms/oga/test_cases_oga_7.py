from cut import *

def test_case_0():
	cut = calorie_intake_calc(133.65,141.8,36,'M',-0.49,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 83

def test_case_1():
	cut = calorie_intake_calc(163.31,189.98,46,'M',0.5,'S')

def test_case_2():
	cut = calorie_intake_calc(35.77,165.45,56,'M',-0.2,'M')
	cut.gender = 'F'
	cut.gender = 'N'
	cut.weight = 187.57

def test_case_3():
	cut = calorie_intake_calc(110.51,167.8,24,'M',0.11,'L')
	cut.height = 145.16
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(114.99,194.88,5,'F',0.44,'L')

