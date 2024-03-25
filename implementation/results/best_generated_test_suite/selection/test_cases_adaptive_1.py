from cut import *

def test_case_0():
	cut = calorie_intake_calc(104.25,215.96,11,'F',0.29,'L')
	cut.height = 179.12
	cut.height = 165.42
	cut.weight = 192.9
	cut.amount_exercise = 'V'
	cut.height = 153.3
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 133.65
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(123.57,170.96,47,'M',0.28,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.height = 191.49
	cut.weight = 183.91
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'

def test_case_2():
	cut = calorie_intake_calc(150.07,149.31,64,'F',0.03,'M')
	cut.bodyfat = 0.01
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.11
	cut.bodyfat = 0.26
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 48

def test_case_3():
	cut = calorie_intake_calc(87.73,219.64,24,'F',0.04,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 210.54
	cut.height = 218.41
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

