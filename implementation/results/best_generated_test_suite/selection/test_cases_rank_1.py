from cut import *

def test_case_0():
	cut = calorie_intake_calc(47.79,146.84,43,'F',0.1,'E')
	cut.age = 40

def test_case_1():
	cut = calorie_intake_calc(146.53,210.5,29,'M',0.25,'S')
	cut.age = 77
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 197.23
	cut.weight = 110.44
	cut.height = 191.84
	cut.bodyfat = 0.02

def test_case_2():
	cut = calorie_intake_calc(124.44,164.26,43,'F',0.21,'L')
	cut.age = 47
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(66.91,215.26,16,'N',0.18,'L')
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.07
	cut.gender = 'F'

def test_case_4():
	cut = calorie_intake_calc(112.2,149.91,43,'M',0.15,'V')
	cut.bodyfat = 0.04
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 54
	cut.bodyfat = 0.25
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

