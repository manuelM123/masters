from cut import *

def test_case_0():
	cut = calorie_intake_calc(96.63,224.45,64,'M',0.41,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.06
	cut.height = 212.02
	cut.weight = 72.08
	cut.amount_exercise = 'N'
	cut.age = 83
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(151.07,152.17,27,'M',-0.32,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.18
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(73.48,189.35,58,'M',0.74,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 15

def test_case_3():
	cut = calorie_intake_calc(111.34,178.77,58,'M',-0.0,'V')
	cut.weight = 71.12

def test_case_4():
	cut = calorie_intake_calc(127.8,173.24,10,'F',0.15,'M')
	cut.weight = 94.6
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'

def test_case_5():
	cut = calorie_intake_calc(171.04,169.65,51,'N',0.47,'S')
	cut.bodyfat = 0.48
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.06
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	cut.gender = 'M'
	cut.amount_exercise = 'N'
	cut.gender = 'N'

