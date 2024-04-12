from cut import *

def test_case_0():
	cut = calorie_intake_calc(112.22,161.33,75,'M',0.24,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	cut.age = 32
	cut.gender = 'F'
	cut.age = 64

def test_case_1():
	cut = calorie_intake_calc(104.6,176.78,79,'F',0.29,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.24
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'

