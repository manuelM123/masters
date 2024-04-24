from cut import *

def test_case_0():
	cut = calorie_intake_calc(149.83,144.41,65,'F',0.04,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 212.85
	cut.weight = 155.59

def test_case_1():
	cut = calorie_intake_calc(207.99,157.96,50,'M',0.02,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(147.98,209.82,16,'F',0.09,'N')
	cut.bodyfat = 0.15
	cut.bodyfat = 0.07
	cut.height = 140.08
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 10
	cut.amount_exercise = 'E'
	cut.weight = 194.95
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(52.09,161.82,65,'M',0.17,'N')
	cut.gender = 'N'
	cut.weight = 150.34
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 195.14
	cut.bodyfat = 0.03
	cut.gender = 'M'
	cut.age = 14
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(188.21,213.56,53,'N',0.03,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.02
	cut.weight = 157.06
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_5():
	cut = calorie_intake_calc(98.7,192.92,16,'F',0.22,'L')

def test_case_6():
	cut = calorie_intake_calc(128.55,148.01,47,'M',0.24,'L')
	cut.height = 198.29
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 97.3
	cut.age = 55
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 35

def test_case_7():
	cut = calorie_intake_calc(149.6,209.94,46,'M',0.13,'N')
	cut.age = 48
	cut.weight = 51.43
	cut.height = 187.73
	cut.weight = 184.78
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'V'
	cut.weight = 90.68
	cut.gender = 'F'
	cut.bodyfat = 0.03

def test_case_8():
	cut = calorie_intake_calc(139.11,159.32,60,'M',0.13,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

