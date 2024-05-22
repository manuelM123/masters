from cut import *

def test_case_0():
	cut = calorie_intake_calc(166.51,216.69,10,'F',-0.35,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 161.12
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.17
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.43
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(160.08,197.58,11,'M',0.09,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.height = 172.81
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	cut.height = 182.68
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 83

def test_case_2():
	cut = calorie_intake_calc(142.75,220.22,66,'M',-0.34,'V')
	cut.weight = 65.35
	cut.height = 209.2
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 103.75
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.32
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(53.81,175.74,30,'F',0.23,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 137.96
	cut.height = 161.33
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.44
	cut.height = 201.84
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(89.71,217.09,14,'N',-0.19,'M')
	cut.age = 57
	cut.gender = 'F'

def test_case_5():
	cut = calorie_intake_calc(107.86,213.48,60,'N',0.2,'L')
	cut.age = 85
	cut.weight = 99.46
	cut.age = 43
	cut.age = 70
	cut.weight = 127.84

def test_case_6():
	cut = calorie_intake_calc(125.36,189.48,73,'M',0.06,'S')
	cut.weight = 63.0
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	cut.age = 38
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 28
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 30

def test_case_7():
	cut = calorie_intake_calc(139.18,173.98,37,'F',0.56,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_8():
	cut = calorie_intake_calc(88.62,190.67,16,'F',0.64,'S')
	cut.height = 224.56
	cut.gender = 'F'
	cut.amount_exercise = 'L'
	cut.gender = 'F'
	cut.age = 17
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 16
	cut.bodyfat = 0.01
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_9():
	cut = calorie_intake_calc(84.7,205.65,43,'F',-0.26,'V')
	cut.gender = 'M'
	cut.weight = 48.33
	cut.age = 38
	cut.bodyfat = 0.07
	cut.gender = 'F'
	cut.amount_exercise = 'L'
	cut.age = 24

def test_case_10():
	cut = calorie_intake_calc(109.28,163.73,82,'N',0.43,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_11():
	cut = calorie_intake_calc(192.76,193.16,85,'M',0.45,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	cut.weight = 42.23
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_12():
	cut = calorie_intake_calc(192.5,168.82,6,'N',-0.18,'E')
	cut.amount_exercise = 'N'
	cut.bodyfat = -0.35
	cut.weight = 97.5
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 178.02

def test_case_13():
	cut = calorie_intake_calc(67.1,187.35,34,'F',-0.1,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.age = 43
	cut.gender = 'N'
	cut.age = 33
	cut.weight = 104.63

def test_case_14():
	cut = calorie_intake_calc(206.57,188.63,15,'M',-0.02,'N')
	cut.bodyfat = 0.55
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'

