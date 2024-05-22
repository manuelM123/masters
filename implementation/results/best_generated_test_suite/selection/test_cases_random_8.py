from cut import *

def test_case_0():
	cut = calorie_intake_calc(58.62,210.22,30,'M',0.72,'N')
	cut.weight = 150.24
	cut.amount_exercise = 'S'
	cut.bodyfat = -0.08
	cut.weight = 187.35
	cut.amount_exercise = 'M'

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(120.84,162.4,5,'N',0.0,'M')
	cut.amount_exercise = 'V'
	cut.height = 224.75

def test_case_3():
	cut = calorie_intake_calc(39.87,183.71,44,'N',0.19,'N')
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 196.51
	cut.weight = 57.45
	cut.bodyfat = -0.47
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(61.28,154.33,77,'N',0.59,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 221.94
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.weight = 185.87
	cut.age = 15

