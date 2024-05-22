from cut import *

def test_case_0():
	cut = calorie_intake_calc(72.58,162.74,19,'F',0.23,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.03
	cut.height = 182.21
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(129.39,200.26,44,'F',0.3,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 132.65
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(148.64,188.21,28,'N',0.43,'V')
	cut.height = 180.32

def test_case_3():
	cut = calorie_intake_calc(177.18,196.12,25,'F',-0.11,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.62

def test_case_4():
	cut = calorie_intake_calc(177.18,196.12,25,'F',-0.11,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.62

def test_case_5():
	cut = calorie_intake_calc(191.87,221.82,64,'N',0.48,'L')
	cut.weight = 155.2
	cut.height = 168.97
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 94.36

