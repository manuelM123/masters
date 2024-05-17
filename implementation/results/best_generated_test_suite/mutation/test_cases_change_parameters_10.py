from cut import *

def test_case_0():
	cut = calorie_intake_calc(191.85,171.27,74,'M',0.16,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.26
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(170.51,171.76,75,'N',-0.35,'V')
	cut.age = 64
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.weight = 90.89
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.age = 6
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(73.44,172.23,19,'N',0.47,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.69
	cut.weight = 80.92

def test_case_3():
	cut = calorie_intake_calc(142.28,140.23,59,'N',0.68,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(98.44,222.96,16,'F',-0.3,'E')
	cut.gender = 'M'
	cut.age = 71
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 144.43

def test_case_5():
	cut = calorie_intake_calc(82.45,166.62,54,'N',0.01,'E')
	cut.height = 192.66
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.32
	cut.age = 81
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 55.94
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 168.91

def test_case_6():
	cut = calorie_intake_calc(37.04,205.23,15,'N',0.29,'N')
	cut.weight = 61.72

def test_case_7():
	cut = calorie_intake_calc(102.74,196.13,83,'M',0.6,'N')
	cut.gender = 'M'

def test_case_8():
	cut = calorie_intake_calc(147.96,203.06,83,'N',0.52,'L')
	cut.height = 223.1
	cut.amount_exercise = 'M'
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_9():
	cut = calorie_intake_calc(107.1,149.34,79,'N',-0.02,'E')

