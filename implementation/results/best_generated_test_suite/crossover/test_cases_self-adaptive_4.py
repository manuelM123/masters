from cut import *

def test_case_0():
	cut = calorie_intake_calc(66.16,186.61,77,'M',-0.28,'L')
	cut.weight = 164.04
	cut.bodyfat = 0.21
	cut.height = 184.94
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'

def test_case_1():
	cut = calorie_intake_calc(86.65,204.98,5,'F',0.4,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 193.51
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.3
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(38.91,205.02,59,'N',0.29,'L')
	cut.bodyfat = 0.67
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 31
	cut.gender = 'N'
	cut.height = 207.9
	cut.height = 208.28
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(158.78,190.8,10,'N',-0.07,'N')
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(185.23,198.04,78,'M',0.2,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.14
	cut.age = 29
	cut.bodyfat = 0.39

def test_case_5():
	cut = calorie_intake_calc(55.69,145.6,61,'M',0.05,'V')
	cut.weight = 199.5
	cut.weight = 135.12
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.18
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_6():
	cut = calorie_intake_calc(202.75,167.8,12,'F',0.02,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'

def test_case_7():
	cut = calorie_intake_calc(100.39,156.22,44,'M',-0.36,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.64
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 164.94
	result_tdee_calculation = cut.tdee_calculation()

def test_case_8():
	cut = calorie_intake_calc(102.0,190.32,61,'M',-0.35,'N')
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.11
	cut.height = 187.15
	cut.height = 155.12

def test_case_9():
	cut = calorie_intake_calc(48.4,222.51,61,'F',0.23,'V')
	cut.bodyfat = -0.33
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	cut.gender = 'F'
	cut.age = 61
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 136.42
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 170.56

