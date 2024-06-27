from cut import *

def test_case_0():
	cut = calorie_intake_calc(121.21,154.68,22,'M',0.2,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(177.63,197.3,76,'F',0.29,'N')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(43.29,180.15,75,'M',-0.22,'S')

def test_case_3():
	cut = calorie_intake_calc(160.81,216.87,12,'M',-0.03,'V')
	cut.gender = 'M'
	cut.age = 72
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(189.81,151.9,80,'N',-0.13,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	cut.age = 18

def test_case_5():
	cut = calorie_intake_calc(107.23,221.31,62,'N',-0.45,'S')
	cut.age = 42

def test_case_6():
	cut = calorie_intake_calc(61.88,151.72,14,'F',0.59,'V')
	cut.height = 187.99
	cut.weight = 35.42
	cut.height = 155.17

def test_case_7():
	cut = calorie_intake_calc(89.68,220.46,78,'M',-0.25,'V')

def test_case_8():
	cut = calorie_intake_calc(85.11,156.15,81,'N',0.07,'L')

def test_case_9():
	cut = calorie_intake_calc(177.39,145.95,17,'N',0.31,'N')
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 16
	result_tdee_calculation = cut.tdee_calculation()

def test_case_10():
	cut = calorie_intake_calc(40.75,139.18,67,'M',-0.44,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.42
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.51

def test_case_11():
	cut = calorie_intake_calc(151.56,154.95,23,'M',0.66,'S')
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_12():
	cut = calorie_intake_calc(212.69,162.05,71,'N',-0.41,'S')
	cut.weight = 149.64
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_13():
	cut = calorie_intake_calc(124.78,178.94,66,'F',-0.03,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.06
	cut.height = 139.42

def test_case_14():
	cut = calorie_intake_calc(197.16,154.87,59,'M',-0.29,'M')
	cut.height = 171.32
	cut.amount_exercise = 'V'

def test_case_15():
	cut = calorie_intake_calc(178.35,151.4,80,'F',0.48,'S')
	cut.height = 182.38
	cut.amount_exercise = 'S'
	cut.height = 186.25

def test_case_16():
	cut = calorie_intake_calc(206.35,220.29,69,'F',0.48,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_17():
	cut = calorie_intake_calc(73.47,143.33,28,'M',-0.04,'E')
	cut.weight = 188.95
	result_tdee_calculation = cut.tdee_calculation()

