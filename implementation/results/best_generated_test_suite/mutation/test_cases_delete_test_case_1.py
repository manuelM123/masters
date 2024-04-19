from cut import *

def test_case_0():
	cut = calorie_intake_calc(41.17,196.07,26,'M',0.18,'N')
	cut.amount_exercise = 'S'
	cut.height = 215.41
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.height = 198.46
	cut.gender = 'M'
	cut.bodyfat = 0.04
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(188.66,207.17,41,'M',0.17,'E')
	cut.height = 162.86
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 163.17
	cut.age = 75
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.13
	cut.weight = 90.39
	cut.bodyfat = 0.29
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(183.67,190.97,67,'N',0.06,'M')
	cut.bodyfat = 0.05
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 121.38
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.age = 63

def test_case_3():
	cut = calorie_intake_calc(70.12,220.23,76,'F',0.05,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 79
	cut.gender = 'M'

def test_case_4():
	cut = calorie_intake_calc(161.94,190.42,62,'N',0.14,'M')
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.3

def test_case_5():
	cut = calorie_intake_calc(181.9,216.51,62,'M',0.17,'N')
	cut.weight = 170.4
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(125.49,144.61,23,'F',0.18,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 152.9

def test_case_7():
	cut = calorie_intake_calc(176.49,156.1,15,'F',0.3,'M')

