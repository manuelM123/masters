from cut import *

def test_case_0():
	cut = calorie_intake_calc(190.72,215.12,27,'M',-0.26,'S')
	cut.gender = 'F'
	cut.bodyfat = 0.67
	cut.gender = 'N'
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 51
	cut.amount_exercise = 'N'
	cut.age = 25

def test_case_1():
	cut = calorie_intake_calc(59.91,148.31,79,'F',-0.09,'M')
	cut.amount_exercise = 'M'
	cut.bodyfat = 0.38
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 217.07
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(59.91,148.31,79,'F',-0.09,'M')
	cut.amount_exercise = 'M'
	cut.bodyfat = 0.38
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 217.07
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(155.38,177.84,8,'F',0.62,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(76.48,161.76,24,'M',-0.06,'V')
	cut.bodyfat = -0.27
	cut.gender = 'N'

def test_case_5():
	cut = calorie_intake_calc(119.96,190.83,61,'M',0.8,'V')
	cut.gender = 'F'
	cut.amount_exercise = 'N'
	cut.bodyfat = 0.67

def test_case_6():
	cut = calorie_intake_calc(103.0,157.78,56,'M',-0.07,'E')
	cut.bodyfat = -0.37
	cut.weight = 78.18
	cut.height = 166.68
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 125.8

def test_case_7():
	cut = calorie_intake_calc(103.0,157.78,56,'M',-0.07,'E')
	cut.bodyfat = -0.37
	cut.weight = 78.18
	cut.height = 166.68
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 125.8

def test_case_8():
	cut = calorie_intake_calc(129.12,159.92,73,'M',0.22,'V')
	cut.age = 54
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 138.57

def test_case_9():
	cut = calorie_intake_calc(43.17,183.4,48,'F',0.26,'L')
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'V'
	cut.weight = 122.47
	cut.age = 41
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_10():
	cut = calorie_intake_calc(107.68,141.66,36,'M',-0.32,'S')
	cut.gender = 'M'
	cut.bodyfat = -0.41
	cut.age = 38
	cut.amount_exercise = 'N'
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.17

def test_case_11():
	cut = calorie_intake_calc(202.36,206.81,67,'N',-0.24,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_12():
	cut = calorie_intake_calc(62.9,149.92,18,'M',-0.26,'V')
	cut.age = 26
	result_tdee_calculation = cut.tdee_calculation()

def test_case_13():
	cut = calorie_intake_calc(174.39,146.93,27,'M',-0.48,'M')
	cut.age = 74
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 42
	cut.age = 14
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_14():
	cut = calorie_intake_calc(187.87,189.29,13,'M',-0.02,'N')
	cut.height = 180.64
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 213.97
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 8
	cut.amount_exercise = 'V'
	cut.weight = 93.24
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

