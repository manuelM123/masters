from cut import *

def test_case_0():
	cut = calorie_intake_calc(209.71,207.46,40,'N',0.28,'V')
	cut.height = 214.09

def test_case_1():
	cut = calorie_intake_calc(182.73,156.98,64,'N',0.01,'N')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 94.85
	cut.bodyfat = 0.26
	cut.gender = 'N'
	cut.bodyfat = 0.27
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.13

def test_case_2():
	cut = calorie_intake_calc(170.09,149.78,28,'F',0.17,'S')
	cut.bodyfat = 0.16
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 75
	cut.amount_exercise = 'M'
	cut.height = 140.43
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(118.13,174.9,10,'M',0.14,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.23
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(96.03,154.2,78,'M',0.25,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 55.0
	cut.gender = 'F'
	cut.weight = 123.46
	cut.amount_exercise = 'V'

def test_case_5():
	cut = calorie_intake_calc(199.39,173.8,57,'F',0.15,'L')
	cut.weight = 158.36
	cut.age = 13
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.26
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 65.65
	cut.gender = 'M'
	cut.amount_exercise = 'L'

def test_case_6():
	cut = calorie_intake_calc(183.04,152.06,32,'M',0.01,'E')
	cut.weight = 160.47
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.28
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_7():
	cut = calorie_intake_calc(140.76,155.37,41,'F',0.14,'N')
	cut.height = 160.9
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 79
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 63

def test_case_8():
	cut = calorie_intake_calc(183.76,193.71,51,'M',0.03,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 54.22
	cut.weight = 174.63

