from cut import *

def test_case_0():
	cut = calorie_intake_calc(167.14,145.33,83,'F',-0.13,'E')
	cut.bodyfat = 0.16
	cut.age = 15
	cut.bodyfat = -0.34
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 147.74
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.bodyfat = -0.16

def test_case_1():
	cut = calorie_intake_calc(202.36,195.5,36,'N',-0.04,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(71.16,182.07,49,'F',0.68,'L')
	cut.age = 83
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 142.22
	cut.height = 195.89
	cut.gender = 'M'

def test_case_3():
	cut = calorie_intake_calc(144.17,195.61,55,'F',-0.28,'V')
	cut.amount_exercise = 'S'
	cut.gender = 'N'
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 19
	cut.age = 41
	cut.gender = 'F'
	cut.weight = 90.37

def test_case_4():
	cut = calorie_intake_calc(194.29,197.37,20,'F',0.54,'S')
	cut.height = 146.46
	cut.gender = 'F'
	cut.age = 46
	cut.weight = 123.93
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 177.66

def test_case_5():
	cut = calorie_intake_calc(186.36,221.28,30,'F',-0.34,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 208.71
	cut.height = 179.42

def test_case_6():
	cut = calorie_intake_calc(214.61,155.28,22,'F',-0.32,'E')
	cut.bodyfat = 0.72
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.61
	cut.amount_exercise = 'V'
	cut.amount_exercise = 'V'

def test_case_7():
	cut = calorie_intake_calc(210.95,189.28,36,'N',0.11,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_8():
	cut = calorie_intake_calc(131.31,183.59,39,'M',0.3,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 17
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_9():
	cut = calorie_intake_calc(84.61,187.6,41,'N',-0.13,'S')
	cut.bodyfat = 0.07
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_10():
	cut = calorie_intake_calc(116.88,184.43,79,'M',0.09,'V')
	cut.age = 50
	cut.age = 43
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 123.72
	cut.weight = 66.53

def test_case_11():
	cut = calorie_intake_calc(207.27,182.32,50,'M',0.27,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 211.35
	cut.weight = 150.99
	cut.age = 60
	cut.gender = 'F'
	cut.bodyfat = -0.12

def test_case_12():
	cut = calorie_intake_calc(141.01,168.37,22,'M',-0.27,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 197.48
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_13():
	cut = calorie_intake_calc(74.09,153.32,36,'F',-0.07,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 67
	cut.age = 23
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 172.89

def test_case_14():
	cut = calorie_intake_calc(60.89,135.86,55,'N',-0.49,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 47.46
	cut.weight = 195.98

