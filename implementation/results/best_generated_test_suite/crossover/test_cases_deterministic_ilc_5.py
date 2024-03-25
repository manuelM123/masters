from cut import *

def test_case_0():
	cut = calorie_intake_calc(87.76,219.41,39,'M',0.18,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'V'
	cut.age = 40
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 74
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 134.47

def test_case_1():
	cut = calorie_intake_calc(147.34,175.63,75,'F',0.04,'V')
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(85.65,205.2,38,'N',0.07,'M')
	cut.weight = 126.72
	cut.bodyfat = 0.09
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'S'
	cut.age = 38
	cut.height = 196.36
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(63.74,162.51,78,'F',0.09,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 59.84
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 181.82
	cut.weight = 124.79
	cut.weight = 188.39

