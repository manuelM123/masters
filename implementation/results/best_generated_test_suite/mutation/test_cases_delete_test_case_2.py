from cut import *

def test_case_0():
	cut = calorie_intake_calc(166.58,146.82,79,'F',0.15,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 96.41
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()

