from cut import *

def test_case_0():
	cut = calorie_intake_calc(63.27,206.64,65,'F',0.15,'V')
	cut.amount_exercise = 'N'
	cut.age = 75
	cut.age = 53
	cut.weight = 189.31
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 179.25
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	cut.age = 60

def test_case_1():
	cut = calorie_intake_calc(58.45,204.27,47,'F',0.11,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 110.84
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 207.75
	cut.height = 146.32

def test_case_2():
	cut = calorie_intake_calc(136.1,161.16,27,'M',0.01,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 79

def test_case_3():
	cut = calorie_intake_calc(199.36,208.13,38,'N',0.04,'E')
	cut.gender = 'F'
	cut.bodyfat = 0.06
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	cut.gender = 'M'

