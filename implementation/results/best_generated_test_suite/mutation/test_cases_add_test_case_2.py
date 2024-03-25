from cut import *

def test_case_0():
	cut = calorie_intake_calc(173.04,207.16,47,'N',0.24,'N')
	cut.age = 53
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 35
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(210.33,148.11,12,'M',0.22,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	cut.age = 45
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.13

def test_case_2():
	cut = calorie_intake_calc(67.98,172.49,20,'M',0.24,'M')
	cut.weight = 193.69
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 207.16
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

