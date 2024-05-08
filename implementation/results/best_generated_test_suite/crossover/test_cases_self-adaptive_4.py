from cut import *

def test_case_0():
	cut = calorie_intake_calc(187.51,179.44,40,'M',0.18,'L')
	cut.height = 177.97
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	cut.weight = 158.78

def test_case_1():
	cut = calorie_intake_calc(196.04,196.5,80,'F',0.7,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 193.15
	cut.height = 196.77
	cut.bodyfat = 0.64
	cut.bodyfat = 0.38

def test_case_2():
	cut = calorie_intake_calc(166.14,203.07,27,'M',0.28,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 77
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.17
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.22

