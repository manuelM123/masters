from cut import *

def test_case_0():
	cut = calorie_intake_calc(199.63,217.59,26,'M',0.24,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 43
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(107.26,186.56,35,'N',0.18,'L')
	cut.height = 170.94
	cut.amount_exercise = 'M'
	cut.weight = 80.61
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 19

def test_case_2():
	cut = calorie_intake_calc(131.6,202.09,51,'M',0.16,'E')

def test_case_3():
	cut = calorie_intake_calc(172.1,177.07,31,'N',0.11,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.02
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'

def test_case_4():
	cut = calorie_intake_calc(193.99,204.06,48,'M',0.01,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.weight = 147.47
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 167.98
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	cut.gender = 'N'

