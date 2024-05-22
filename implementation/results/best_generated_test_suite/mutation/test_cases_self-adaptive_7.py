from cut import *

def test_case_0():
	cut = calorie_intake_calc(78.18,198.55,62,'N',0.36,'L')
	cut.bodyfat = -0.43
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(80.94,205.64,40,'M',0.09,'S')
	cut.weight = 76.38
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(175.53,144.82,70,'F',0.74,'S')
	cut.bodyfat = -0.09
	cut.gender = 'F'
	cut.bodyfat = 0.42

def test_case_3():
	cut = calorie_intake_calc(69.83,150.31,7,'N',0.35,'E')
	cut.weight = 108.07

def test_case_4():
	cut = calorie_intake_calc(69.83,150.31,7,'N',0.35,'E')
	cut.weight = 108.07

def test_case_5():
	cut = calorie_intake_calc(174.7,170.05,70,'M',-0.38,'S')
	cut.weight = 115.5
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.31
	cut.age = 67
	cut.age = 5
	cut.weight = 41.34
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 80.02
	cut.bodyfat = -0.29

def test_case_6():
	cut = calorie_intake_calc(42.53,219.67,73,'N',0.31,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 193.45
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_7():
	cut = calorie_intake_calc(77.68,183.52,66,'M',-0.11,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 163.45
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 182.97

def test_case_8():
	cut = calorie_intake_calc(115.49,174.47,16,'F',0.23,'M')
	cut.weight = 77.66
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 77
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_9():
	cut = calorie_intake_calc(168.01,174.99,56,'N',0.68,'V')

