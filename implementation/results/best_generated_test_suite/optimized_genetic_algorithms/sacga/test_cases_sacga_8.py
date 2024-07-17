from cut import *

def test_case_0():
	cut = calorie_intake_calc(74.08,196.64,48,'M',-0.46,'S')
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 224.72

def test_case_1():
	cut = calorie_intake_calc(173.62,147.3,7,'N',0.28,'E')
	cut.bodyfat = -0.25

def test_case_2():
	cut = calorie_intake_calc(153.95,219.0,45,'M',-0.31,'M')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(138.46,174.47,70,'N',0.29,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'

def test_case_4():
	cut = calorie_intake_calc(124.79,158.45,73,'N',0.25,'N')
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 162.34
	cut.age = 16

def test_case_5():
	cut = calorie_intake_calc(58.38,171.01,77,'N',0.56,'V')

def test_case_6():
	cut = calorie_intake_calc(88.66,142.96,51,'F',-0.25,'N')
	cut.weight = 77.22
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 188.41

def test_case_7():
	cut = calorie_intake_calc(99.94,140.01,49,'N',-0.14,'L')
	cut.weight = 213.75
	cut.bodyfat = -0.48
	cut.age = 54

def test_case_8():
	cut = calorie_intake_calc(95.29,164.48,78,'M',0.29,'E')

def test_case_9():
	cut = calorie_intake_calc(204.7,166.48,43,'M',0.75,'N')
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.76
	result_tdee_calculation = cut.tdee_calculation()

def test_case_10():
	cut = calorie_intake_calc(99.16,186.03,24,'F',-0.16,'V')
	cut.height = 164.03
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

