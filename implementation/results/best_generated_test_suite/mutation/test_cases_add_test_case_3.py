from cut import *

def test_case_0():
	cut = calorie_intake_calc(45.48,156.24,35,'M',-0.48,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 50.0
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.66
	cut.weight = 38.82
	cut.height = 214.18

def test_case_1():
	cut = calorie_intake_calc(67.79,178.59,28,'N',0.44,'M')
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 142.1

def test_case_2():
	cut = calorie_intake_calc(95.74,157.96,34,'M',-0.03,'V')
	cut.age = 24
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 85
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(169.22,142.88,18,'N',-0.28,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 81
	cut.height = 187.07
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'

def test_case_4():
	cut = calorie_intake_calc(151.7,179.99,72,'M',-0.03,'E')
	cut.bodyfat = 0.29
	cut.bodyfat = 0.02
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_5():
	cut = calorie_intake_calc(68.49,191.44,54,'M',-0.32,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.79
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.weight = 115.97
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.11

def test_case_6():
	cut = calorie_intake_calc(87.03,200.52,29,'F',-0.13,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'

def test_case_7():
	cut = calorie_intake_calc(196.17,150.42,44,'F',0.18,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.24
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_8():
	cut = calorie_intake_calc(210.39,170.65,59,'M',0.75,'L')
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 96.76
	cut.gender = 'N'
	cut.amount_exercise = 'M'

def test_case_9():
	cut = calorie_intake_calc(121.9,143.83,43,'M',-0.27,'L')
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.05

def test_case_10():
	cut = calorie_intake_calc(134.4,141.38,14,'F',-0.12,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	cut.weight = 213.45
	cut.age = 19

def test_case_11():
	cut = calorie_intake_calc(89.76,222.38,7,'M',-0.21,'V')
	cut.amount_exercise = 'V'
	cut.height = 218.03
	cut.gender = 'M'
	cut.bodyfat = -0.18
	result_tdee_calculation = cut.tdee_calculation()

