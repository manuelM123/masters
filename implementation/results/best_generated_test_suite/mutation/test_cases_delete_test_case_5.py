from cut import *

def test_case_0():
	cut = calorie_intake_calc(196.64,163.7,53,'F',0.02,'E')
	cut.gender = 'M'
	cut.age = 74
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 64
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(176.29,201.97,32,'F',0.22,'M')
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(47.96,185.27,56,'F',0.08,'S')
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 47

def test_case_3():
	cut = calorie_intake_calc(130.39,162.08,16,'F',0.09,'S')
	cut.gender = 'M'
	cut.age = 61
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	cut.weight = 76.48
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(176.51,162.47,53,'F',0.21,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'

