from cut import *

def test_case_0():
	cut = calorie_intake_calc(171.83,153.64,52,'M',-0.11,'M')
	cut.weight = 209.89
	cut.weight = 81.98
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(157.76,150.78,14,'F',-0.21,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.amount_exercise = 'V'
	cut.weight = 37.55

def test_case_2():
	cut = calorie_intake_calc(159.38,207.32,70,'N',0.12,'L')
	cut.weight = 86.23
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	cut.bodyfat = 0.11

def test_case_3():
	cut = calorie_intake_calc(156.55,162.27,26,'M',0.29,'N')
	cut.bodyfat = -0.49
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 7
	cut.age = 82

def test_case_4():
	cut = calorie_intake_calc(112.52,148.28,80,'M',-0.01,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.09
	cut.gender = 'F'
	cut.age = 15
	cut.gender = 'M'

def test_case_5():
	cut = calorie_intake_calc(179.99,174.97,63,'F',-0.11,'M')
	cut.age = 40
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 84
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.37
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(139.91,138.65,50,'M',-0.19,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.0
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_7():
	cut = calorie_intake_calc(67.37,179.79,20,'F',-0.09,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 209.29
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 21
	cut.bodyfat = 0.26

def test_case_8():
	cut = calorie_intake_calc(37.04,184.38,55,'N',-0.19,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 202.13
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 161.52
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.35
	cut.amount_exercise = 'N'

def test_case_9():
	cut = calorie_intake_calc(136.43,148.73,42,'F',0.26,'L')
	cut.age = 26
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 101.27

def test_case_10():
	cut = calorie_intake_calc(190.46,176.8,44,'N',0.39,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_11():
	cut = calorie_intake_calc(97.89,202.74,77,'N',0.2,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.35
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 136.59
	cut.weight = 142.65
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

