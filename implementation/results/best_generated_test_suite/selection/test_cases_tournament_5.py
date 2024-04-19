from cut import *

def test_case_0():
	cut = calorie_intake_calc(149.71,190.76,32,'N',0.02,'M')
	cut.height = 206.15
	cut.gender = 'N'
	cut.amount_exercise = 'N'
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(54.68,180.65,19,'M',0.28,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'

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
	cut = calorie_intake_calc(112.78,166.05,36,'N',0.17,'M')
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 73.86
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'

