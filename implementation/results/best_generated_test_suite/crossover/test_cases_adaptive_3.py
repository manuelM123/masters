from cut import *

def test_case_0():
	cut = calorie_intake_calc(172.17,167.05,48,'N',-0.28,'M')
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 77
	cut.height = 208.12
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(152.5,210.23,29,'M',0.04,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 56
	cut.age = 66
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(163.97,146.27,41,'N',0.29,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 74
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 215.74
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 97.32

def test_case_3():
	cut = calorie_intake_calc(105.2,213.02,62,'N',-0.13,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 183.32

def test_case_4():
	cut = calorie_intake_calc(121.05,166.84,19,'M',0.58,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 37.85
	cut.bodyfat = 0.71
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.03
	cut.bodyfat = 0.03
	cut.height = 189.67
	cut.weight = 164.53

def test_case_5():
	cut = calorie_intake_calc(166.2,139.69,68,'M',0.65,'E')
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(59.04,213.28,20,'F',0.7,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_7():
	cut = calorie_intake_calc(210.29,216.55,79,'N',-0.09,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 36
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.age = 46

def test_case_8():
	cut = calorie_intake_calc(206.46,148.13,40,'F',0.02,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.45
	cut.gender = 'M'
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 73.93
	cut.weight = 156.07

