from cut import *

def test_case_0():
	cut = calorie_intake_calc(203.06,155.29,72,'F',0.21,'S')
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 133.73
	cut.height = 179.88
	cut.height = 179.43
	cut.bodyfat = 0.21
	cut.age = 15
	cut.height = 168.42

def test_case_1():
	cut = calorie_intake_calc(109.2,170.48,60,'F',0.01,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 157.84
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 122.34
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 170.51
	cut.height = 149.67

def test_case_2():
	cut = calorie_intake_calc(90.49,207.47,50,'F',0.16,'N')
	cut.amount_exercise = 'L'
	cut.age = 48
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(200.22,147.35,49,'F',0.13,'E')

def test_case_4():
	cut = calorie_intake_calc(78.73,154.8,10,'M',0.2,'V')
	cut.age = 21
	cut.gender = 'F'
	cut.weight = 165.3
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	cut.age = 50
	cut.weight = 57.2

