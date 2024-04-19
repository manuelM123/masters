from cut import *

def test_case_0():
	cut = calorie_intake_calc(153.04,196.71,10,'F',0.13,'L')
	cut.age = 31
	cut.gender = 'F'
	cut.gender = 'N'
	cut.bodyfat = 0.17
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	cut.weight = 102.89
	cut.bodyfat = 0.26
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(198.96,208.52,31,'F',0.29,'M')
	cut.gender = 'N'
	cut.bodyfat = 0.15

def test_case_2():
	cut = calorie_intake_calc(177.0,173.03,21,'F',0.08,'L')
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.04

def test_case_3():
	cut = calorie_intake_calc(210.1,201.57,78,'N',0.03,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.bodyfat = 0.28

def test_case_4():
	cut = calorie_intake_calc(135.72,163.13,76,'F',0.19,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 178.66
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 105.66

def test_case_5():
	cut = calorie_intake_calc(109.96,195.73,31,'N',0.28,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 164.46

def test_case_6():
	cut = calorie_intake_calc(193.87,211.12,18,'F',0.29,'M')
	cut.gender = 'N'

def test_case_7():
	cut = calorie_intake_calc(207.83,160.77,72,'F',0.13,'E')
	cut.age = 52
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.height = 179.07
	result_tdee_calculation = cut.tdee_calculation()

def test_case_8():
	cut = calorie_intake_calc(87.54,193.93,57,'F',0.29,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 166.59
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.29
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 72
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 79
	cut.age = 59

def test_case_9():
	cut = calorie_intake_calc(94.36,200.4,10,'N',0.19,'S')
	cut.bodyfat = 0.26
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 34
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

