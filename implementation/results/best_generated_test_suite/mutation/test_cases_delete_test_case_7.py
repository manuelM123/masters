from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.39,157.64,80,'F',0.15,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 194.75
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 151.11
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.08
	cut.age = 69
	cut.age = 22

def test_case_1():
	cut = calorie_intake_calc(181.03,183.69,37,'N',0.63,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'N'
	cut.age = 13
	cut.bodyfat = 0.31
	cut.age = 68

def test_case_2():
	cut = calorie_intake_calc(167.13,188.43,53,'F',-0.24,'L')
	cut.age = 35
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 165.29
	cut.age = 21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 174.15
	cut.weight = 39.3

def test_case_3():
	cut = calorie_intake_calc(43.86,155.68,40,'M',0.6,'V')
	cut.age = 31
	cut.height = 143.3
	cut.bodyfat = -0.16
	cut.weight = 72.67
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 23
	cut.bodyfat = 0.64
	cut.bodyfat = 0.08
	cut.gender = 'M'

