from cut import *

def test_case_0():
	cut = calorie_intake_calc(81.98,140.7,79,'M',0.27,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 48.18

def test_case_1():
	cut = calorie_intake_calc(105.53,198.6,31,'F',0.06,'S')
	cut.gender = 'F'
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

