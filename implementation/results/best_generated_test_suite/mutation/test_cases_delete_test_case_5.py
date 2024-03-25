from cut import *

def test_case_0():
	cut = calorie_intake_calc(99.22,174.05,58,'F',0.24,'L')
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 220.68
	cut.bodyfat = 0.06
	cut.height = 142.84
	cut.bodyfat = 0.13
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 62.62

def test_case_1():
	cut = calorie_intake_calc(175.47,210.15,16,'M',0.03,'M')
	cut.age = 47
	cut.weight = 187.91
	cut.gender = 'F'
	cut.age = 20
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 165.51
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(126.39,144.75,70,'M',0.16,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.01

