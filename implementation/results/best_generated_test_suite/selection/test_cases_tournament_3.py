from cut import *

def test_case_0():
	cut = calorie_intake_calc(184.04,191.49,31,'N',0.04,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 37
	cut.age = 42
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(187.75,158.22,59,'F',0.17,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(40.63,215.38,11,'F',0.22,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 194.43
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 61.93
	cut.height = 166.06
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(144.91,188.7,20,'N',0.28,'V')

