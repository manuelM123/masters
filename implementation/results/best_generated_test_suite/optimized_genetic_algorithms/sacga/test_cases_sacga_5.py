from cut import *

def test_case_0():
	cut = calorie_intake_calc(172.64,194.31,19,'M',0.66,'L')
	cut.weight = 214.74
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 27

def test_case_1():
	cut = calorie_intake_calc(164.8,210.32,59,'M',-0.13,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(160.19,140.5,83,'N',0.57,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'

def test_case_3():
	cut = calorie_intake_calc(170.82,203.18,56,'N',-0.27,'M')

def test_case_4():
	cut = calorie_intake_calc(49.84,159.67,53,'N',-0.36,'S')
	cut.age = 28
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(38.09,216.93,78,'N',0.59,'L')
	cut.bodyfat = -0.24

def test_case_6():
	cut = calorie_intake_calc(125.86,160.77,6,'F',-0.09,'V')
	cut.age = 14
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 85

def test_case_7():
	cut = calorie_intake_calc(159.68,136.32,25,'F',-0.17,'E')
	cut.age = 79

def test_case_8():
	cut = calorie_intake_calc(50.21,191.63,47,'M',0.05,'E')
	cut.age = 63
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_9():
	cut = calorie_intake_calc(188.32,186.92,71,'M',0.77,'E')

def test_case_10():
	cut = calorie_intake_calc(173.0,183.64,63,'F',0.61,'E')

def test_case_11():
	cut = calorie_intake_calc(98.57,140.19,25,'M',-0.27,'L')
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_12():
	cut = calorie_intake_calc(209.55,210.92,73,'M',0.3,'E')
	cut.weight = 199.79
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_13():
	cut = calorie_intake_calc(164.82,174.0,60,'F',0.09,'N')
	cut.bodyfat = -0.28
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_14():
	cut = calorie_intake_calc(115.19,156.8,9,'F',0.59,'M')
	cut.age = 84
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.37

def test_case_15():
	cut = calorie_intake_calc(89.7,220.81,47,'F',-0.13,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_16():
	cut = calorie_intake_calc(128.81,213.14,57,'N',-0.34,'N')
	cut.bodyfat = 0.58
	cut.height = 137.72
	cut.age = 48
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_17():
	cut = calorie_intake_calc(204.73,195.92,43,'M',0.52,'N')

def test_case_18():
	cut = calorie_intake_calc(51.43,142.93,27,'F',-0.28,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

