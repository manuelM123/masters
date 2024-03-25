from cut import *

def test_case_0():
	cut = calorie_intake_calc(140.72,146.19,71,'M',0.08,'V')
	cut.weight = 166.37
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(209.99,161.05,20,'F',0.16,'M')
	cut.bodyfat = 0.2
	cut.height = 175.91
	cut.weight = 68.61
	cut.weight = 92.49

def test_case_2():
	cut = calorie_intake_calc(125.71,162.95,56,'N',0.06,'L')
	cut.bodyfat = 0.29
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 203.06
	cut.weight = 161.11
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(185.43,199.3,40,'M',0.28,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 154.28
	cut.height = 145.48
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.19
	cut.weight = 146.87
	cut.weight = 192.15
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

