from cut import *

def test_case_0():
	cut = calorie_intake_calc(172.03,177.92,53,'F',0.25,'M')
	cut.age = 44
	cut.height = 148.99
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	cut.weight = 157.84
	cut.age = 55
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 195.14

def test_case_1():
	cut = calorie_intake_calc(208.22,192.2,17,'F',0.06,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.weight = 74.72
	cut.amount_exercise = 'M'
	cut.bodyfat = 0.07
	cut.gender = 'N'
	cut.age = 50
	cut.amount_exercise = 'M'
	cut.age = 73
	cut.age = 19

def test_case_2():
	cut = calorie_intake_calc(86.09,217.14,33,'M',0.11,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.07
	cut.age = 39
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(120.75,159.5,68,'M',0.11,'M')
	cut.age = 38

def test_case_4():
	cut = calorie_intake_calc(129.65,170.7,16,'M',0.28,'S')
	cut.weight = 146.86
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'E'
	cut.age = 74
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.05

