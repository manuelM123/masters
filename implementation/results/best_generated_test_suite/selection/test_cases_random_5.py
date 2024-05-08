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
	cut = calorie_intake_calc(78.93,147.66,60,'F',0.72,'M')
	cut.bodyfat = -0.15
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

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
	cut = calorie_intake_calc(74.74,185.44,35,'M',0.43,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 51
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.08
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(70.72,172.92,15,'N',-0.5,'S')
	cut.height = 222.12
	cut.weight = 188.43
	cut.age = 21
	cut.age = 65
	cut.amount_exercise = 'N'

def test_case_6():
	cut = calorie_intake_calc(198.66,220.9,78,'F',0.54,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'

def test_case_7():
	cut = calorie_intake_calc(206.17,145.52,23,'M',-0.23,'E')
	cut.amount_exercise = 'S'
	cut.age = 36
	cut.gender = 'N'
	cut.age = 21
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 66.73
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 173.37
	cut.weight = 196.26

def test_case_8():
	cut = calorie_intake_calc(175.5,144.22,57,'F',0.3,'M')
	cut.height = 174.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 85
	cut.age = 60
	cut.age = 23

