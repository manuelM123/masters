from cut import *

def test_case_0():
	cut = calorie_intake_calc(133.3,206.65,32,'M',0.1,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 57
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.24

def test_case_1():
	cut = calorie_intake_calc(140.85,177.36,10,'N',0.21,'L')
	cut.height = 177.49
	cut.age = 54
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 204.38
	cut.age = 36
	cut.bodyfat = 0.24
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(47.49,199.4,30,'M',0.04,'S')
	cut.amount_exercise = 'M'
	cut.age = 16
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 152.56
	cut.height = 175.25
	cut.bodyfat = 0.12

def test_case_3():
	cut = calorie_intake_calc(164.12,149.84,34,'M',0.09,'L')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(193.16,213.33,70,'F',0.01,'M')
	cut.age = 12
	cut.bodyfat = 0.15
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'L'
	cut.height = 160.21
	result_tdee_calculation = cut.tdee_calculation()

def test_case_5():
	cut = calorie_intake_calc(186.21,185.99,45,'M',0.16,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.age = 20
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 50.67
	result_tdee_calculation = cut.tdee_calculation()

