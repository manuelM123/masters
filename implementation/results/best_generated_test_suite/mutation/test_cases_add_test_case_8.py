from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.11,156.81,45,'F',-0.44,'V')
	cut.gender = 'M'
	cut.bodyfat = -0.32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.amount_exercise = 'V'
	cut.age = 53
	cut.bodyfat = 0.16
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(173.61,224.66,23,'F',0.79,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 150.63

def test_case_3():
	cut = calorie_intake_calc(78.03,170.43,18,'M',0.05,'L')
	cut.gender = 'F'
	cut.height = 155.48
	cut.weight = 147.99
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(112.12,153.12,40,'M',-0.21,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 200.06
	cut.gender = 'N'
	cut.height = 168.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(157.38,159.01,63,'M',-0.38,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 11
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.24
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 34
	result_tdee_calculation = cut.tdee_calculation()

def test_case_6():
	cut = calorie_intake_calc(167.6,191.33,28,'M',0.03,'M')
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_7():
	cut = calorie_intake_calc(189.37,145.76,62,'F',-0.0,'M')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_8():
	cut = calorie_intake_calc(36.6,187.57,78,'F',0.25,'L')
	cut.bodyfat = 0.05

def test_case_9():
	cut = calorie_intake_calc(154.39,145.94,83,'F',-0.4,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 208.45
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 141.48

