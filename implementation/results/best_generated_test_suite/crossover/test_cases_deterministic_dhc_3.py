from cut import *

def test_case_0():
	cut = calorie_intake_calc(118.86,146.69,59,'M',0.53,'L')
	cut.height = 202.42
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 152.25

def test_case_1():
	cut = calorie_intake_calc(152.5,210.23,29,'M',0.04,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 56
	cut.age = 66
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(47.34,166.65,67,'N',0.6,'L')
	cut.gender = 'M'
	cut.age = 69
	cut.amount_exercise = 'N'
	cut.gender = 'M'
	cut.height = 143.81
	cut.amount_exercise = 'E'

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
	cut = calorie_intake_calc(54.89,135.16,5,'M',-0.24,'N')
	cut.gender = 'F'
	cut.bodyfat = -0.27
	cut.age = 41
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.65
	cut.weight = 123.68
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 155.39
	cut.age = 59
	cut.weight = 90.46

def test_case_5():
	cut = calorie_intake_calc(81.3,214.71,63,'N',0.34,'M')
	cut.age = 77
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 112.91
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 52.17

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

def test_case_7():
	cut = calorie_intake_calc(91.1,185.49,17,'N',0.72,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'

def test_case_8():
	cut = calorie_intake_calc(83.87,179.5,70,'N',0.09,'V')

