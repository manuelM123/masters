from cut import *

def test_case_0():
	cut = calorie_intake_calc(154.92,214.96,38,'M',0.12,'N')

def test_case_1():
	cut = calorie_intake_calc(147.84,139.95,57,'N',-0.41,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 141.18
	cut.bodyfat = 0.48
	cut.gender = 'F'
	cut.weight = 187.73

def test_case_2():
	cut = calorie_intake_calc(80.78,174.86,69,'M',0.04,'E')
	cut.weight = 129.03
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.5
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 185.12
	cut.age = 58
	cut.amount_exercise = 'M'

def test_case_3():
	cut = calorie_intake_calc(66.38,139.36,53,'M',-0.14,'N')

def test_case_4():
	cut = calorie_intake_calc(38.97,149.32,14,'F',0.79,'E')

def test_case_5():
	cut = calorie_intake_calc(90.94,216.18,53,'N',0.8,'V')
	cut.amount_exercise = 'S'
	cut.height = 155.8
	cut.amount_exercise = 'L'
	cut.weight = 125.56

def test_case_6():
	cut = calorie_intake_calc(142.58,179.57,62,'M',-0.19,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 191.17
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 171.48
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.53

def test_case_7():
	cut = calorie_intake_calc(159.21,172.18,84,'F',0.01,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.31
	cut.gender = 'F'
	cut.height = 164.15
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_8():
	cut = calorie_intake_calc(151.33,154.42,51,'M',0.42,'N')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 176.19
	cut.weight = 54.54
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.65

def test_case_9():
	cut = calorie_intake_calc(128.22,208.83,47,'N',0.57,'N')
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

