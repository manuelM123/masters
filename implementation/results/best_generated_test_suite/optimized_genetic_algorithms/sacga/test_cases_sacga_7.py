from cut import *

def test_case_0():
	cut = calorie_intake_calc(146.86,148.6,56,'M',-0.34,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(114.36,190.34,28,'N',-0.07,'L')
	cut.age = 36

def test_case_2():
	cut = calorie_intake_calc(95.93,215.98,41,'F',-0.12,'V')
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'

def test_case_3():
	cut = calorie_intake_calc(186.82,202.34,62,'M',-0.48,'N')
	cut.age = 67

def test_case_4():
	cut = calorie_intake_calc(61.64,170.33,22,'M',-0.29,'V')
	cut.height = 186.56
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 156.66
	cut.height = 180.01

def test_case_5():
	cut = calorie_intake_calc(206.41,223.04,60,'M',-0.01,'E')

def test_case_6():
	cut = calorie_intake_calc(36.42,180.72,48,'M',-0.42,'N')
	cut.weight = 188.27
	result_tdee_calculation = cut.tdee_calculation()

def test_case_7():
	cut = calorie_intake_calc(81.27,174.78,56,'F',0.19,'S')
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'

def test_case_8():
	cut = calorie_intake_calc(182.37,204.22,35,'F',-0.09,'N')

def test_case_9():
	cut = calorie_intake_calc(78.56,156.72,60,'N',-0.35,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_10():
	cut = calorie_intake_calc(132.34,190.4,20,'F',-0.11,'S')
	cut.weight = 156.08
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 186.63
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_11():
	cut = calorie_intake_calc(153.18,211.24,68,'F',0.32,'L')
	cut.age = 50
	cut.height = 195.41
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 89.17

def test_case_12():
	cut = calorie_intake_calc(129.32,203.58,61,'N',-0.49,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

