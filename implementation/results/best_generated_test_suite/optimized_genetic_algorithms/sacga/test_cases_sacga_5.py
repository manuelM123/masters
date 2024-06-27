from cut import *

def test_case_0():
	cut = calorie_intake_calc(214.67,194.65,49,'M',0.23,'E')
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'L'
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(193.76,137.34,40,'F',0.45,'E')
	cut.weight = 103.23
	cut.bodyfat = 0.29
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(64.44,159.14,47,'F',-0.21,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	cut.weight = 94.66

def test_case_3():
	cut = calorie_intake_calc(201.21,199.94,64,'F',0.22,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 224.89

def test_case_4():
	cut = calorie_intake_calc(132.15,221.77,78,'M',-0.33,'S')
	cut.bodyfat = 0.79
	cut.amount_exercise = 'L'
	cut.age = 56
	cut.weight = 102.34

def test_case_5():
	cut = calorie_intake_calc(199.7,147.69,37,'N',-0.47,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.age = 22
	cut.weight = 114.92

def test_case_6():
	cut = calorie_intake_calc(113.07,164.77,48,'N',-0.3,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_7():
	cut = calorie_intake_calc(193.22,160.41,17,'M',-0.1,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.47
	cut.bodyfat = -0.42
	cut.bodyfat = -0.32

def test_case_8():
	cut = calorie_intake_calc(113.07,164.77,48,'N',-0.3,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_9():
	cut = calorie_intake_calc(133.33,162.31,58,'F',-0.33,'M')

def test_case_10():
	cut = calorie_intake_calc(193.22,160.41,17,'M',-0.1,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.47
	cut.bodyfat = -0.42
	cut.bodyfat = -0.32

def test_case_11():
	cut = calorie_intake_calc(120.5,187.14,66,'N',0.41,'N')
	cut.bodyfat = -0.43
	cut.gender = 'N'
	cut.amount_exercise = 'S'

def test_case_12():
	cut = calorie_intake_calc(151.34,164.64,63,'M',-0.38,'M')
	cut.height = 177.28
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_13():
	cut = calorie_intake_calc(176.48,223.82,7,'F',0.6,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_14():
	cut = calorie_intake_calc(179.86,155.84,74,'F',-0.18,'L')
	result_tdee_calculation = cut.tdee_calculation()

