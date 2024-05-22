from cut import *

def test_case_0():
	cut = calorie_intake_calc(110.33,163.96,10,'N',0.19,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.29
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.09

def test_case_1():
	cut = calorie_intake_calc(50.68,220.4,12,'F',0.31,'V')
	cut.height = 213.47
	cut.bodyfat = 0.4
	cut.weight = 181.66
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 67.68
	cut.height = 196.77
	cut.age = 48

def test_case_2():
	cut = calorie_intake_calc(184.31,164.02,76,'F',0.24,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 96.89
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.2
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 171.25
	cut.age = 12
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(175.81,142.48,31,'M',-0.22,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 44
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.age = 44

def test_case_4():
	cut = calorie_intake_calc(192.02,212.67,48,'F',0.09,'M')
	cut.bodyfat = 0.4

def test_case_5():
	cut = calorie_intake_calc(213.01,141.42,78,'M',-0.4,'N')
	cut.weight = 203.13
	cut.height = 182.54
	cut.bodyfat = -0.35
	cut.weight = 104.35
	cut.gender = 'N'
	cut.age = 33
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_6():
	cut = calorie_intake_calc(127.0,183.44,13,'M',-0.39,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 7
	cut.gender = 'M'
	cut.weight = 135.64
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()

