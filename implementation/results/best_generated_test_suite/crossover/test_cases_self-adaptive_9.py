from cut import *

def test_case_0():
	cut = calorie_intake_calc(143.12,200.46,63,'N',0.39,'L')
	cut.gender = 'N'
	cut.age = 83
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 220.12
	cut.amount_exercise = 'V'
	cut.age = 53
	cut.gender = 'F'
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 35

def test_case_2():
	cut = calorie_intake_calc(185.1,162.78,45,'F',0.59,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 166.21
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 196.46
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(121.79,198.12,80,'F',0.25,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 167.43
	cut.bodyfat = -0.49
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.2
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(98.65,220.51,39,'N',-0.04,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 204.13
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.1
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_5():
	cut = calorie_intake_calc(174.06,215.28,24,'F',-0.43,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_6():
	cut = calorie_intake_calc(102.32,161.15,12,'F',-0.33,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 170.31
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 106.26
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_7():
	cut = calorie_intake_calc(36.62,221.4,22,'M',0.21,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 82
	cut.age = 10

def test_case_8():
	cut = calorie_intake_calc(44.76,194.89,46,'N',-0.35,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

