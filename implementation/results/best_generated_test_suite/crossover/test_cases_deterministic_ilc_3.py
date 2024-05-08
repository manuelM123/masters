from cut import *

def test_case_0():
	cut = calorie_intake_calc(159.59,188.95,62,'M',0.13,'M')

def test_case_1():
	cut = calorie_intake_calc(149.14,141.17,36,'M',0.66,'N')
	cut.height = 209.65
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.6
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'

def test_case_2():
	cut = calorie_intake_calc(77.96,173.04,60,'F',0.01,'N')

def test_case_3():
	cut = calorie_intake_calc(54.89,197.25,10,'M',0.59,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.bodyfat = 0.43

def test_case_4():
	cut = calorie_intake_calc(74.74,185.44,35,'M',0.43,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 51
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.08
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(70.72,172.92,15,'N',-0.5,'S')
	cut.height = 222.12
	cut.weight = 188.43
	cut.age = 21
	cut.age = 65
	cut.amount_exercise = 'N'

def test_case_6():
	cut = calorie_intake_calc(195.76,211.64,33,'M',-0.13,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 13
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'
	cut.age = 45
	cut.age = 76

def test_case_7():
	cut = calorie_intake_calc(82.16,208.4,58,'N',0.12,'E')
	cut.amount_exercise = 'L'

def test_case_8():
	cut = calorie_intake_calc(71.42,175.94,19,'M',0.77,'N')
	cut.age = 37
	cut.weight = 203.06
	cut.weight = 50.29
	cut.height = 164.13
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.21
	cut.gender = 'F'
	cut.age = 27

def test_case_9():
	cut = calorie_intake_calc(191.51,164.08,53,'N',-0.02,'N')
	cut.weight = 104.48
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.height = 182.01
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 58
	result_determine_calorie_intake = cut.determine_calorie_intake()

