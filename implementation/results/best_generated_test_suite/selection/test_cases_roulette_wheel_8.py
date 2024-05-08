from cut import *

def test_case_0():
	cut = calorie_intake_calc(47.85,152.75,60,'M',-0.46,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 206.8
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 68.83
	cut.weight = 48.22

def test_case_1():
	cut = calorie_intake_calc(92.59,156.53,31,'M',0.6,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 199.81
	cut.bodyfat = -0.06
	cut.bodyfat = 0.17
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 172.86
	cut.age = 13
	cut.amount_exercise = 'E'
	cut.age = 6
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(108.33,163.25,57,'F',-0.35,'V')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(154.55,186.49,77,'F',-0.22,'S')
	cut.bodyfat = -0.31
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 78
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 139.54
	cut.weight = 77.01

def test_case_4():
	cut = calorie_intake_calc(71.49,171.8,71,'M',-0.14,'E')
	cut.bodyfat = -0.18
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	cut.weight = 104.37
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 186.76
	cut.gender = 'F'
	cut.bodyfat = -0.33

def test_case_5():
	cut = calorie_intake_calc(108.29,213.19,46,'F',0.25,'N')
	cut.gender = 'N'
	cut.weight = 117.68
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'

def test_case_6():
	cut = calorie_intake_calc(121.11,200.08,63,'N',-0.48,'L')
	cut.height = 149.26
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 66
	cut.amount_exercise = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 41
	cut.bodyfat = 0.18
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'

