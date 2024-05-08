from cut import *

def test_case_0():
	cut = calorie_intake_calc(106.5,207.96,13,'M',0.17,'E')
	cut.height = 212.05
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.48
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 64
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(176.36,217.66,30,'M',0.23,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 5
	cut.age = 13
	cut.bodyfat = -0.46
	cut.age = 74
	cut.age = 24

def test_case_2():
	cut = calorie_intake_calc(83.82,215.54,22,'M',-0.5,'E')
	result_tdee_calculation = cut.tdee_calculation()

