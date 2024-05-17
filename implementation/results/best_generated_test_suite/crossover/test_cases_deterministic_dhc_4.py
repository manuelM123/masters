from cut import *

def test_case_0():
	cut = calorie_intake_calc(111.72,196.88,68,'M',-0.33,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(167.74,152.73,59,'F',-0.3,'S')
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.height = 135.56
	cut.height = 193.43
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 192.46
	cut.age = 77
	cut.height = 206.46

def test_case_2():
	cut = calorie_intake_calc(139.27,196.09,57,'M',-0.12,'E')
	cut.age = 84
	cut.bodyfat = 0.63
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.height = 146.84
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'

def test_case_3():
	cut = calorie_intake_calc(214.7,147.88,30,'M',-0.47,'S')
	cut.age = 8
	cut.gender = 'N'

def test_case_4():
	cut = calorie_intake_calc(41.69,147.56,16,'N',-0.14,'L')
	cut.bodyfat = 0.09
	cut.weight = 185.35
	cut.gender = 'N'
	cut.age = 69
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.gender = 'N'
	cut.weight = 126.49
	cut.gender = 'M'

def test_case_5():
	cut = calorie_intake_calc(144.02,203.79,16,'M',0.02,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.1
	cut.weight = 172.0
	cut.age = 28

def test_case_6():
	cut = calorie_intake_calc(59.04,213.28,20,'F',0.7,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_7():
	cut = calorie_intake_calc(210.29,216.55,79,'N',-0.09,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 36
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.age = 46

def test_case_8():
	cut = calorie_intake_calc(122.62,198.53,15,'N',-0.39,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 92.76
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

