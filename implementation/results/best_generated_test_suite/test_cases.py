from cut import *

def test_case_0():
	cut = calorie_intake_calc(128.18,195.1,71,'M',0.11,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.bodyfat = 0.26
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 52.03
	cut.amount_exercise = 'V'
	cut.weight = 136.27
	cut.bodyfat = -0.4
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(123.84,189.38,12,'M',0.7,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(184.81,169.73,20,'M',-0.29,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(111.37,175.96,25,'N',-0.45,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.48
	cut.weight = 43.94
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(205.98,137.37,71,'N',0.14,'L')
	cut.gender = 'N'
	cut.height = 152.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 150.19

def test_case_5():
	cut = calorie_intake_calc(75.99,199.54,83,'M',0.74,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 46
	cut.bodyfat = 0.07
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'
	cut.weight = 200.04
	cut.gender = 'F'

