from cut import *

def test_case_0():
	cut = calorie_intake_calc(173.84,211.45,54,'M',-0.31,'S')
	cut.bodyfat = 0.61
	cut.gender = 'M'
	cut.weight = 145.45
	cut.age = 66

def test_case_1():
	cut = calorie_intake_calc(209.19,167.15,13,'M',0.76,'L')
	cut.height = 156.76
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(73.44,172.23,19,'N',0.47,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.69
	cut.weight = 80.92

def test_case_3():
	cut = calorie_intake_calc(142.28,140.23,59,'N',0.68,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(151.41,149.71,45,'M',0.01,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.22
	cut.age = 43
	cut.height = 201.7
	cut.age = 47
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	cut.age = 16
	cut.height = 139.45

