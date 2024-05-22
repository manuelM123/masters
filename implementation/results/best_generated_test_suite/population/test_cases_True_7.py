from cut import *

def test_case_0():
	cut = calorie_intake_calc(212.9,147.1,83,'F',0.76,'M')
	cut.age = 24

def test_case_1():
	cut = calorie_intake_calc(48.61,166.34,60,'F',0.29,'L')
	cut.gender = 'M'
	cut.age = 57
	cut.height = 208.19
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(205.75,162.07,81,'N',-0.38,'V')
	cut.age = 54
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.weight = 84.28
	cut.weight = 167.89
	cut.amount_exercise = 'M'
	cut.age = 59

def test_case_3():
	cut = calorie_intake_calc(72.71,194.3,6,'M',0.69,'M')
	cut.gender = 'M'
	cut.amount_exercise = 'V'
	cut.age = 73
	cut.gender = 'M'
	cut.bodyfat = 0.58
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.66
	cut.gender = 'N'

def test_case_4():
	cut = calorie_intake_calc(83.56,219.66,31,'N',0.19,'V')
	cut.age = 6
	cut.gender = 'M'
	cut.weight = 131.58
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(97.16,140.03,21,'M',0.39,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'

def test_case_6():
	cut = calorie_intake_calc(81.82,208.05,59,'N',0.73,'E')
	cut.bodyfat = -0.06
	cut.gender = 'F'
	cut.gender = 'N'

def test_case_7():
	cut = calorie_intake_calc(195.48,199.4,70,'F',-0.22,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'M'

def test_case_8():
	cut = calorie_intake_calc(69.04,163.68,78,'M',-0.17,'M')
	cut.age = 27
	cut.height = 179.23
	result_tdee_calculation = cut.tdee_calculation()

def test_case_9():
	cut = calorie_intake_calc(164.64,163.84,83,'M',0.3,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 16
	cut.weight = 139.05
	cut.age = 15
	cut.bodyfat = 0.76
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 57
	cut.age = 5
	cut.gender = 'M'

