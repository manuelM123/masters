from cut import *

def test_case_0():
	cut = calorie_intake_calc(41.17,196.07,26,'M',0.18,'N')
	cut.amount_exercise = 'S'
	cut.height = 215.41
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.height = 198.46
	cut.gender = 'M'
	cut.bodyfat = 0.04
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(188.66,207.17,41,'M',0.17,'E')
	cut.height = 162.86
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 163.17
	cut.age = 75
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 90.39
	cut.bodyfat = 0.29
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(181.33,168.02,69,'F',0.16,'E')
	cut.height = 184.8
	cut.age = 71

def test_case_3():
	cut = calorie_intake_calc(70.12,220.23,76,'F',0.05,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 79
	cut.gender = 'M'

def test_case_4():
	cut = calorie_intake_calc(208.15,164.69,55,'M',0.03,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 40
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 144.82
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_5():
	cut = calorie_intake_calc(152.54,218.0,61,'N',0.11,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.22
	cut.age = 15
	cut.weight = 58.25
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'
	cut.gender = 'F'

def test_case_6():
	cut = calorie_intake_calc(147.3,156.19,41,'M',0.14,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 44.57
	cut.bodyfat = 0.3
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.weight = 159.6
	cut.weight = 103.9

def test_case_7():
	cut = calorie_intake_calc(143.07,193.18,75,'M',0.25,'S')
	cut.bodyfat = 0.16
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 42

def test_case_8():
	cut = calorie_intake_calc(93.29,151.95,79,'N',0.22,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.height = 180.86
	cut.bodyfat = 0.21

