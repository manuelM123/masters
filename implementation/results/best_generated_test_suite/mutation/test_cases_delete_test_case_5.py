from cut import *

def test_case_0():
	cut = calorie_intake_calc(47.85,152.75,60,'M',-0.46,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 206.8
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 68.83
	cut.weight = 48.22

def test_case_1():
	cut = calorie_intake_calc(139.24,213.07,83,'N',0.41,'V')
	cut.gender = 'F'
	cut.age = 50
	cut.age = 42
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(78.93,147.66,60,'F',0.72,'M')
	cut.bodyfat = -0.15
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(154.55,186.49,77,'F',-0.22,'S')
	cut.bodyfat = -0.31
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 78
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 139.54
	cut.weight = 77.01

def test_case_4():
	cut = calorie_intake_calc(75.55,211.49,29,'N',-0.09,'S')

