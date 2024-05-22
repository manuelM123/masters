from cut import *

def test_case_0():
	cut = calorie_intake_calc(191.62,171.44,13,'F',0.25,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 170.5
	cut.amount_exercise = 'S'
	cut.height = 203.7
	cut.bodyfat = 0.69
	cut.amount_exercise = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.07
	cut.age = 44

def test_case_1():
	cut = calorie_intake_calc(91.22,171.6,59,'M',-0.19,'S')
	cut.age = 20
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 45

def test_case_2():
	cut = calorie_intake_calc(69.59,176.66,60,'F',-0.47,'E')
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.bodyfat = 0.41
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 140.13
	cut.bodyfat = 0.42

def test_case_3():
	cut = calorie_intake_calc(142.95,179.62,27,'F',0.4,'L')
	cut.weight = 129.49

def test_case_4():
	cut = calorie_intake_calc(37.37,190.95,16,'F',0.56,'S')
	cut.bodyfat = 0.57
	cut.age = 15
	cut.weight = 140.93
	cut.weight = 179.85
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(192.11,162.37,55,'F',-0.12,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 150.92

def test_case_6():
	cut = calorie_intake_calc(93.79,154.1,12,'N',0.3,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.25
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 213.21
	cut.gender = 'F'

def test_case_7():
	cut = calorie_intake_calc(191.66,206.56,39,'F',-0.08,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	cut.age = 67

def test_case_8():
	cut = calorie_intake_calc(116.16,224.77,54,'N',0.57,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 108.49
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	cut.height = 142.32
	result_tdee_calculation = cut.tdee_calculation()

def test_case_9():
	cut = calorie_intake_calc(99.94,217.28,5,'N',0.73,'L')

def test_case_10():
	cut = calorie_intake_calc(70.02,156.36,24,'M',0.21,'E')
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.69
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	cut.bodyfat = -0.21
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

