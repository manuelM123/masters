from cut import *

def test_case_0():
	cut = calorie_intake_calc(104.91,195.59,64,'F',0.1,'E')
	cut.age = 45
	cut.weight = 114.44

def test_case_1():
	cut = calorie_intake_calc(150.07,148.58,16,'F',0.19,'M')
	cut.gender = 'M'
	cut.gender = 'M'
	cut.gender = 'M'
	cut.amount_exercise = 'S'

def test_case_2():
	cut = calorie_intake_calc(193.19,145.79,21,'F',0.23,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(113.71,180.67,10,'F',0.22,'L')
	cut.bodyfat = 0.15
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.gender = 'F'

def test_case_4():
	cut = calorie_intake_calc(112.43,174.16,19,'F',0.11,'M')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 100.46
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(188.34,206.86,45,'F',0.17,'M')
	cut.amount_exercise = 'L'
	cut.height = 146.69

def test_case_6():
	cut = calorie_intake_calc(128.22,156.12,56,'F',0.18,'S')

def test_case_7():
	cut = calorie_intake_calc(159.67,173.48,71,'F',0.2,'E')
	cut.weight = 142.64

def test_case_8():
	cut = calorie_intake_calc(196.91,163.17,33,'M',0.27,'S')
	cut.height = 213.7
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_9():
	cut = calorie_intake_calc(184.34,154.14,35,'M',0.23,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.17

