from cut import *

def test_case_0():
	cut = calorie_intake_calc(152.61,217.84,60,'M',-0.44,'V')
	cut.weight = 106.24
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.28
	cut.height = 222.02
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.01

def test_case_1():
	cut = calorie_intake_calc(54.42,183.11,44,'N',0.56,'V')
	cut.gender = 'N'
	cut.weight = 38.51
	cut.bodyfat = -0.08
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 182.42
	cut.amount_exercise = 'S'

def test_case_2():
	cut = calorie_intake_calc(53.35,173.58,49,'M',-0.21,'M')
	cut.weight = 212.96
	cut.bodyfat = 0.08
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'
	cut.height = 142.14
	cut.height = 138.36
	cut.weight = 129.98
	cut.bodyfat = 0.06

