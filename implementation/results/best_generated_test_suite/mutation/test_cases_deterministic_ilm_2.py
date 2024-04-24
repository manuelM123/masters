from cut import *

def test_case_0():
	cut = calorie_intake_calc(153.04,196.71,10,'F',0.13,'L')
	cut.age = 31
	cut.gender = 'F'
	cut.gender = 'N'
	cut.bodyfat = 0.17
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	cut.weight = 102.89
	cut.bodyfat = 0.26
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(207.99,157.96,50,'M',0.02,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(177.0,173.03,21,'F',0.08,'L')
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.04

def test_case_3():
	cut = calorie_intake_calc(52.09,161.82,65,'M',0.17,'N')
	cut.gender = 'N'
	cut.weight = 150.34
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.13
	cut.bodyfat = 0.03
	cut.gender = 'M'
	cut.age = 14
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(188.21,213.56,53,'N',0.03,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.02
	cut.weight = 157.06
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_5():
	cut = calorie_intake_calc(98.7,192.92,16,'F',0.22,'L')

def test_case_6():
	cut = calorie_intake_calc(128.55,148.01,47,'M',0.24,'L')
	cut.height = 198.29
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 97.3
	cut.age = 55
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 35

def test_case_7():
	cut = calorie_intake_calc(207.83,160.77,72,'F',0.13,'E')
	cut.age = 52
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.height = 179.07
	result_tdee_calculation = cut.tdee_calculation()

def test_case_8():
	cut = calorie_intake_calc(87.54,193.93,57,'F',0.29,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 166.59
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.29
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 72
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 79
	cut.age = 59

