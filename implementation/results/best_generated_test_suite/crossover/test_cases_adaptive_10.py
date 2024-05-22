from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.39,157.64,80,'F',0.15,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 68
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.08
	cut.age = 69
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(129.52,218.33,22,'M',0.56,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(187.41,158.15,60,'M',-0.21,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 199.72
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 15
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 140.11
	cut.age = 55

