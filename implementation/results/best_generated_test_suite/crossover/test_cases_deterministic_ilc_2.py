from cut import *

def test_case_0():
	cut = calorie_intake_calc(95.74,170.07,59,'M',0.27,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(107.41,157.82,51,'N',0.23,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(50.31,183.55,80,'F',0.28,'N')
	cut.weight = 70.09
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

