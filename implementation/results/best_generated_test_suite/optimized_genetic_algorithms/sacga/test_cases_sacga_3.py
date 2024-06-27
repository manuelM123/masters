from cut import *

def test_case_0():
	cut = calorie_intake_calc(39.1,171.28,50,'M',0.56,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(108.19,178.21,5,'N',0.15,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(111.02,152.43,32,'N',-0.1,'L')
	cut.age = 61
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 35

def test_case_3():
	cut = calorie_intake_calc(44.77,202.81,10,'F',-0.49,'S')
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(121.5,161.97,16,'N',0.54,'S')
	cut.age = 21
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_5():
	cut = calorie_intake_calc(182.14,167.86,18,'M',-0.15,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.11
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_6():
	cut = calorie_intake_calc(47.03,135.87,55,'N',-0.21,'S')
	cut.height = 182.54
	cut.bodyfat = -0.44

def test_case_7():
	cut = calorie_intake_calc(175.26,204.76,45,'N',0.62,'M')
	cut.height = 213.87
	cut.weight = 163.32
	cut.age = 62

def test_case_8():
	cut = calorie_intake_calc(126.29,201.07,39,'F',0.67,'S')
	cut.weight = 117.0
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 190.61

def test_case_9():
	cut = calorie_intake_calc(96.3,150.45,40,'M',0.18,'E')
	cut.age = 68
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 183.45

