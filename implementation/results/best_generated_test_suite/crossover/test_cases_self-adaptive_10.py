from cut import *

def test_case_0():
	cut = calorie_intake_calc(79.81,206.21,84,'N',0.5,'M')
	cut.amount_exercise = 'V'
	cut.height = 183.05
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 8
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 137.05
	cut.bodyfat = 0.45
	cut.gender = 'N'
	cut.height = 141.03

def test_case_1():
	cut = calorie_intake_calc(53.04,189.32,64,'M',0.0,'N')
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 87.93

def test_case_2():
	cut = calorie_intake_calc(199.2,181.75,79,'F',-0.1,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	cut.age = 42
	cut.amount_exercise = 'M'
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 158.61
	cut.weight = 168.25

def test_case_3():
	cut = calorie_intake_calc(53.04,189.32,64,'M',0.0,'N')
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 87.93

def test_case_4():
	cut = calorie_intake_calc(126.86,219.72,71,'M',0.29,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_5():
	cut = calorie_intake_calc(92.71,217.36,68,'F',0.16,'L')
	cut.height = 203.01
	cut.age = 32
	cut.height = 185.19
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.44

def test_case_6():
	cut = calorie_intake_calc(204.13,152.39,58,'N',-0.2,'L')
	cut.height = 204.15
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 115.35
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'

def test_case_7():
	cut = calorie_intake_calc(148.87,198.58,30,'M',-0.14,'S')
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 68.05
	cut.height = 160.56

def test_case_8():
	cut = calorie_intake_calc(54.96,209.13,18,'F',0.33,'E')
	cut.amount_exercise = 'L'
	cut.weight = 84.74
	cut.bodyfat = -0.41
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 50
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_9():
	cut = calorie_intake_calc(56.94,195.06,29,'M',-0.41,'E')
	cut.amount_exercise = 'E'
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_10():
	cut = calorie_intake_calc(70.75,221.58,30,'M',0.17,'M')
	cut.weight = 67.1
	cut.age = 68
	cut.height = 163.4
	cut.height = 150.62
	cut.height = 149.38
	cut.age = 56

def test_case_11():
	cut = calorie_intake_calc(211.09,221.91,55,'N',0.56,'E')
	cut.amount_exercise = 'S'
	cut.weight = 206.69
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 54
	cut.weight = 49.74
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_12():
	cut = calorie_intake_calc(46.35,144.97,78,'F',-0.38,'M')
	cut.amount_exercise = 'V'
	cut.height = 140.33
	cut.bodyfat = 0.12
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_13():
	cut = calorie_intake_calc(41.74,150.39,39,'N',0.03,'L')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_14():
	cut = calorie_intake_calc(114.0,207.78,53,'F',-0.37,'N')
	cut.amount_exercise = 'L'

def test_case_15():
	cut = calorie_intake_calc(183.59,195.24,42,'N',-0.39,'M')
	cut.bodyfat = 0.5
	cut.weight = 203.57
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.31
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

