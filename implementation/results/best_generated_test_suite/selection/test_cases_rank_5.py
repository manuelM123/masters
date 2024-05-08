from cut import *

def test_case_0():
	cut = calorie_intake_calc(139.05,135.39,55,'N',0.56,'V')

def test_case_1():
	cut = calorie_intake_calc(108.21,152.86,11,'F',0.01,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.45
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 99.7
	cut.bodyfat = 0.48
	cut.gender = 'F'
	cut.gender = 'F'

def test_case_2():
	cut = calorie_intake_calc(173.78,211.02,7,'N',-0.42,'E')
	cut.age = 5
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 185.12
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'

def test_case_3():
	cut = calorie_intake_calc(82.09,166.1,76,'M',-0.09,'E')
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.height = 199.85
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 139.54
	cut.height = 144.46

def test_case_4():
	cut = calorie_intake_calc(71.49,171.8,71,'M',-0.14,'E')
	cut.bodyfat = -0.18
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 200.78
	cut.height = 186.76
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(90.29,180.15,60,'F',0.09,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_6():
	cut = calorie_intake_calc(142.58,179.57,62,'M',-0.19,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 191.17
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 171.48
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

