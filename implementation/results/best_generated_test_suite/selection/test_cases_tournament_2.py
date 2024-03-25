from cut import *

def test_case_0():
	cut = calorie_intake_calc(147.77,158.13,45,'F',0.3,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 217.41
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(94.29,165.52,68,'M',0.05,'V')
	cut.weight = 206.57
	cut.height = 201.32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 141.35
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(92.26,159.55,48,'M',0.2,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.weight = 107.6

