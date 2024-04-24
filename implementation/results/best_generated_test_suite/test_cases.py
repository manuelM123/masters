from cut import *

def test_case_0():
	cut = calorie_intake_calc(124.58,198.51,50,'M',-0.33,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 168.84
	cut.amount_exercise = 'L'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 184.0
	cut.age = 30
	cut.bodyfat = -0.26
	cut.age = 76
	cut.weight = 206.49
	cut.age = 5
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.age = 71

def test_case_1():
	cut = calorie_intake_calc(132.13,144.4,34,'F',0.53,'M')
	cut.age = 50
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 34
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 53
	cut.height = 221.16
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	cut.bodyfat = -0.32
	cut.bodyfat = -0.47
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 213.27
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 63
	cut.amount_exercise = 'N'
	cut.height = 163.46

def test_case_2():
	cut = calorie_intake_calc(59.38,176.8,46,'M',0.51,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 192.54
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	cut.gender = 'F'
	cut.height = 166.71
	cut.age = 45

def test_case_3():
	cut = calorie_intake_calc(210.06,205.63,54,'M',-0.13,'N')

def test_case_4():
	cut = calorie_intake_calc(147.77,205.73,14,'M',0.09,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 44.56
	cut.age = 72
	cut.age = 31
	cut.age = 73
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_5():
	cut = calorie_intake_calc(203.5,202.52,56,'N',-0.16,'V')
	cut.age = 85
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 66
	cut.bodyfat = -0.35
	cut.height = 208.82
	cut.gender = 'F'
	cut.weight = 54.08

def test_case_6():
	cut = calorie_intake_calc(154.08,187.57,33,'M',0.07,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 145.84
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 173.49
	cut.height = 146.22

def test_case_7():
	cut = calorie_intake_calc(196.82,205.3,76,'F',0.29,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 155.92
	cut.gender = 'M'
	cut.bodyfat = -0.39
	cut.height = 190.87
	cut.height = 184.73
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_8():
	cut = calorie_intake_calc(174.23,194.22,77,'F',0.28,'V')
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_9():
	cut = calorie_intake_calc(102.23,222.99,77,'N',-0.16,'E')
	cut.weight = 140.72
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 84
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 119.76
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'

def test_case_10():
	cut = calorie_intake_calc(84.62,192.46,49,'F',0.75,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_11():
	cut = calorie_intake_calc(181.31,221.27,84,'N',-0.34,'M')
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 56
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 58
	cut.height = 175.21
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 19
	cut.bodyfat = 0.33
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.4
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_12():
	cut = calorie_intake_calc(185.34,157.32,47,'N',0.28,'N')
	cut.amount_exercise = 'V'
	cut.gender = 'M'
	cut.age = 64
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.48
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 69
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 176.33
	cut.height = 192.51
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

