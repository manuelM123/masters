from cut import *

def test_case_0():
	cut = calorie_intake_calc(86.58,199.82,61,'M',-0.25,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.bodyfat = 0.46
	cut.height = 139.19
	cut.height = 151.46
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(86.74,171.69,17,'F',0.11,'V')
	cut.bodyfat = 0.77
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(142.79,145.85,10,'F',0.36,'S')
	cut.height = 149.61
	cut.bodyfat = 0.26
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(183.45,186.26,43,'F',0.79,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 10
	cut.height = 138.46
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 164.51

def test_case_4():
	cut = calorie_intake_calc(64.62,189.82,38,'F',0.57,'V')
	cut.bodyfat = 0.15
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 163.39
	cut.height = 208.44
	cut.weight = 171.57
	cut.weight = 207.01
	cut.weight = 122.04

def test_case_5():
	cut = calorie_intake_calc(90.94,216.18,53,'N',0.8,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 155.8
	cut.amount_exercise = 'L'
	cut.weight = 125.56

def test_case_6():
	cut = calorie_intake_calc(176.34,213.84,84,'F',0.78,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 78.87
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 71.38
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.25
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_7():
	cut = calorie_intake_calc(151.86,146.25,66,'N',-0.49,'E')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_8():
	cut = calorie_intake_calc(151.33,154.42,51,'M',0.42,'N')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 176.19
	cut.weight = 54.54
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.65

