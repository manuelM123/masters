from cut import *

def test_case_0():
	cut = calorie_intake_calc(181.12,152.1,29,'M',0.43,'E')
	cut.age = 59
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 62
	cut.age = 23

def test_case_1():
	cut = calorie_intake_calc(37.36,192.99,49,'F',0.64,'M')
	cut.bodyfat = -0.12
	cut.weight = 87.52
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 169.9
	cut.gender = 'F'

def test_case_2():
	cut = calorie_intake_calc(67.97,202.3,20,'M',0.15,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 59
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(138.08,212.13,27,'N',0.62,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(43.09,170.24,39,'F',-0.09,'L')
	cut.height = 146.64
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'

