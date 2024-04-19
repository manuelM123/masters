from cut import *

def test_case_0():
	cut = calorie_intake_calc(203.92,149.72,48,'N',0.28,'S')
	cut.height = 159.57
	cut.bodyfat = 0.17
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(147.34,184.44,76,'M',0.07,'M')
	cut.bodyfat = 0.18
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 19
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.24
	cut.gender = 'M'
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(71.66,186.87,40,'M',0.04,'M')
	cut.height = 198.18
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.11
	cut.gender = 'M'

def test_case_3():
	cut = calorie_intake_calc(157.51,193.08,51,'F',0.17,'V')
	cut.bodyfat = 0.29
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	cut.gender = 'N'
	cut.weight = 76.01

def test_case_4():
	cut = calorie_intake_calc(48.0,148.79,45,'F',0.28,'S')
	cut.bodyfat = 0.21
	cut.weight = 144.48
	cut.height = 208.39
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 59
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.21

def test_case_5():
	cut = calorie_intake_calc(95.13,154.15,31,'N',0.28,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 178.66
	cut.height = 155.57
	cut.gender = 'M'

def test_case_6():
	cut = calorie_intake_calc(70.42,144.07,51,'M',0.09,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.17
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 95.72
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'
	cut.bodyfat = 0.02
	cut.gender = 'M'

def test_case_7():
	cut = calorie_intake_calc(153.17,210.09,59,'F',0.29,'L')
	cut.height = 165.37
	cut.age = 63
	cut.amount_exercise = 'L'
	cut.age = 60
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_8():
	cut = calorie_intake_calc(168.39,148.46,64,'M',0.02,'L')
	cut.amount_exercise = 'V'
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.18
	cut.height = 204.76
	cut.age = 28

