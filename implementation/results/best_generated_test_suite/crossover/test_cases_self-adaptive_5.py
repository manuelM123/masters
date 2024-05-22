from cut import *

def test_case_0():
	cut = calorie_intake_calc(47.65,143.37,41,'N',-0.47,'L')
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 164.48
	cut.gender = 'F'
	cut.height = 221.19
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(127.85,178.35,72,'M',0.03,'N')
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 216.94
	cut.bodyfat = 0.32
	cut.gender = 'N'
	cut.height = 185.41

def test_case_2():
	cut = calorie_intake_calc(69.35,158.47,43,'F',-0.35,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 44
	cut.height = 223.05
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 219.49

def test_case_3():
	cut = calorie_intake_calc(163.48,154.78,74,'M',-0.1,'L')
	cut.age = 8
	cut.height = 180.94
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 90.63

def test_case_4():
	cut = calorie_intake_calc(163.48,154.78,74,'M',-0.1,'L')
	cut.age = 8
	cut.height = 180.94
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 90.63

def test_case_5():
	cut = calorie_intake_calc(108.0,219.89,75,'F',0.08,'V')
	cut.height = 176.23
	cut.height = 192.88
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 163.51
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(107.47,167.75,72,'M',-0.08,'M')
	cut.height = 196.14
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 172.38
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.age = 21
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'

def test_case_7():
	cut = calorie_intake_calc(79.68,147.33,40,'N',0.18,'N')
	cut.bodyfat = 0.5
	cut.weight = 106.98
	cut.height = 184.19
	cut.height = 189.6
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 162.5

def test_case_8():
	cut = calorie_intake_calc(197.42,152.22,30,'N',0.76,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_9():
	cut = calorie_intake_calc(96.52,190.65,20,'F',0.74,'L')
	cut.height = 224.21
	cut.amount_exercise = 'V'

def test_case_10():
	cut = calorie_intake_calc(104.01,150.27,75,'F',-0.24,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 106.46
	cut.gender = 'F'

def test_case_11():
	cut = calorie_intake_calc(181.56,178.47,39,'N',-0.07,'M')
	cut.height = 172.18
	cut.gender = 'F'
	cut.amount_exercise = 'M'
	cut.bodyfat = -0.27
	cut.height = 155.66
	cut.bodyfat = 0.74

def test_case_12():
	cut = calorie_intake_calc(93.14,216.73,41,'F',0.28,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 50
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_13():
	cut = calorie_intake_calc(151.05,221.62,40,'F',0.62,'M')
	cut.amount_exercise = 'E'
	cut.age = 67
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 51
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'

