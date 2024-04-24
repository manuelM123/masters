from cut import *

def test_case_0():
	cut = calorie_intake_calc(210.37,181.16,66,'N',0.19,'V')
	cut.age = 72

def test_case_1():
	cut = calorie_intake_calc(87.1,162.31,75,'M',0.01,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(143.19,165.79,56,'M',0.12,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.12
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(140.03,183.8,21,'F',0.0,'N')
	cut.bodyfat = 0.04
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(95.08,163.77,62,'M',0.2,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.2
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'
	cut.weight = 52.92
	cut.height = 143.69
	cut.height = 141.05
	cut.weight = 68.04
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(187.85,142.98,58,'N',0.09,'V')
	cut.amount_exercise = 'N'

def test_case_6():
	cut = calorie_intake_calc(65.12,210.86,51,'N',0.2,'E')
	cut.height = 196.09
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 207.15
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	cut.gender = 'F'
	cut.gender = 'N'
	cut.weight = 186.5

def test_case_7():
	cut = calorie_intake_calc(144.68,205.89,15,'N',0.29,'M')

