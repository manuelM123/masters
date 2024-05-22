from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.49,150.72,61,'M',0.79,'S')
	cut.weight = 41.05
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 132.8
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 179.43
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.02
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 79

def test_case_1():
	cut = calorie_intake_calc(113.48,188.1,39,'M',0.38,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 147.23
	cut.height = 200.94
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 76
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(163.97,164.69,77,'F',0.63,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 39.07
	cut.bodyfat = 0.57
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(94.51,156.48,25,'N',-0.45,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'

def test_case_4():
	cut = calorie_intake_calc(112.8,145.87,13,'M',-0.08,'S')
	cut.bodyfat = 0.06
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 172.37

def test_case_5():
	cut = calorie_intake_calc(192.74,177.84,43,'F',0.65,'L')
	cut.age = 45
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.bodyfat = 0.16
	result_tdee_calculation = cut.tdee_calculation()

def test_case_6():
	cut = calorie_intake_calc(73.67,163.72,13,'F',-0.04,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 208.8
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 81
	cut.bodyfat = 0.58
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_7():
	cut = calorie_intake_calc(67.25,186.88,64,'M',0.01,'M')
	cut.weight = 121.01
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.height = 160.68
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 135.64

def test_case_8():
	cut = calorie_intake_calc(87.67,135.28,10,'F',-0.38,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_9():
	cut = calorie_intake_calc(117.42,198.42,46,'M',-0.2,'E')
	cut.bodyfat = -0.38
	cut.bodyfat = -0.06
	cut.age = 70
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 212.04
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 160.95

def test_case_10():
	cut = calorie_intake_calc(76.6,208.67,13,'F',-0.47,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	cut.bodyfat = -0.2
	cut.bodyfat = 0.69
	cut.height = 206.58
	cut.weight = 136.39

def test_case_11():
	cut = calorie_intake_calc(189.65,152.6,23,'M',0.62,'V')
	cut.weight = 98.84
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 99.03
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_12():
	cut = calorie_intake_calc(135.11,209.33,80,'F',0.51,'V')
	cut.height = 201.83
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'
	cut.age = 53
	cut.height = 138.58
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_13():
	cut = calorie_intake_calc(82.99,149.97,36,'F',-0.48,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

