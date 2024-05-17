from cut import *

def test_case_0():
	cut = calorie_intake_calc(172.17,167.05,48,'N',-0.28,'M')
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 77
	cut.height = 208.12
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(157.04,162.52,47,'F',-0.26,'E')
	cut.age = 13
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(180.9,185.99,45,'M',0.47,'S')
	cut.age = 31
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.32
	cut.age = 52
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(88.7,208.73,72,'N',0.17,'S')
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.height = 157.51
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(66.83,145.86,7,'M',-0.5,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'

def test_case_5():
	cut = calorie_intake_calc(166.2,139.69,68,'M',0.65,'E')
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(166.14,171.09,8,'F',-0.47,'N')
	cut.age = 61
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 134.7
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 73

