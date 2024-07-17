from cut import *

def test_case_0():
	cut = calorie_intake_calc(91.43,140.53,79,'F',-0.4,'V')
	cut.height = 156.06
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(105.26,145.54,51,'F',0.55,'E')
	cut.bodyfat = -0.12

def test_case_2():
	cut = calorie_intake_calc(59.49,196.06,38,'F',0.62,'S')

def test_case_3():
	cut = calorie_intake_calc(158.93,137.66,57,'M',0.32,'E')
	cut.age = 18

def test_case_4():
	cut = calorie_intake_calc(200.65,159.69,69,'M',0.75,'L')
	cut.amount_exercise = 'N'
	cut.age = 25
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 147.89

def test_case_5():
	cut = calorie_intake_calc(172.91,176.54,39,'F',0.28,'L')
	cut.age = 65
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 60.93

def test_case_6():
	cut = calorie_intake_calc(118.06,148.34,48,'N',-0.38,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_7():
	cut = calorie_intake_calc(87.69,166.44,82,'N',0.62,'E')
	cut.weight = 88.36
	cut.weight = 112.0
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_8():
	cut = calorie_intake_calc(126.56,150.92,56,'M',-0.46,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 72
	cut.age = 16

def test_case_9():
	cut = calorie_intake_calc(146.38,171.65,63,'N',0.51,'L')
	cut.age = 13

def test_case_10():
	cut = calorie_intake_calc(202.52,169.28,27,'M',-0.09,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_11():
	cut = calorie_intake_calc(172.53,155.68,50,'M',0.08,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_12():
	cut = calorie_intake_calc(126.05,155.81,21,'M',0.31,'M')
	cut.weight = 142.03
	cut.weight = 148.39
	result_tdee_calculation = cut.tdee_calculation()

def test_case_13():
	cut = calorie_intake_calc(144.81,149.92,11,'F',-0.5,'M')

def test_case_14():
	cut = calorie_intake_calc(168.34,183.67,85,'M',-0.48,'E')
	cut.weight = 129.37

