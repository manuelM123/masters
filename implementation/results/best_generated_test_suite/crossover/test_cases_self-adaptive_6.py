from cut import *

def test_case_0():
	cut = calorie_intake_calc(110.0,147.01,6,'M',-0.28,'L')

def test_case_1():
	cut = calorie_intake_calc(58.45,141.08,73,'M',-0.22,'M')
	cut.amount_exercise = 'L'
	cut.gender = 'F'
	cut.bodyfat = -0.01
	cut.weight = 154.6
	cut.height = 222.92
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 66

def test_case_2():
	cut = calorie_intake_calc(84.65,215.84,47,'N',-0.34,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(157.62,171.7,22,'F',-0.03,'L')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(63.37,192.74,75,'M',-0.45,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 8

def test_case_5():
	cut = calorie_intake_calc(63.37,192.74,75,'M',-0.45,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 8

def test_case_6():
	cut = calorie_intake_calc(204.03,216.55,83,'F',0.5,'S')

def test_case_7():
	cut = calorie_intake_calc(204.03,216.55,83,'F',0.5,'S')

def test_case_8():
	cut = calorie_intake_calc(93.25,137.24,38,'F',0.29,'S')
	cut.age = 50

def test_case_9():
	cut = calorie_intake_calc(158.03,202.31,21,'M',0.21,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'

def test_case_10():
	cut = calorie_intake_calc(85.96,162.91,67,'N',0.66,'N')
	cut.weight = 71.58
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 158.7
	cut.bodyfat = 0.12
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_11():
	cut = calorie_intake_calc(155.08,152.12,79,'M',0.17,'M')
	cut.amount_exercise = 'V'
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.07
	cut.age = 27
	cut.bodyfat = 0.68
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_12():
	cut = calorie_intake_calc(185.84,190.39,35,'M',0.65,'V')
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'V'

def test_case_13():
	cut = calorie_intake_calc(103.13,169.57,44,'M',0.13,'V')
	cut.bodyfat = -0.26
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 41
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_14():
	cut = calorie_intake_calc(88.73,137.07,39,'F',-0.27,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 66
	cut.age = 49
	cut.bodyfat = 0.45
	cut.height = 219.34
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 81
	cut.age = 14

def test_case_15():
	cut = calorie_intake_calc(75.46,184.86,42,'F',-0.21,'E')
	cut.weight = 209.07
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 160.21
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 90.41
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'S'

def test_case_16():
	cut = calorie_intake_calc(214.37,169.86,25,'M',0.36,'L')
	cut.weight = 90.5

def test_case_17():
	cut = calorie_intake_calc(147.69,158.49,28,'N',0.71,'M')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_18():
	cut = calorie_intake_calc(197.71,178.99,68,'M',0.07,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'
	cut.age = 57
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.47
	cut.bodyfat = 0.1

def test_case_19():
	cut = calorie_intake_calc(83.75,158.54,15,'M',0.13,'V')
	cut.weight = 89.19
	cut.weight = 69.07
	cut.height = 173.08
	cut.age = 79
	cut.weight = 143.32
	cut.amount_exercise = 'E'

def test_case_20():
	cut = calorie_intake_calc(87.92,189.32,73,'M',0.3,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

