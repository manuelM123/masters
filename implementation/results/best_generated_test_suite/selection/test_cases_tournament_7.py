from cut import *

def test_case_0():
	cut = calorie_intake_calc(52.1,209.9,17,'F',0.23,'N')
	cut.bodyfat = 0.06
	cut.bodyfat = 0.15
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 29
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	cut.age = 12
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 46

def test_case_1():
	cut = calorie_intake_calc(82.0,216.41,23,'M',0.21,'V')
	cut.height = 192.3
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(84.29,140.16,46,'N',0.16,'V')
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.age = 63
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 77.16
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(183.98,216.26,69,'M',0.01,'S')
	cut.weight = 47.82
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(138.19,209.83,18,'F',0.27,'L')
	cut.age = 26
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(80.84,198.18,14,'M',0.02,'L')
	cut.bodyfat = 0.21
	cut.weight = 49.02
	cut.gender = 'M'
	cut.height = 165.75

def test_case_6():
	cut = calorie_intake_calc(78.37,210.84,51,'N',0.08,'S')
	cut.weight = 111.25
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 114.62
	cut.gender = 'M'
	cut.bodyfat = 0.16

