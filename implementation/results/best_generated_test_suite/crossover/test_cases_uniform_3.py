from cut import *

def test_case_0():
	cut = calorie_intake_calc(174.04,184.64,53,'F',0.18,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 81.45

def test_case_1():
	cut = calorie_intake_calc(166.39,150.6,75,'M',0.02,'N')
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'S'
	cut.gender = 'M'
	cut.height = 146.59
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(120.9,145.11,52,'F',0.06,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 72
	cut.weight = 72.07

def test_case_3():
	cut = calorie_intake_calc(188.66,143.72,31,'F',0.2,'E')
	cut.height = 211.0
	cut.age = 80
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 64.57
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 72.08

def test_case_4():
	cut = calorie_intake_calc(148.93,218.33,48,'M',0.07,'S')
	cut.bodyfat = 0.22
	cut.amount_exercise = 'V'
	cut.weight = 201.47
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 213.55

