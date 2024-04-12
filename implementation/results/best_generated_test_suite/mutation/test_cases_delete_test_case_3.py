from cut import *

def test_case_0():
	cut = calorie_intake_calc(167.19,163.17,27,'M',0.04,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.14
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 146.47
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.15

def test_case_1():
	cut = calorie_intake_calc(55.87,215.63,66,'N',0.14,'L')
	cut.weight = 148.29
	cut.weight = 135.96

def test_case_2():
	cut = calorie_intake_calc(210.52,171.31,34,'M',0.05,'V')
	cut.height = 164.95
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 181.42
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 173.14
	cut.age = 49
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.bodyfat = 0.1
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(62.81,182.87,12,'M',0.04,'S')
	cut.age = 45
	cut.weight = 119.46
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.15
	cut.bodyfat = 0.14
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'

