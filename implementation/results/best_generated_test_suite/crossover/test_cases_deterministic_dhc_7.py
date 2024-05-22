from cut import *

def test_case_0():
	cut = calorie_intake_calc(76.78,218.43,72,'M',0.6,'E')
	cut.gender = 'F'
	cut.height = 200.05
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.46

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(160.0,158.97,12,'M',-0.21,'V')
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(45.55,145.98,7,'M',0.43,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(144.42,224.32,18,'M',0.04,'N')
	cut.age = 71

def test_case_5():
	cut = calorie_intake_calc(91.75,170.4,49,'N',-0.4,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 171.64
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'

def test_case_6():
	cut = calorie_intake_calc(126.66,194.54,22,'F',0.47,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

