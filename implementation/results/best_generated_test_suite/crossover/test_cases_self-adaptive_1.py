from cut import *

def test_case_0():
	cut = calorie_intake_calc(157.37,157.65,20,'M',0.28,'E')
	cut.bodyfat = 0.02
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(53.84,170.68,24,'N',0.26,'L')
	cut.gender = 'N'
	cut.age = 70

def test_case_2():
	cut = calorie_intake_calc(207.49,190.56,64,'F',0.11,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(100.12,202.01,11,'M',0.25,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(155.09,185.91,67,'M',0.29,'L')
	cut.age = 57
	cut.height = 161.88
	cut.gender = 'M'

