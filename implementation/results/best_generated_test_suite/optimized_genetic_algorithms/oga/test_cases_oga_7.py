from cut import *

def test_case_0():
	cut = calorie_intake_calc(63.88,153.01,78,'F',0.38,'N')
	cut.height = 205.74
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(200.81,142.33,13,'M',-0.05,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.bodyfat = -0.28
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(161.88,175.88,27,'M',0.11,'E')
	cut.gender = 'F'
	cut.amount_exercise = 'L'
	cut.height = 202.49
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(114.83,173.61,71,'M',0.04,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(103.86,199.95,58,'F',-0.46,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 161.59

