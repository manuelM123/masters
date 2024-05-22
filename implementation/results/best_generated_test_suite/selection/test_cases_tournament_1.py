from cut import *

def test_case_0():
	cut = calorie_intake_calc(188.64,146.93,69,'F',0.18,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	cut.weight = 133.72

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 79.76
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(162.14,182.87,84,'F',-0.36,'M')
	cut.weight = 131.69
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(172.52,195.47,33,'M',0.77,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.35
	cut.age = 50
	cut.height = 159.7
	cut.age = 40

def test_case_4():
	cut = calorie_intake_calc(112.12,153.12,40,'M',-0.21,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 200.06
	cut.gender = 'N'
	cut.height = 168.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(125.12,218.14,20,'N',0.77,'E')
	cut.height = 180.11
	cut.gender = 'F'
	cut.height = 180.23
	cut.amount_exercise = 'S'
	cut.age = 83
	cut.amount_exercise = 'M'
	cut.age = 72

def test_case_6():
	cut = calorie_intake_calc(86.75,183.63,60,'M',-0.15,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 18
	cut.height = 224.73
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()

