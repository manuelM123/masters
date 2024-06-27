from cut import *

def test_case_0():
	cut = calorie_intake_calc(148.25,203.55,33,'M',0.5,'E')
	cut.bodyfat = -0.0
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(92.36,159.41,81,'N',0.18,'V')
	cut.weight = 155.55
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.29

def test_case_2():
	cut = calorie_intake_calc(199.93,195.31,71,'M',0.21,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.2
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 142.74

def test_case_3():
	cut = calorie_intake_calc(156.26,141.73,48,'F',-0.14,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	cut.height = 176.67

def test_case_4():
	cut = calorie_intake_calc(103.05,165.09,14,'N',-0.47,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

