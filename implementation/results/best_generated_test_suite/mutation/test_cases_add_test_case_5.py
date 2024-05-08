from cut import *

def test_case_0():
	cut = calorie_intake_calc(161.56,220.98,68,'N',0.72,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(139.24,213.07,83,'N',0.41,'V')
	cut.gender = 'F'
	cut.age = 50
	cut.age = 42
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(83.18,148.12,19,'F',0.12,'M')
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 163.43
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(130.44,217.59,49,'N',-0.18,'V')
	cut.height = 155.32
	cut.height = 145.15
	cut.bodyfat = -0.14
	cut.gender = 'N'
	cut.gender = 'F'

def test_case_4():
	cut = calorie_intake_calc(146.4,167.15,78,'M',-0.12,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

