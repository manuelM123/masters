from cut import *

def test_case_0():
	cut = calorie_intake_calc(56.17,142.4,65,'N',-0.15,'M')
	cut.bodyfat = 0.44

def test_case_1():
	cut = calorie_intake_calc(73.19,163.16,27,'N',0.54,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 60.04
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 201.05
	cut.amount_exercise = 'V'
	cut.weight = 130.58
	cut.bodyfat = 0.18
	cut.height = 211.54

def test_case_2():
	cut = calorie_intake_calc(195.8,169.1,71,'M',0.01,'E')
	cut.weight = 171.28
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(126.96,189.16,46,'F',-0.06,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 40

def test_case_4():
	cut = calorie_intake_calc(129.47,142.93,84,'N',0.19,'M')

def test_case_5():
	cut = calorie_intake_calc(158.93,219.93,78,'N',0.42,'L')

def test_case_6():
	cut = calorie_intake_calc(61.26,163.45,53,'F',0.29,'V')
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_7():
	cut = calorie_intake_calc(158.77,179.81,52,'F',0.51,'E')
	cut.weight = 160.6
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.58
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_8():
	cut = calorie_intake_calc(77.4,220.14,23,'N',0.74,'V')
	cut.bodyfat = -0.37
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 181.46

def test_case_9():
	cut = calorie_intake_calc(112.92,168.78,49,'F',0.17,'N')
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 143.01

