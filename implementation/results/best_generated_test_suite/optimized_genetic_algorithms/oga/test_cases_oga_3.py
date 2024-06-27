from cut import *

def test_case_0():
	cut = calorie_intake_calc(204.89,168.32,14,'F',-0.23,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.73

def test_case_1():
	cut = calorie_intake_calc(48.39,211.2,63,'F',0.19,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(194.99,150.97,50,'M',-0.03,'M')
	cut.height = 163.54
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(165.35,137.24,56,'F',0.46,'V')
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(195.42,150.74,40,'F',0.68,'V')
	cut.bodyfat = -0.34
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 165.18

