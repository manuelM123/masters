from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.26,153.2,25,'M',0.21,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 75
	cut.amount_exercise = 'N'

def test_case_1():
	cut = calorie_intake_calc(94.8,140.94,14,'F',0.18,'V')
	cut.height = 220.64
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(99.76,156.83,55,'M',0.08,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'

def test_case_3():
	cut = calorie_intake_calc(202.06,150.36,53,'M',0.07,'S')
	cut.height = 204.97
	cut.bodyfat = 0.29
	cut.weight = 111.19
	cut.weight = 177.23
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(117.43,200.27,71,'F',0.14,'V')
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 146.05
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 62.02

