from cut import *

def test_case_0():
	cut = calorie_intake_calc(97.3,198.46,36,'M',0.17,'M')
	cut.age = 31
	cut.gender = 'F'
	cut.gender = 'N'
	cut.bodyfat = 0.17
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	cut.gender = 'F'
	cut.bodyfat = 0.26
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(103.87,144.47,76,'M',0.03,'S')
	cut.amount_exercise = 'L'
	cut.height = 161.96
	cut.weight = 110.1
	cut.height = 219.14
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 199.6
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'

def test_case_2():
	cut = calorie_intake_calc(141.82,175.07,27,'N',0.09,'V')
	cut.amount_exercise = 'M'
	cut.weight = 122.5
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 173.78
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.04

def test_case_3():
	cut = calorie_intake_calc(210.1,201.57,78,'N',0.03,'M')
	cut.height = 161.97
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.28

def test_case_4():
	cut = calorie_intake_calc(135.72,163.13,76,'F',0.19,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 178.66
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 183.58
	cut.weight = 180.56
	cut.amount_exercise = 'M'

def test_case_5():
	cut = calorie_intake_calc(181.47,163.43,18,'M',0.14,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_6():
	cut = calorie_intake_calc(153.19,215.44,61,'N',0.25,'M')
	cut.amount_exercise = 'S'

def test_case_7():
	cut = calorie_intake_calc(189.14,200.82,61,'F',0.02,'L')
	cut.age = 52
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 23
	cut.weight = 81.61
	cut.age = 33

def test_case_8():
	cut = calorie_intake_calc(87.54,193.93,57,'F',0.29,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 79.23
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.29
	cut.age = 81
	cut.age = 72
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 79
	cut.age = 59

