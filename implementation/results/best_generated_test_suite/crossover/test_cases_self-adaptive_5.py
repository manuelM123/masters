from cut import *

def test_case_0():
	cut = calorie_intake_calc(149.71,190.76,32,'N',0.02,'M')
	cut.height = 206.15
	cut.gender = 'N'
	cut.amount_exercise = 'N'
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(188.66,207.17,41,'M',0.17,'E')
	cut.height = 162.86
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 147.8
	cut.age = 75
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.13
	cut.weight = 90.39
	cut.bodyfat = 0.29
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(204.48,220.43,80,'F',0.03,'E')
	cut.bodyfat = 0.27
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(194.72,168.24,45,'F',0.09,'E')
	cut.amount_exercise = 'S'
	cut.weight = 72.73
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.25
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 175.39

def test_case_4():
	cut = calorie_intake_calc(208.15,164.69,55,'M',0.03,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 40
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 144.82
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_5():
	cut = calorie_intake_calc(207.12,158.4,59,'M',0.23,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.12
	cut.bodyfat = 0.15

def test_case_6():
	cut = calorie_intake_calc(184.05,156.56,65,'F',0.07,'N')
	cut.age = 13
	cut.height = 172.0
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.22
	cut.height = 158.98
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.02

def test_case_7():
	cut = calorie_intake_calc(156.13,212.23,26,'N',0.24,'N')

