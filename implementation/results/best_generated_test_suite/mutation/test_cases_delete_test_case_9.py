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
	cut = calorie_intake_calc(77.23,197.0,32,'N',-0.3,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 194.57
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
	cut = calorie_intake_calc(91.98,167.33,38,'M',0.25,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_6():
	cut = calorie_intake_calc(165.63,136.65,36,'N',-0.12,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.1
	cut.weight = 41.14
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 55
	cut.age = 77
	cut.gender = 'F'

