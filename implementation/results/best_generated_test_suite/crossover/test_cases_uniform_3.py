from cut import *

def test_case_0():
	cut = calorie_intake_calc(172.56,211.56,57,'N',0.27,'S')
	cut.weight = 193.95
	cut.bodyfat = 0.28

def test_case_1():
	cut = calorie_intake_calc(73.72,211.22,28,'M',0.04,'S')
	cut.age = 77
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 197.51
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 151.73
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 56

def test_case_2():
	cut = calorie_intake_calc(105.49,163.83,56,'F',0.08,'S')
	cut.weight = 152.23
	cut.weight = 61.12
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 118.43
	cut.amount_exercise = 'S'
	cut.gender = 'M'
	cut.bodyfat = 0.17
	cut.height = 182.24
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 214.54

def test_case_3():
	cut = calorie_intake_calc(125.04,174.77,61,'N',0.24,'V')
	cut.age = 55
	cut.bodyfat = 0.28
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'

def test_case_4():
	cut = calorie_intake_calc(118.65,181.54,63,'M',0.18,'S')
	cut.weight = 206.54
	cut.bodyfat = 0.24
	cut.bodyfat = 0.09
	cut.bodyfat = 0.22
	cut.height = 183.16
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.15

