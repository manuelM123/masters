from cut import *

def test_case_0():
	cut = calorie_intake_calc(104.53,169.33,24,'F',0.35,'L')
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.bodyfat = 0.7
	cut.height = 220.43

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(168.21,185.35,27,'M',-0.2,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.41
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 82
	cut.gender = 'F'
	cut.bodyfat = -0.37
	cut.gender = 'F'
	cut.amount_exercise = 'M'

def test_case_3():
	cut = calorie_intake_calc(59.76,154.99,62,'M',0.24,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(209.19,146.24,51,'M',-0.41,'V')
	cut.height = 137.2
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.47

def test_case_5():
	cut = calorie_intake_calc(200.76,165.03,49,'M',0.03,'L')
	cut.age = 77
	cut.height = 173.76
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 202.88
	cut.weight = 59.03
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 64

def test_case_6():
	cut = calorie_intake_calc(155.23,176.12,5,'N',-0.23,'L')
	cut.bodyfat = -0.27
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 197.87
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_7():
	cut = calorie_intake_calc(164.28,152.98,24,'M',0.07,'V')

