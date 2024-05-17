from cut import *

def test_case_0():
	cut = calorie_intake_calc(63.38,220.35,19,'M',0.32,'S')
	cut.age = 25
	cut.bodyfat = -0.25
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.53
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 162.99
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(192.7,177.0,7,'F',-0.36,'V')
	cut.bodyfat = 0.21
	cut.amount_exercise = 'S'
	cut.age = 69
	cut.amount_exercise = 'M'
	cut.gender = 'N'
	cut.weight = 101.06
	cut.bodyfat = 0.16
	cut.bodyfat = -0.1
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(212.39,199.5,72,'M',-0.28,'S')
	cut.amount_exercise = 'M'

def test_case_3():
	cut = calorie_intake_calc(97.37,156.62,57,'M',0.33,'M')
	cut.amount_exercise = 'V'
	cut.weight = 166.25
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 195.01
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'

def test_case_4():
	cut = calorie_intake_calc(133.07,207.43,72,'N',-0.12,'M')
	cut.age = 24

def test_case_5():
	cut = calorie_intake_calc(190.61,167.39,61,'M',-0.13,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 136.57
	cut.gender = 'F'
	cut.height = 186.61
	cut.age = 13
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 48
	cut.weight = 134.83

def test_case_6():
	cut = calorie_intake_calc(153.61,201.03,67,'M',0.14,'M')
	cut.height = 162.49
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 71
	cut.bodyfat = -0.44
	cut.weight = 180.11
	cut.amount_exercise = 'M'
	cut.age = 64

