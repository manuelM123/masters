from cut import *

def test_case_0():
	cut = calorie_intake_calc(68.31,214.42,10,'M',0.01,'N')
	cut.gender = 'M'
	cut.bodyfat = 0.47
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.66
	cut.bodyfat = 0.6
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(188.38,145.31,8,'M',-0.4,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	cut.bodyfat = 0.53

def test_case_2():
	cut = calorie_intake_calc(211.25,205.8,53,'F',0.1,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.36
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 70.16
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(69.1,182.91,74,'M',0.77,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 224.82

def test_case_4():
	cut = calorie_intake_calc(195.71,155.3,58,'M',0.17,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.39
	cut.height = 167.16
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.66
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_5():
	cut = calorie_intake_calc(91.98,167.33,38,'M',0.25,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_6():
	cut = calorie_intake_calc(138.43,194.22,78,'F',-0.06,'E')
	cut.age = 59
	cut.height = 212.27
	cut.weight = 187.66
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 32
	cut.weight = 38.34

