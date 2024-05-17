from cut import *

def test_case_0():
	cut = calorie_intake_calc(186.7,158.12,12,'M',0.17,'V')
	cut.weight = 206.01

def test_case_1():
	cut = calorie_intake_calc(82.0,168.49,52,'F',-0.45,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(144.78,217.97,18,'M',0.46,'V')
	cut.bodyfat = 0.05
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.34
	cut.amount_exercise = 'E'

def test_case_3():
	cut = calorie_intake_calc(199.2,156.31,76,'N',-0.05,'L')

def test_case_4():
	cut = calorie_intake_calc(189.36,155.04,24,'M',-0.41,'E')
	cut.height = 164.6
	cut.weight = 138.68
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 150.94
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.age = 25
	cut.height = 149.79
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_5():
	cut = calorie_intake_calc(80.21,168.59,53,'M',-0.38,'V')
	cut.height = 220.41
	cut.bodyfat = 0.68
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 55
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 193.81

