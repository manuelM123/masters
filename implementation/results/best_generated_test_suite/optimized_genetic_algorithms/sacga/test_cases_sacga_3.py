from cut import *

def test_case_0():
	cut = calorie_intake_calc(122.74,156.97,76,'M',0.32,'V')
	cut.height = 165.67
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 84
	cut.age = 21

def test_case_1():
	cut = calorie_intake_calc(99.82,220.82,25,'M',0.06,'M')
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(120.69,212.96,41,'F',-0.04,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(100.78,172.41,47,'N',-0.21,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.gender = 'M'

def test_case_4():
	cut = calorie_intake_calc(209.04,140.1,35,'M',-0.13,'S')
	cut.bodyfat = 0.64
	cut.bodyfat = -0.23
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.46

def test_case_5():
	cut = calorie_intake_calc(134.35,177.29,11,'M',-0.4,'L')
	cut.weight = 57.79
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 51.86

def test_case_6():
	cut = calorie_intake_calc(162.84,184.41,37,'F',-0.19,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	cut.gender = 'N'
	cut.weight = 202.93

def test_case_7():
	cut = calorie_intake_calc(119.17,166.7,61,'M',0.19,'E')
	cut.age = 19
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'

def test_case_8():
	cut = calorie_intake_calc(200.53,218.11,77,'N',0.22,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 35.08
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_9():
	cut = calorie_intake_calc(127.2,139.08,19,'M',0.52,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 148.69

def test_case_10():
	cut = calorie_intake_calc(188.27,196.93,42,'F',0.19,'V')
	cut.height = 172.19
	cut.age = 68
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_11():
	cut = calorie_intake_calc(101.38,170.44,61,'N',-0.22,'E')
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 172.69

def test_case_12():
	cut = calorie_intake_calc(95.34,183.86,25,'F',-0.11,'N')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 73
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_13():
	cut = calorie_intake_calc(105.33,173.45,76,'N',0.75,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_14():
	cut = calorie_intake_calc(99.48,150.05,21,'N',-0.24,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_15():
	cut = calorie_intake_calc(131.45,200.21,76,'F',-0.05,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 77.65
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_16():
	cut = calorie_intake_calc(41.4,201.49,28,'F',-0.01,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_17():
	cut = calorie_intake_calc(36.28,204.86,14,'N',-0.42,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.33
	cut.gender = 'F'

def test_case_18():
	cut = calorie_intake_calc(60.56,138.73,67,'N',0.42,'V')
	cut.age = 19
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 191.85

def test_case_19():
	cut = calorie_intake_calc(145.69,194.17,55,'F',-0.45,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 82
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_20():
	cut = calorie_intake_calc(94.88,144.69,10,'M',-0.4,'L')
	cut.weight = 192.72
	cut.gender = 'M'
	cut.bodyfat = 0.06

