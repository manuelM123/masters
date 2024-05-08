from cut import *

def test_case_0():
	cut = calorie_intake_calc(66.61,199.78,70,'N',-0.31,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	cut.bodyfat = 0.0

def test_case_1():
	cut = calorie_intake_calc(200.97,165.27,67,'M',-0.37,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 10
	cut.weight = 113.92

def test_case_2():
	cut = calorie_intake_calc(90.46,183.12,49,'F',0.28,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.07
	cut.amount_exercise = 'V'
	cut.height = 169.95
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(90.05,193.9,44,'F',0.43,'M')
	cut.weight = 183.82

