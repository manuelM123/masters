from cut import *

def test_case_0():
	cut = calorie_intake_calc(177.51,172.68,27,'F',-0.44,'V')
	cut.weight = 131.12
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 126.81
	cut.age = 59
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(172.57,206.42,26,'M',0.62,'V')
	cut.bodyfat = 0.55
	cut.weight = 41.37
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(83.96,191.41,49,'M',-0.41,'S')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(185.61,219.87,42,'N',0.78,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(157.43,219.54,13,'M',-0.11,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 187.96
	cut.weight = 111.82
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 143.84
	cut.bodyfat = -0.11
	cut.height = 149.06
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(199.89,167.07,47,'M',0.18,'S')
	cut.age = 35
	cut.weight = 100.91
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(200.75,224.64,51,'N',-0.28,'S')
	cut.height = 215.99

