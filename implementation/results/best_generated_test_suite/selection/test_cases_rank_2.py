from cut import *

def test_case_0():
	cut = calorie_intake_calc(121.65,217.78,70,'M',0.24,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 50
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 156.37
	cut.height = 148.95
	cut.weight = 186.43
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(73.35,208.36,59,'M',0.06,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 171.02
	cut.height = 157.12
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(160.49,205.18,48,'M',0.26,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.21
	cut.amount_exercise = 'N'

def test_case_3():
	cut = calorie_intake_calc(79.66,205.77,21,'F',0.08,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.29
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 48.07

