from cut import *

def test_case_0():
	cut = calorie_intake_calc(137.6,165.19,39,'F',0.2,'M')
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 110.16
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	cut.height = 149.6
	cut.bodyfat = 0.04
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(173.66,143.69,20,'M',0.01,'S')
	cut.bodyfat = 0.15
	cut.age = 20
	cut.amount_exercise = 'N'
	cut.gender = 'N'
	cut.age = 19
	cut.weight = 178.34

def test_case_2():
	cut = calorie_intake_calc(51.35,183.54,29,'F',0.28,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'

def test_case_3():
	cut = calorie_intake_calc(82.22,209.4,75,'M',0.28,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 192.13
	cut.age = 47
	cut.age = 35
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.age = 69

