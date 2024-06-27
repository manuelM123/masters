from cut import *

def test_case_0():
	cut = calorie_intake_calc(47.32,144.93,44,'N',0.35,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 153.72
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(86.08,173.56,51,'F',0.43,'S')
	cut.gender = 'F'

def test_case_2():
	cut = calorie_intake_calc(191.96,138.0,67,'F',0.49,'S')
	cut.age = 71
	cut.amount_exercise = 'V'

def test_case_3():
	cut = calorie_intake_calc(47.79,197.33,36,'F',-0.33,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

