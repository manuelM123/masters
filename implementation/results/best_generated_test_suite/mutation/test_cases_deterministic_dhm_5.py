from cut import *

def test_case_0():
	cut = calorie_intake_calc(144.66,208.55,44,'M',0.19,'V')
	cut.amount_exercise = 'S'
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.22
	cut.weight = 193.5
	cut.height = 158.35
	cut.height = 183.66
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'

def test_case_1():
	cut = calorie_intake_calc(75.59,203.63,13,'N',0.06,'M')
	cut.bodyfat = 0.08
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 187.0
	cut.weight = 195.7
	cut.bodyfat = 0.2
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'

def test_case_2():
	cut = calorie_intake_calc(82.29,189.71,20,'N',0.27,'V')
	cut.weight = 163.02
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.19
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.21
	cut.weight = 101.99

def test_case_3():
	cut = calorie_intake_calc(117.65,178.03,24,'M',0.03,'N')
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 55
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 194.76

def test_case_4():
	cut = calorie_intake_calc(182.38,140.57,16,'N',0.04,'M')
	cut.bodyfat = 0.06
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'S'
	cut.weight = 66.01

def test_case_5():
	cut = calorie_intake_calc(193.86,184.5,76,'F',0.26,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 177.63
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 24
	cut.age = 78
	cut.bodyfat = 0.02

def test_case_6():
	cut = calorie_intake_calc(60.6,209.52,43,'F',0.26,'V')
	cut.weight = 150.3
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.3

def test_case_7():
	cut = calorie_intake_calc(86.78,204.21,73,'M',0.28,'M')
	cut.height = 188.98
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 165.29
	cut.weight = 152.75
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_8():
	cut = calorie_intake_calc(156.31,169.61,61,'F',0.02,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.01
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 204.8
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.amount_exercise = 'M'
	cut.weight = 191.09
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 128.65

