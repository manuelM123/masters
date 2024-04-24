from cut import *

def test_case_0():
	cut = calorie_intake_calc(167.83,214.16,53,'M',0.29,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(92.39,196.71,73,'N',0.18,'S')
	cut.bodyfat = 0.25

def test_case_2():
	cut = calorie_intake_calc(66.0,179.67,12,'M',0.26,'M')
	cut.weight = 115.89
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 60
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(177.71,198.87,67,'F',0.28,'L')
	cut.height = 161.22
	cut.weight = 112.12
	cut.bodyfat = 0.07
	cut.amount_exercise = 'L'
	cut.bodyfat = 0.06
	cut.bodyfat = 0.27

def test_case_4():
	cut = calorie_intake_calc(172.41,184.3,12,'N',0.13,'E')
	cut.bodyfat = 0.07
	cut.bodyfat = 0.27
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(164.47,140.64,41,'M',0.27,'M')

def test_case_6():
	cut = calorie_intake_calc(124.69,216.69,76,'M',0.15,'E')

def test_case_7():
	cut = calorie_intake_calc(208.47,158.32,14,'M',0.28,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 52.21
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 79.5
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_8():
	cut = calorie_intake_calc(166.35,156.43,64,'F',0.25,'M')
	cut.height = 196.08
	cut.age = 21
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 75
	cut.amount_exercise = 'V'
	cut.height = 185.15

def test_case_9():
	cut = calorie_intake_calc(180.29,188.69,31,'N',0.23,'E')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_10():
	cut = calorie_intake_calc(98.42,219.95,39,'F',0.24,'S')
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 178.69

