from cut import *

def test_case_0():
	cut = calorie_intake_calc(110.39,153.92,61,'N',0.3,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 180.17

def test_case_1():
	cut = calorie_intake_calc(141.92,145.48,79,'M',-0.4,'N')
	cut.age = 30
	cut.age = 44
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(156.56,175.83,55,'F',-0.22,'S')

def test_case_3():
	cut = calorie_intake_calc(67.07,171.22,21,'M',-0.0,'L')
	cut.amount_exercise = 'V'

def test_case_4():
	cut = calorie_intake_calc(51.13,222.2,48,'N',0.03,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(174.5,175.86,32,'F',-0.16,'E')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_6():
	cut = calorie_intake_calc(185.25,152.92,50,'F',-0.25,'V')
	cut.weight = 75.36
	cut.height = 180.43
	cut.height = 157.68

def test_case_7():
	cut = calorie_intake_calc(152.83,203.64,25,'M',0.21,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.76

def test_case_8():
	cut = calorie_intake_calc(68.44,203.08,65,'N',0.47,'M')

def test_case_9():
	cut = calorie_intake_calc(173.19,167.84,11,'F',0.77,'E')

def test_case_10():
	cut = calorie_intake_calc(163.29,197.07,40,'F',-0.13,'L')
	cut.bodyfat = 0.36
	cut.height = 223.64
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_11():
	cut = calorie_intake_calc(138.47,159.47,57,'F',0.05,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 140.62
	cut.amount_exercise = 'N'
	cut.gender = 'M'

def test_case_12():
	cut = calorie_intake_calc(126.84,207.48,51,'F',-0.27,'N')

def test_case_13():
	cut = calorie_intake_calc(203.42,166.47,48,'F',-0.35,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 186.06

def test_case_14():
	cut = calorie_intake_calc(200.1,167.66,76,'F',0.62,'N')
	cut.height = 158.42
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 156.85
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_15():
	cut = calorie_intake_calc(211.22,186.74,11,'M',0.22,'N')
	cut.weight = 48.28

def test_case_16():
	cut = calorie_intake_calc(208.06,165.88,71,'N',0.56,'E')
	cut.amount_exercise = 'M'
	cut.bodyfat = 0.26
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

