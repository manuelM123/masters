from cut import *

def test_case_0():
	cut = calorie_intake_calc(133.52,182.75,14,'F',0.03,'V')
	cut.height = 212.49
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'
	cut.age = 73

def test_case_1():
	cut = calorie_intake_calc(111.7,181.14,64,'N',0.2,'V')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(55.57,201.78,40,'N',0.22,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.0

def test_case_3():
	cut = calorie_intake_calc(63.54,147.3,29,'M',0.15,'E')
	cut.bodyfat = 0.1
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 198.6
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.22
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'

def test_case_4():
	cut = calorie_intake_calc(139.72,198.35,73,'M',0.24,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 185.41
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'

