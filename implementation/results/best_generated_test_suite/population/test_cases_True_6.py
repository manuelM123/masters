from cut import *

def test_case_0():
	cut = calorie_intake_calc(128.66,148.45,67,'F',0.0,'E')
	cut.bodyfat = 0.3
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 171.1

def test_case_1():
	cut = calorie_intake_calc(117.65,179.41,38,'M',0.35,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(198.83,151.57,69,'M',-0.35,'S')

def test_case_3():
	cut = calorie_intake_calc(133.93,146.57,31,'N',0.74,'S')
	cut.height = 144.39
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 114.52
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 159.47
	cut.bodyfat = -0.13

def test_case_4():
	cut = calorie_intake_calc(71.82,141.84,82,'N',-0.23,'N')
	cut.age = 29
	cut.age = 60
	cut.amount_exercise = 'M'
	cut.bodyfat = -0.18
	cut.weight = 64.16
	cut.amount_exercise = 'N'
	cut.age = 57
	cut.weight = 176.81
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(121.8,204.29,20,'M',-0.34,'L')
	cut.age = 9
	cut.amount_exercise = 'N'
	cut.height = 140.35
	cut.amount_exercise = 'N'
	cut.bodyfat = 0.51
	cut.age = 77
	cut.gender = 'F'
	cut.bodyfat = -0.47
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(82.43,175.5,26,'F',-0.27,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 137.87
	cut.age = 46
	cut.age = 41
	cut.height = 149.94
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 67
	cut.amount_exercise = 'E'
	cut.height = 203.95
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_7():
	cut = calorie_intake_calc(158.05,171.11,81,'M',-0.02,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'

def test_case_8():
	cut = calorie_intake_calc(165.21,169.41,8,'N',-0.48,'M')
	cut.amount_exercise = 'S'

def test_case_9():
	cut = calorie_intake_calc(189.44,167.54,48,'M',0.09,'L')
	cut.weight = 203.45
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 91.45
	cut.bodyfat = -0.33
	cut.bodyfat = -0.2
	result_determine_calorie_intake = cut.determine_calorie_intake()

