from cut import *

def test_case_0():
	cut = calorie_intake_calc(54.98,143.45,72,'N',0.18,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.24

def test_case_1():
	cut = calorie_intake_calc(48.27,191.69,46,'N',0.18,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 57
	cut.bodyfat = 0.25
	cut.age = 40

def test_case_2():
	cut = calorie_intake_calc(77.33,160.54,58,'M',0.18,'N')
	cut.weight = 139.18
	cut.gender = 'M'
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(173.45,166.39,10,'F',0.1,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.23
	cut.bodyfat = 0.22
	cut.amount_exercise = 'V'
	cut.height = 210.58
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(138.89,205.39,45,'N',0.08,'E')
	cut.weight = 76.52
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.amount_exercise = 'N'
	cut.height = 181.36

def test_case_5():
	cut = calorie_intake_calc(52.58,196.05,60,'M',0.29,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.gender = 'M'

def test_case_6():
	cut = calorie_intake_calc(162.5,140.89,64,'F',0.11,'L')
	cut.age = 67
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.07
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 41

def test_case_7():
	cut = calorie_intake_calc(102.03,190.21,37,'F',0.02,'E')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 21
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_8():
	cut = calorie_intake_calc(89.06,146.62,58,'F',0.23,'S')
	cut.gender = 'N'
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_9():
	cut = calorie_intake_calc(90.74,214.06,19,'F',0.05,'N')
	cut.age = 69
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 212.2
	cut.weight = 205.45
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 162.52
	cut.bodyfat = 0.16
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.04
	result_tdee_calculation = cut.tdee_calculation()

def test_case_10():
	cut = calorie_intake_calc(167.36,214.57,71,'F',0.22,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 10
	cut.weight = 122.05

