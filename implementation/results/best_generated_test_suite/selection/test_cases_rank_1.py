from cut import *

def test_case_0():
	cut = calorie_intake_calc(151.01,183.1,73,'N',0.07,'N')

def test_case_1():
	cut = calorie_intake_calc(60.11,175.5,11,'F',0.01,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 141.18
	cut.bodyfat = 0.48
	cut.gender = 'F'
	cut.weight = 187.73

def test_case_2():
	cut = calorie_intake_calc(196.01,135.27,68,'N',-0.19,'V')
	cut.weight = 129.03
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.5
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 185.12
	cut.age = 58
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(174.02,218.91,54,'F',0.29,'L')

def test_case_4():
	cut = calorie_intake_calc(106.18,172.51,9,'F',-0.38,'M')
	cut.amount_exercise = 'N'
	cut.gender = 'M'
	cut.gender = 'N'
	cut.bodyfat = 0.65
	cut.bodyfat = 0.03
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 190.01
	cut.amount_exercise = 'S'
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(135.6,164.81,71,'N',0.45,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.age = 47

def test_case_6():
	cut = calorie_intake_calc(178.07,163.72,34,'M',-0.36,'N')
	cut.amount_exercise = 'V'
	cut.height = 191.17
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 171.48
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_7():
	cut = calorie_intake_calc(141.99,151.52,37,'M',-0.48,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.31
	cut.bodyfat = 0.69
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'

def test_case_8():
	cut = calorie_intake_calc(126.52,184.05,78,'F',0.46,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 56.59

def test_case_9():
	cut = calorie_intake_calc(82.02,167.72,6,'F',-0.24,'E')

