from cut import *

def test_case_0():
	cut = calorie_intake_calc(180.12,181.47,9,'F',0.48,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 56.67

def test_case_1():
	cut = calorie_intake_calc(163.26,193.21,9,'F',-0.04,'V')
	cut.weight = 56.55
	cut.weight = 145.79

def test_case_2():
	cut = calorie_intake_calc(49.32,182.49,76,'N',-0.23,'M')
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(85.96,199.31,18,'N',-0.11,'L')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(146.18,142.75,7,'N',0.22,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(73.35,163.89,78,'N',0.22,'M')
	cut.gender = 'M'
	cut.height = 169.07
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_6():
	cut = calorie_intake_calc(83.48,179.06,79,'N',-0.48,'S')
	cut.bodyfat = 0.31
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 43.7
	cut.height = 211.74

def test_case_7():
	cut = calorie_intake_calc(95.08,223.86,56,'M',0.09,'L')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_8():
	cut = calorie_intake_calc(98.57,145.51,21,'M',-0.02,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 57.66
	cut.age = 63
	result_tdee_calculation = cut.tdee_calculation()

def test_case_9():
	cut = calorie_intake_calc(150.97,210.88,66,'M',-0.21,'E')
	cut.gender = 'M'
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 6

def test_case_10():
	cut = calorie_intake_calc(46.62,204.87,82,'N',0.73,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_11():
	cut = calorie_intake_calc(148.08,139.32,58,'N',0.17,'L')
	cut.height = 183.64

def test_case_12():
	cut = calorie_intake_calc(196.49,176.59,72,'F',0.64,'N')
	cut.height = 187.4
	cut.age = 37

def test_case_13():
	cut = calorie_intake_calc(158.32,176.98,51,'M',0.25,'N')

def test_case_14():
	cut = calorie_intake_calc(141.79,183.73,30,'N',-0.24,'S')
	cut.weight = 144.09
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_15():
	cut = calorie_intake_calc(127.35,188.87,71,'M',0.26,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.36
	result_tdee_calculation = cut.tdee_calculation()

def test_case_16():
	cut = calorie_intake_calc(112.06,195.1,39,'M',0.55,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'

def test_case_17():
	cut = calorie_intake_calc(213.99,170.27,23,'M',-0.29,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 164.25
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_18():
	cut = calorie_intake_calc(109.61,194.2,17,'N',-0.45,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 39.52

def test_case_19():
	cut = calorie_intake_calc(102.41,165.96,42,'N',0.49,'S')
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_20():
	cut = calorie_intake_calc(168.79,171.15,32,'M',0.71,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'

def test_case_21():
	cut = calorie_intake_calc(35.79,160.4,40,'N',0.26,'L')

