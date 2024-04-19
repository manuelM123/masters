from cut import *

def test_case_0():
	cut = calorie_intake_calc(144.06,150.74,28,'N',0.03,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.0
	cut.age = 37
	cut.height = 184.94
	cut.weight = 71.99
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(58.33,151.46,21,'M',0.06,'E')
	cut.age = 78
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.26
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 108.86

def test_case_2():
	cut = calorie_intake_calc(176.46,178.35,21,'M',0.12,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	cut.gender = 'M'
	cut.weight = 147.84
	cut.age = 39
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 30
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(178.55,211.08,59,'M',0.12,'N')
	cut.height = 217.37
	cut.bodyfat = 0.14
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 78
	cut.amount_exercise = 'N'
	cut.weight = 98.07
	cut.age = 44

def test_case_4():
	cut = calorie_intake_calc(105.64,212.24,59,'F',0.01,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 181.64
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(41.56,144.68,50,'M',0.15,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	cut.age = 25
	cut.age = 16
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_6():
	cut = calorie_intake_calc(91.9,145.27,48,'F',0.24,'L')
	cut.amount_exercise = 'S'
	cut.gender = 'N'

def test_case_7():
	cut = calorie_intake_calc(142.25,220.06,21,'N',0.17,'L')
	cut.weight = 48.7
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.weight = 48.12

