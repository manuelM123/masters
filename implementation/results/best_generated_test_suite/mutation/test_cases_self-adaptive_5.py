from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.11,156.81,45,'F',-0.44,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 210.88
	cut.amount_exercise = 'V'
	cut.age = 53
	cut.amount_exercise = 'E'
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(47.5,147.37,81,'F',0.36,'M')
	cut.bodyfat = 0.61
	cut.bodyfat = 0.71
	cut.height = 179.98

def test_case_2():
	cut = calorie_intake_calc(39.8,194.88,75,'N',-0.09,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 186.17
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 52
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 203.37
	cut.age = 65
	cut.gender = 'N'

def test_case_3():
	cut = calorie_intake_calc(112.75,166.06,33,'F',0.1,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.16
	cut.height = 177.88
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 76
	cut.gender = 'N'
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(206.41,166.84,79,'M',0.29,'L')
	cut.weight = 174.48
	cut.age = 11
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(108.04,207.41,18,'M',0.67,'V')
	cut.gender = 'N'
	cut.age = 14
	cut.gender = 'F'
	cut.bodyfat = 0.54
	cut.height = 199.46
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	cut.age = 35

def test_case_6():
	cut = calorie_intake_calc(173.62,221.18,84,'F',-0.15,'L')
	cut.age = 78
	cut.weight = 160.31
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 169.77
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'

def test_case_7():
	cut = calorie_intake_calc(65.53,174.65,46,'F',0.03,'V')
	cut.amount_exercise = 'S'
	cut.weight = 45.4
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_8():
	cut = calorie_intake_calc(201.05,178.23,62,'N',0.03,'V')
	cut.height = 192.24
	cut.height = 212.36
	cut.weight = 116.72
	cut.gender = 'F'

