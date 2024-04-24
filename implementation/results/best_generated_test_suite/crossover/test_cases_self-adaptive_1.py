from cut import *

def test_case_0():
	cut = calorie_intake_calc(206.21,156.85,29,'F',0.25,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.15
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'E'
	cut.weight = 77.3
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(148.89,146.48,60,'F',0.03,'N')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 91.74
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(183.67,190.97,67,'N',0.06,'M')
	cut.bodyfat = 0.05
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 121.38
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.age = 63

def test_case_3():
	cut = calorie_intake_calc(87.39,211.1,41,'M',0.17,'L')
	cut.weight = 97.95
	cut.amount_exercise = 'E'
	cut.height = 176.26
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 154.93
	cut.bodyfat = 0.28
	cut.weight = 87.71

def test_case_4():
	cut = calorie_intake_calc(144.05,142.45,51,'F',0.25,'S')
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.29
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.02
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 52

def test_case_5():
	cut = calorie_intake_calc(175.7,218.29,73,'M',0.05,'E')
	cut.bodyfat = 0.12
	cut.age = 13
	cut.amount_exercise = 'M'
	cut.height = 173.48
	result_tdee_calculation = cut.tdee_calculation()

