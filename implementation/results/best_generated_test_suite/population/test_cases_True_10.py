from cut import *

def test_case_0():
	cut = calorie_intake_calc(170.26,156.93,40,'N',0.17,'E')
	cut.amount_exercise = 'V'
	cut.height = 146.34
	cut.weight = 131.49

def test_case_1():
	cut = calorie_intake_calc(204.78,211.42,11,'F',0.06,'S')
	cut.bodyfat = 0.09
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 23
	cut.gender = 'F'
	cut.amount_exercise = 'L'
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(210.15,202.66,21,'N',0.29,'S')
	cut.amount_exercise = 'E'
	cut.age = 58
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 40
	cut.age = 48

def test_case_3():
	cut = calorie_intake_calc(62.36,174.3,12,'M',0.03,'M')
	cut.gender = 'F'
	cut.height = 207.76
	cut.gender = 'F'
	cut.weight = 155.78
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	cut.height = 220.66

def test_case_4():
	cut = calorie_intake_calc(147.64,215.29,77,'M',0.15,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.18

def test_case_5():
	cut = calorie_intake_calc(206.04,176.6,38,'M',0.2,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.17
	cut.weight = 205.16
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_6():
	cut = calorie_intake_calc(176.29,203.91,33,'F',0.21,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_7():
	cut = calorie_intake_calc(130.34,173.93,45,'F',0.26,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 218.44
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_8():
	cut = calorie_intake_calc(147.75,185.93,47,'N',0.15,'N')
	cut.gender = 'M'
	cut.amount_exercise = 'E'
	cut.height = 186.83
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.08

def test_case_9():
	cut = calorie_intake_calc(75.84,157.38,35,'F',0.27,'L')

