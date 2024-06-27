from cut import *

def test_case_0():
	cut = calorie_intake_calc(133.92,176.75,15,'F',-0.4,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(107.44,192.46,11,'N',0.2,'V')
	cut.weight = 194.87
	cut.height = 152.79
	cut.gender = 'M'
	cut.bodyfat = -0.23

def test_case_2():
	cut = calorie_intake_calc(188.28,147.37,71,'N',0.01,'M')
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 214.18

def test_case_3():
	cut = calorie_intake_calc(49.98,168.82,23,'M',-0.33,'V')
	cut.weight = 179.84
	cut.weight = 90.17
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(199.25,154.83,48,'M',-0.19,'N')
	cut.gender = 'M'
	cut.gender = 'N'

def test_case_5():
	cut = calorie_intake_calc(176.41,208.17,72,'M',0.21,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_6():
	cut = calorie_intake_calc(207.76,174.18,35,'M',-0.23,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_7():
	cut = calorie_intake_calc(40.34,198.53,20,'M',0.24,'N')
	cut.bodyfat = 0.28
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_8():
	cut = calorie_intake_calc(67.39,163.67,34,'M',0.22,'E')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_9():
	cut = calorie_intake_calc(69.93,224.31,34,'N',-0.1,'M')
	cut.age = 61
	cut.age = 40

def test_case_10():
	cut = calorie_intake_calc(145.74,155.72,51,'M',0.34,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.65

def test_case_11():
	cut = calorie_intake_calc(65.83,154.92,73,'N',0.31,'M')

def test_case_12():
	cut = calorie_intake_calc(36.85,215.78,64,'N',-0.22,'M')
	cut.bodyfat = 0.38
	cut.bodyfat = -0.04

def test_case_13():
	cut = calorie_intake_calc(63.04,151.82,36,'F',-0.32,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 184.21

