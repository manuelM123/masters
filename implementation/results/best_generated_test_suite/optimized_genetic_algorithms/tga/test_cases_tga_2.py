from cut import *

def test_case_0():
	cut = calorie_intake_calc(150.8,189.95,29,'M',0.04,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(159.24,201.71,17,'F',-0.1,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 171.86

def test_case_2():
	cut = calorie_intake_calc(91.87,168.79,78,'F',-0.15,'M')
	cut.amount_exercise = 'V'

