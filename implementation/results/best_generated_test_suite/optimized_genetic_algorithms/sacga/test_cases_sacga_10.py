from cut import *

def test_case_0():
	cut = calorie_intake_calc(184.08,143.41,5,'F',0.0,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.0
	cut.bodyfat = 0.68

def test_case_1():
	cut = calorie_intake_calc(57.11,213.51,42,'F',0.56,'N')
	cut.height = 215.47

def test_case_2():
	cut = calorie_intake_calc(109.66,190.34,29,'N',0.52,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 204.45
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(89.74,220.41,51,'N',0.56,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.age = 59

def test_case_4():
	cut = calorie_intake_calc(199.2,148.52,63,'M',-0.19,'S')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_5():
	cut = calorie_intake_calc(81.53,175.5,42,'N',-0.11,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 209.36

def test_case_6():
	cut = calorie_intake_calc(196.06,187.02,39,'N',0.27,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.1
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_7():
	cut = calorie_intake_calc(87.52,187.87,24,'M',0.33,'S')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_8():
	cut = calorie_intake_calc(152.09,138.28,69,'N',0.29,'S')
	cut.weight = 104.89
	cut.amount_exercise = 'L'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_9():
	cut = calorie_intake_calc(119.16,194.27,59,'F',0.67,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_10():
	cut = calorie_intake_calc(129.55,178.19,12,'F',0.61,'N')
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 85

def test_case_11():
	cut = calorie_intake_calc(115.67,154.14,83,'M',-0.15,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'

def test_case_12():
	cut = calorie_intake_calc(67.57,149.37,48,'F',-0.18,'E')
	cut.age = 21
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 204.9

def test_case_13():
	cut = calorie_intake_calc(189.47,182.88,62,'M',0.3,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 187.82
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_14():
	cut = calorie_intake_calc(198.53,149.64,84,'F',-0.08,'E')
	cut.bodyfat = 0.51

def test_case_15():
	cut = calorie_intake_calc(134.89,181.09,30,'M',-0.16,'M')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_16():
	cut = calorie_intake_calc(71.0,185.46,54,'M',0.19,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

