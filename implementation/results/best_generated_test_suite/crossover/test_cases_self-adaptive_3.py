from cut import *

def test_case_0():
	cut = calorie_intake_calc(172.17,167.05,48,'N',-0.28,'M')
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 77
	cut.height = 208.12
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

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
	cut = calorie_intake_calc(209.01,210.87,55,'M',0.61,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 172.66
	cut.bodyfat = -0.14
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 219.54
	cut.age = 59

def test_case_3():
	cut = calorie_intake_calc(49.26,171.55,76,'N',0.65,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 176.29

def test_case_4():
	cut = calorie_intake_calc(156.74,165.97,23,'M',0.09,'V')
	cut.weight = 203.03
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 198.42

def test_case_5():
	cut = calorie_intake_calc(84.81,190.84,60,'N',-0.45,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 212.49
	cut.age = 80
	cut.bodyfat = 0.29
	cut.bodyfat = 0.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.amount_exercise = 'V'

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

