from cut import *

def test_case_0():
	cut = calorie_intake_calc(146.22,190.84,62,'F',-0.02,'L')
	cut.weight = 60.99
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.32

def test_case_1():
	cut = calorie_intake_calc(190.12,212.36,9,'N',-0.35,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 192.83

def test_case_2():
	cut = calorie_intake_calc(99.14,182.37,43,'M',-0.08,'N')
	cut.weight = 81.33

def test_case_3():
	cut = calorie_intake_calc(173.12,201.23,36,'N',0.26,'N')
	cut.amount_exercise = 'S'

def test_case_4():
	cut = calorie_intake_calc(147.98,157.57,41,'F',0.3,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 167.05
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(147.98,157.57,41,'F',0.3,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 167.05
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_6():
	cut = calorie_intake_calc(93.74,180.35,24,'F',-0.08,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 79

def test_case_7():
	cut = calorie_intake_calc(68.94,224.09,73,'M',0.33,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'

def test_case_8():
	cut = calorie_intake_calc(94.14,137.76,48,'F',0.74,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 168.39
	cut.weight = 129.14

def test_case_9():
	cut = calorie_intake_calc(197.47,201.03,27,'M',0.69,'V')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_10():
	cut = calorie_intake_calc(167.47,174.47,22,'F',0.19,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 121.97
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_11():
	cut = calorie_intake_calc(148.14,145.5,45,'F',0.04,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 190.51
	cut.height = 205.21
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_12():
	cut = calorie_intake_calc(58.36,185.21,51,'F',0.61,'E')

def test_case_13():
	cut = calorie_intake_calc(173.69,140.83,20,'M',0.46,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.age = 18

def test_case_14():
	cut = calorie_intake_calc(93.21,146.5,28,'M',-0.48,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 173.17
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_15():
	cut = calorie_intake_calc(80.03,173.89,50,'N',-0.05,'S')
	cut.bodyfat = 0.19

def test_case_16():
	cut = calorie_intake_calc(36.12,159.56,75,'M',0.6,'L')
	cut.amount_exercise = 'L'

