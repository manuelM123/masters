from cut import *

def test_case_0():
	cut = calorie_intake_calc(95.79,158.88,36,'M',-0.34,'E')
	cut.height = 220.45
	cut.age = 55
	cut.gender = 'N'
	cut.age = 16
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(140.78,171.49,8,'F',-0.01,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(167.13,188.43,53,'F',-0.24,'L')
	cut.age = 35
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 165.29
	cut.age = 21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.weight = 39.3

def test_case_3():
	cut = calorie_intake_calc(78.03,170.43,18,'M',0.05,'L')
	cut.gender = 'F'
	cut.height = 155.48
	cut.weight = 147.99
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

