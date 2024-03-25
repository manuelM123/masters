from cut import *

def test_case_0():
	cut = calorie_intake_calc(120.55,210.1,49,'F',0.06,'E')
	cut.bodyfat = 0.09
	cut.gender = 'N'
	cut.bodyfat = 0.02
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 187.74
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(74.06,176.69,19,'M',0.16,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(81.79,180.49,37,'M',0.17,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 97.85
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.2
	cut.height = 155.14
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

