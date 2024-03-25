from cut import *

def test_case_0():
	cut = calorie_intake_calc(206.2,178.24,32,'M',0.27,'S')
	cut.gender = 'M'
	cut.amount_exercise = 'V'
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(200.22,197.68,25,'N',0.12,'E')
	cut.gender = 'F'
	cut.bodyfat = 0.16
	cut.age = 30
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	cut.weight = 58.59
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.12
	cut.bodyfat = 0.14
	cut.bodyfat = 0.15

def test_case_2():
	cut = calorie_intake_calc(158.34,211.52,35,'M',0.01,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 28
	cut.amount_exercise = 'M'
	cut.age = 58
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.01
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(50.27,176.06,60,'N',0.21,'N')
	cut.amount_exercise = 'L'
	cut.height = 169.86
	cut.bodyfat = 0.13
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 42

