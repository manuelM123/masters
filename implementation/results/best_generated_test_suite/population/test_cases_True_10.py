from cut import *

def test_case_0():
	cut = calorie_intake_calc(107.5,210.49,49,'F',0.43,'E')

def test_case_1():
	cut = calorie_intake_calc(184.11,187.92,65,'M',0.02,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(183.3,194.49,21,'F',0.15,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.gender = 'F'

def test_case_3():
	cut = calorie_intake_calc(164.46,136.73,38,'F',0.29,'M')
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 162.04
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 45
	cut.weight = 153.98
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(194.72,183.93,70,'F',-0.24,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_5():
	cut = calorie_intake_calc(120.55,149.42,71,'M',-0.11,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 154.16
	cut.weight = 130.58
	cut.age = 21
	cut.age = 49
	cut.bodyfat = 0.55
	cut.bodyfat = 0.01
	cut.height = 156.94
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 116.26

def test_case_6():
	cut = calorie_intake_calc(202.68,147.61,15,'M',0.74,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.32
	cut.age = 14
	cut.height = 173.5
	cut.bodyfat = -0.41
	cut.gender = 'N'
	cut.height = 159.13
	cut.bodyfat = 0.45
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_7():
	cut = calorie_intake_calc(168.61,196.76,48,'M',0.75,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_8():
	cut = calorie_intake_calc(70.16,223.65,8,'N',0.31,'S')

def test_case_9():
	cut = calorie_intake_calc(75.63,153.97,48,'N',0.68,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'

