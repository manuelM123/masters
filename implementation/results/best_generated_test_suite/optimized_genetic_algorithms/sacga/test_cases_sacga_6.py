from cut import *

def test_case_0():
	cut = calorie_intake_calc(209.67,142.48,70,'N',0.6,'S')
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 174.89
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(53.64,189.77,50,'F',-0.38,'E')
	cut.weight = 90.53
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 167.3

def test_case_2():
	cut = calorie_intake_calc(192.73,163.09,13,'F',-0.09,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'

def test_case_3():
	cut = calorie_intake_calc(207.15,219.83,24,'N',0.5,'M')
	cut.age = 36
	cut.height = 160.84

def test_case_4():
	cut = calorie_intake_calc(138.5,199.24,47,'F',0.18,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 143.26
	result_tdee_calculation = cut.tdee_calculation()

def test_case_5():
	cut = calorie_intake_calc(183.22,190.01,26,'F',0.19,'N')

def test_case_6():
	cut = calorie_intake_calc(108.2,217.8,36,'F',-0.17,'E')
	cut.height = 209.67
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 96.9
	cut.amount_exercise = 'M'

def test_case_7():
	cut = calorie_intake_calc(131.1,202.61,33,'M',-0.14,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 7

def test_case_8():
	cut = calorie_intake_calc(35.0,223.6,83,'F',0.16,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	cut.bodyfat = -0.02
	result_tdee_calculation = cut.tdee_calculation()

def test_case_9():
	cut = calorie_intake_calc(48.43,173.32,60,'M',-0.39,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'

def test_case_10():
	cut = calorie_intake_calc(178.46,206.8,68,'M',-0.15,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 224.72

def test_case_11():
	cut = calorie_intake_calc(190.21,194.91,69,'N',0.62,'N')
	cut.height = 162.57
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_12():
	cut = calorie_intake_calc(195.68,208.03,82,'M',-0.24,'S')
	cut.height = 179.76
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'

def test_case_13():
	cut = calorie_intake_calc(206.23,187.42,62,'N',0.16,'N')
	cut.weight = 165.46
	cut.gender = 'M'
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

