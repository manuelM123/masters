from cut import *

def test_case_0():
	cut = calorie_intake_calc(84.09,185.37,69,'N',0.15,'E')
	cut.age = 32
	cut.amount_exercise = 'E'
	cut.weight = 85.98

def test_case_1():
	cut = calorie_intake_calc(130.2,202.51,58,'N',0.24,'L')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.21
	cut.bodyfat = 0.01
	cut.weight = 69.49
	cut.bodyfat = 0.06

def test_case_2():
	cut = calorie_intake_calc(190.0,146.74,35,'M',0.05,'L')

def test_case_3():
	cut = calorie_intake_calc(128.13,199.09,74,'M',0.06,'S')
	cut.bodyfat = 0.3
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.bodyfat = 0.26
	cut.age = 31
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(126.6,191.83,53,'F',0.01,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'

