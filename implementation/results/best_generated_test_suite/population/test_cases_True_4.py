from cut import *

def test_case_0():
	cut = calorie_intake_calc(56.85,218.46,32,'N',-0.28,'M')
	cut.weight = 165.67
	cut.height = 213.96

def test_case_1():
	cut = calorie_intake_calc(91.33,192.78,39,'M',-0.29,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'

def test_case_2():
	cut = calorie_intake_calc(104.72,179.24,17,'F',-0.07,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 80
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 139.86

def test_case_3():
	cut = calorie_intake_calc(112.91,196.2,27,'F',-0.4,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 24
	cut.weight = 44.0
	cut.height = 159.59
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 103.39

def test_case_4():
	cut = calorie_intake_calc(41.95,153.56,17,'F',-0.36,'E')
	cut.bodyfat = -0.25
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 146.7
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 195.19
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 190.4
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 81.66

def test_case_5():
	cut = calorie_intake_calc(120.05,224.68,51,'M',-0.37,'E')

def test_case_6():
	cut = calorie_intake_calc(61.54,143.21,36,'M',0.6,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 178.02
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_7():
	cut = calorie_intake_calc(84.61,171.2,66,'F',0.32,'S')

def test_case_8():
	cut = calorie_intake_calc(65.78,188.59,35,'M',0.15,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 181.78
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'

def test_case_9():
	cut = calorie_intake_calc(53.57,185.83,70,'N',-0.03,'M')
	cut.bodyfat = -0.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

