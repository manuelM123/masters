from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.11,156.81,45,'F',-0.44,'V')
	cut.gender = 'M'
	cut.bodyfat = -0.32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.amount_exercise = 'V'
	cut.age = 53
	cut.bodyfat = 0.16
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(129.39,200.26,44,'F',0.3,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 178.53
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(37.98,144.17,32,'F',0.39,'S')
	cut.bodyfat = 0.28
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 75
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 207.11
	cut.bodyfat = 0.46

def test_case_3():
	cut = calorie_intake_calc(40.91,173.75,6,'M',0.45,'L')

def test_case_4():
	cut = calorie_intake_calc(86.07,186.52,38,'M',-0.31,'E')
	cut.amount_exercise = 'E'
	cut.weight = 189.54
	cut.age = 23
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(84.86,182.66,82,'M',-0.47,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'

def test_case_6():
	cut = calorie_intake_calc(149.38,222.28,56,'F',-0.4,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.62
	cut.height = 158.99
	cut.bodyfat = 0.15

def test_case_7():
	cut = calorie_intake_calc(185.87,154.48,28,'N',0.01,'L')
	cut.weight = 187.29
	result_tdee_calculation = cut.tdee_calculation()

def test_case_8():
	cut = calorie_intake_calc(207.85,149.89,16,'F',-0.3,'N')
	cut.gender = 'M'
	cut.height = 206.08
	cut.age = 79
	cut.weight = 209.95
	cut.amount_exercise = 'V'
	cut.age = 11
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_9():
	cut = calorie_intake_calc(114.1,203.87,34,'M',0.21,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.26
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 21
	cut.gender = 'F'

def test_case_10():
	cut = calorie_intake_calc(72.77,183.73,12,'F',0.37,'V')
	cut.weight = 118.86
	cut.age = 64
	cut.height = 175.16

def test_case_11():
	cut = calorie_intake_calc(175.7,198.49,18,'F',-0.13,'M')

def test_case_12():
	cut = calorie_intake_calc(177.57,159.02,78,'M',-0.19,'S')
	cut.age = 56
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_13():
	cut = calorie_intake_calc(136.41,163.18,63,'F',-0.35,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.31
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 179.99
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_14():
	cut = calorie_intake_calc(122.41,163.09,32,'M',-0.03,'M')
	cut.gender = 'F'
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()

