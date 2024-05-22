from cut import *

def test_case_0():
	cut = calorie_intake_calc(174.17,154.7,36,'M',-0.42,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(71.87,178.85,36,'M',-0.33,'V')
	cut.bodyfat = 0.69
	cut.age = 60
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.height = 195.93
	cut.height = 161.61
	cut.gender = 'F'
	cut.bodyfat = 0.44
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(80.88,151.39,78,'F',-0.13,'S')
	cut.weight = 95.93
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 6
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.11

def test_case_3():
	cut = calorie_intake_calc(123.07,188.03,32,'F',0.22,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 69
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 138.8
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(46.13,211.27,17,'F',0.25,'E')
	cut.height = 154.08
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(159.03,217.83,51,'N',0.01,'M')
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 193.3
	cut.weight = 98.19

def test_case_6():
	cut = calorie_intake_calc(184.61,221.35,83,'M',-0.47,'S')
	cut.weight = 63.34
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_7():
	cut = calorie_intake_calc(212.93,170.65,15,'F',0.14,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.35
	cut.age = 54
	cut.weight = 176.88
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 137.34
	cut.height = 222.83
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_8():
	cut = calorie_intake_calc(68.81,140.23,83,'N',-0.25,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 213.05
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 185.86

