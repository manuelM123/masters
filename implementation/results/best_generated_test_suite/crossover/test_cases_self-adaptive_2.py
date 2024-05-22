from cut import *

def test_case_0():
	cut = calorie_intake_calc(62.88,144.93,18,'M',0.15,'S')
	cut.height = 216.2
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.78
	cut.weight = 116.76
	cut.gender = 'M'
	cut.weight = 197.25
	cut.age = 15
	cut.age = 8
	cut.age = 11

def test_case_1():
	cut = calorie_intake_calc(103.22,202.07,72,'M',0.19,'S')
	cut.weight = 59.76
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.06
	cut.bodyfat = -0.1

def test_case_2():
	cut = calorie_intake_calc(161.43,145.39,65,'M',-0.1,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.age = 55
	cut.age = 8
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.gender = 'N'

def test_case_3():
	cut = calorie_intake_calc(40.26,185.05,70,'N',0.73,'V')
	cut.weight = 59.27
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 171.14
	cut.height = 151.08
	cut.height = 165.06
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(177.32,157.49,38,'M',0.03,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 10
	cut.height = 189.88
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.51
	cut.age = 59

def test_case_5():
	cut = calorie_intake_calc(150.87,164.33,10,'N',0.18,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 17
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 173.69
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 85
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_6():
	cut = calorie_intake_calc(171.25,184.93,74,'F',-0.26,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.8

def test_case_7():
	cut = calorie_intake_calc(74.46,205.29,70,'M',-0.24,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_8():
	cut = calorie_intake_calc(126.55,161.65,79,'M',-0.42,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 151.97
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 109.11
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 195.42
	cut.height = 223.78
	cut.weight = 107.75

def test_case_9():
	cut = calorie_intake_calc(170.08,180.08,31,'M',-0.47,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 181.0
	cut.weight = 147.93
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 166.43
	cut.height = 189.48
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_10():
	cut = calorie_intake_calc(40.16,218.08,6,'N',-0.28,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.25
	result_tdee_calculation = cut.tdee_calculation()

def test_case_11():
	cut = calorie_intake_calc(176.53,216.38,39,'M',-0.21,'E')
	cut.amount_exercise = 'V'
	cut.age = 56
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_12():
	cut = calorie_intake_calc(210.41,146.81,31,'F',0.29,'V')
	cut.weight = 46.13

