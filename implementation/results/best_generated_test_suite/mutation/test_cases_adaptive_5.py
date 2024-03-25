from cut import *

def test_case_0():
	cut = calorie_intake_calc(161.18,170.68,75,'F',0.18,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(47.15,209.28,67,'F',0.06,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.23
	cut.weight = 109.68
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.21

def test_case_2():
	cut = calorie_intake_calc(61.8,182.49,38,'N',0.15,'S')

def test_case_3():
	cut = calorie_intake_calc(106.65,213.39,41,'N',0.19,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 62
	cut.gender = 'F'
	cut.height = 170.06
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'

def test_case_4():
	cut = calorie_intake_calc(118.1,214.65,60,'M',0.27,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 17
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 39
	cut.height = 172.91
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.14

