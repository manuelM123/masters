from cut import *

def test_case_0():
	cut = calorie_intake_calc(210.59,197.56,55,'N',-0.26,'L')
	cut.weight = 84.12
	cut.gender = 'F'
	cut.weight = 58.28
	cut.height = 223.07
	cut.height = 151.11
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 140.18
	cut.age = 69
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(146.1,216.35,21,'N',-0.3,'L')
	cut.weight = 37.49
	cut.weight = 75.22
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(105.75,149.41,47,'F',-0.05,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 162.77
	cut.bodyfat = 0.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.19
	cut.age = 55

def test_case_3():
	cut = calorie_intake_calc(102.68,152.02,36,'F',0.22,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 83
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 72
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 85
	cut.weight = 47.06
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(201.32,142.81,55,'F',0.32,'S')
	cut.age = 62
	cut.bodyfat = 0.44
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 144.41
	cut.weight = 147.31
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(53.63,183.18,39,'M',-0.48,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 70
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 129.65
	cut.bodyfat = 0.18
	cut.height = 137.71
	cut.amount_exercise = 'E'
	cut.age = 20

def test_case_6():
	cut = calorie_intake_calc(135.64,211.16,69,'F',-0.33,'L')
	cut.height = 194.34
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

