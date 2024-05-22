from cut import *

def test_case_0():
	cut = calorie_intake_calc(188.64,146.93,69,'F',0.18,'L')
	cut.age = 34
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 133.72

def test_case_1():
	cut = calorie_intake_calc(210.55,153.42,54,'N',0.57,'S')
	cut.gender = 'F'
	cut.bodyfat = -0.02
	cut.height = 142.1

def test_case_2():
	cut = calorie_intake_calc(191.59,140.6,30,'F',0.26,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 205.61
	cut.age = 81
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(191.59,140.6,30,'F',0.26,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 205.61
	cut.age = 81
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(115.98,190.83,53,'M',-0.07,'V')
	cut.age = 43
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.height = 143.62
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'

def test_case_5():
	cut = calorie_intake_calc(116.56,169.27,48,'M',0.21,'V')
	cut.height = 186.55
	cut.height = 136.39
	cut.age = 24
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 46
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(189.79,154.53,68,'N',0.43,'M')
	cut.bodyfat = 0.26
	cut.age = 36

def test_case_7():
	cut = calorie_intake_calc(163.7,139.33,27,'M',0.43,'M')
	cut.age = 48

def test_case_8():
	cut = calorie_intake_calc(109.32,180.76,83,'M',0.64,'E')
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_9():
	cut = calorie_intake_calc(56.61,140.07,62,'N',0.02,'L')
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 135.56

def test_case_10():
	cut = calorie_intake_calc(143.4,206.3,49,'F',-0.13,'M')
	cut.height = 191.39
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 189.92
	cut.height = 211.28

def test_case_11():
	cut = calorie_intake_calc(116.37,170.23,42,'M',-0.42,'N')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.75
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_12():
	cut = calorie_intake_calc(48.14,141.27,85,'F',-0.43,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 195.75
	cut.bodyfat = 0.63
	cut.bodyfat = 0.0
	result_tdee_calculation = cut.tdee_calculation()

def test_case_13():
	cut = calorie_intake_calc(121.32,142.77,77,'F',-0.15,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 106.27
	cut.height = 222.31
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()

