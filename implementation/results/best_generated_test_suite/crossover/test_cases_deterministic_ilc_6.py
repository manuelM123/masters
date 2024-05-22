from cut import *

def test_case_0():
	cut = calorie_intake_calc(70.94,207.73,47,'F',0.13,'V')
	cut.amount_exercise = 'L'
	cut.height = 218.48
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(51.53,203.41,13,'M',0.22,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 49.37

def test_case_2():
	cut = calorie_intake_calc(47.4,179.6,11,'M',0.44,'S')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.height = 199.07
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 176.15

def test_case_3():
	cut = calorie_intake_calc(171.82,194.69,8,'N',-0.24,'L')
	cut.bodyfat = 0.65
	cut.weight = 157.25
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.18
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'

def test_case_4():
	cut = calorie_intake_calc(64.91,161.52,69,'N',0.44,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_5():
	cut = calorie_intake_calc(126.08,167.95,49,'M',0.11,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 71.39
	cut.age = 11
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 146.33
	cut.height = 135.53
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(66.18,198.41,34,'N',-0.04,'N')
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 42
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 47

def test_case_7():
	cut = calorie_intake_calc(208.42,192.08,12,'M',-0.18,'E')
	cut.amount_exercise = 'S'
	cut.age = 52
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_8():
	cut = calorie_intake_calc(70.15,146.11,54,'M',0.27,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.31
	cut.height = 201.24
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'

def test_case_9():
	cut = calorie_intake_calc(36.29,157.49,69,'M',0.63,'E')
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 164.34
	cut.gender = 'F'

