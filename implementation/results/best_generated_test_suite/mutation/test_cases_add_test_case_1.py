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
	cut = calorie_intake_calc(129.39,200.26,44,'F',0.3,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 178.53
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(37.98,144.17,32,'F',0.39,'S')
	cut.bodyfat = 0.28
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 75
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 207.11
	cut.bodyfat = 0.46

def test_case_3():
	cut = calorie_intake_calc(102.67,147.57,5,'F',0.48,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'

def test_case_4():
	cut = calorie_intake_calc(171.75,150.25,45,'F',-0.48,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.38
	cut.bodyfat = -0.01
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(152.25,183.79,14,'F',-0.46,'S')
	cut.weight = 177.82
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.gender = 'M'
	cut.weight = 143.47

def test_case_6():
	cut = calorie_intake_calc(97.46,221.5,78,'M',-0.37,'S')
	cut.bodyfat = 0.62
	cut.age = 80
	cut.gender = 'N'
	cut.amount_exercise = 'N'
	cut.height = 147.13

def test_case_7():
	cut = calorie_intake_calc(39.99,220.25,53,'M',-0.33,'N')

def test_case_8():
	cut = calorie_intake_calc(176.79,154.55,60,'N',-0.31,'V')
	cut.age = 60
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 150.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_9():
	cut = calorie_intake_calc(93.32,168.49,75,'F',0.11,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 173.6
	cut.weight = 72.35
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 77
	cut.weight = 42.75
	cut.weight = 113.08

