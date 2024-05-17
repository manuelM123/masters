from cut import *

def test_case_0():
	cut = calorie_intake_calc(90.6,166.02,47,'F',0.05,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'

def test_case_1():
	cut = calorie_intake_calc(191.13,157.31,33,'F',0.29,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.41
	cut.age = 40
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.height = 181.97
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(125.45,178.39,75,'M',-0.3,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 142.11
	cut.height = 166.02
	cut.weight = 121.05
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 191.1
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 62.38

