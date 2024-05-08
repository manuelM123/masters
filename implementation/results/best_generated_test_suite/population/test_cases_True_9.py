from cut import *

def test_case_0():
	cut = calorie_intake_calc(109.3,184.35,70,'M',0.28,'S')
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 211.72
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(39.67,180.9,20,'N',0.8,'E')
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(133.99,188.24,70,'F',-0.44,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 67
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

def test_case_3():
	cut = calorie_intake_calc(109.36,202.91,76,'N',0.78,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 206.49
	cut.age = 17
	cut.age = 47
	cut.bodyfat = 0.04
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(142.79,182.6,63,'M',0.31,'S')
	cut.height = 220.51

def test_case_5():
	cut = calorie_intake_calc(181.23,192.83,78,'N',0.63,'V')
	cut.weight = 98.3
	cut.bodyfat = 0.64
	cut.amount_exercise = 'M'
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.47
	cut.bodyfat = 0.19
	cut.amount_exercise = 'L'
	cut.bodyfat = -0.09

def test_case_6():
	cut = calorie_intake_calc(206.19,207.84,49,'N',0.22,'V')
	cut.height = 202.76
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 219.54
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 77.52
	cut.bodyfat = 0.04

def test_case_7():
	cut = calorie_intake_calc(163.55,188.47,17,'M',-0.09,'M')
	cut.height = 202.2
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.height = 145.7
	cut.bodyfat = -0.17

def test_case_8():
	cut = calorie_intake_calc(45.73,183.05,65,'N',0.67,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 136.22

def test_case_9():
	cut = calorie_intake_calc(212.36,143.83,16,'F',0.12,'L')
	cut.bodyfat = 0.38
	cut.weight = 106.6
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 85
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.44

