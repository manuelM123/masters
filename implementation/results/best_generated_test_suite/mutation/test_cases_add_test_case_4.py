from cut import *

def test_case_0():
	cut = calorie_intake_calc(178.83,205.64,39,'F',0.75,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 55
	cut.gender = 'N'
	cut.age = 16
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(140.78,171.49,8,'F',-0.01,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(167.13,188.43,53,'F',-0.24,'L')
	cut.age = 35
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 165.29
	cut.age = 21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 174.15
	cut.weight = 39.3

def test_case_3():
	cut = calorie_intake_calc(78.03,170.43,18,'M',0.05,'L')
	cut.gender = 'F'
	cut.height = 155.48
	cut.weight = 147.99
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(134.73,153.25,11,'M',-0.04,'M')
	cut.weight = 108.89
	cut.bodyfat = -0.07
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 165.2
	cut.height = 138.49
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(54.57,202.46,16,'N',-0.24,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.age = 38
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 139.9

def test_case_6():
	cut = calorie_intake_calc(116.07,183.24,10,'M',0.66,'S')
	cut.gender = 'M'
	cut.age = 39
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 169.25
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.78

def test_case_7():
	cut = calorie_intake_calc(118.56,164.15,62,'N',0.56,'S')
	cut.height = 180.25
	cut.age = 74

def test_case_8():
	cut = calorie_intake_calc(160.86,145.84,10,'M',-0.03,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.13
	cut.amount_exercise = 'S'

def test_case_9():
	cut = calorie_intake_calc(147.25,213.91,73,'N',-0.21,'V')
	cut.bodyfat = 0.71
	cut.amount_exercise = 'E'
	cut.age = 9
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.29
	cut.gender = 'M'
	cut.bodyfat = 0.67
	result_tdee_calculation = cut.tdee_calculation()

def test_case_10():
	cut = calorie_intake_calc(41.15,207.45,54,'N',-0.4,'M')

def test_case_11():
	cut = calorie_intake_calc(157.13,147.33,50,'M',-0.5,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_12():
	cut = calorie_intake_calc(44.93,184.82,30,'F',0.06,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 207.53

def test_case_13():
	cut = calorie_intake_calc(123.05,172.8,33,'F',0.26,'E')
	cut.bodyfat = 0.39

def test_case_14():
	cut = calorie_intake_calc(120.15,193.55,77,'M',-0.38,'S')

def test_case_15():
	cut = calorie_intake_calc(176.13,212.57,17,'M',0.06,'V')
	cut.height = 181.96
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

def test_case_16():
	cut = calorie_intake_calc(210.42,161.52,70,'N',0.68,'L')
	cut.bodyfat = -0.36
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_17():
	cut = calorie_intake_calc(137.68,213.35,74,'M',-0.09,'E')
	cut.weight = 130.76
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 157.79
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

