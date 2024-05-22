from cut import *

def test_case_0():
	cut = calorie_intake_calc(135.82,141.93,41,'F',-0.36,'S')
	cut.bodyfat = 0.27
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(188.92,168.59,72,'M',-0.36,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(198.33,163.46,49,'N',-0.5,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	cut.weight = 41.04
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.15

def test_case_3():
	cut = calorie_intake_calc(115.19,153.1,79,'M',-0.38,'E')
	cut.amount_exercise = 'E'
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.height = 142.38

def test_case_4():
	cut = calorie_intake_calc(61.96,155.55,48,'M',-0.13,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'
	cut.weight = 168.74
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(210.7,160.02,60,'F',0.75,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	cut.age = 75
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_6():
	cut = calorie_intake_calc(122.87,188.34,17,'F',0.33,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_7():
	cut = calorie_intake_calc(123.57,161.96,40,'M',0.26,'E')
	cut.bodyfat = 0.17
	cut.amount_exercise = 'L'
	cut.height = 221.72
	cut.age = 8
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_8():
	cut = calorie_intake_calc(163.96,175.83,54,'F',-0.43,'E')
	cut.age = 70
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_9():
	cut = calorie_intake_calc(54.8,197.95,26,'M',-0.24,'M')
	cut.height = 184.46
	cut.height = 181.45
	cut.height = 181.37
	cut.height = 184.01

def test_case_10():
	cut = calorie_intake_calc(188.81,148.5,17,'N',-0.1,'L')
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 40

def test_case_11():
	cut = calorie_intake_calc(136.96,137.21,47,'M',0.34,'S')
	cut.weight = 148.62
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.05
	cut.gender = 'N'
	cut.age = 46

def test_case_12():
	cut = calorie_intake_calc(123.45,168.1,26,'M',0.32,'L')
	cut.bodyfat = -0.12
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	cut.height = 205.25
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_13():
	cut = calorie_intake_calc(174.35,169.73,70,'M',0.28,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_14():
	cut = calorie_intake_calc(102.28,210.58,31,'F',-0.01,'S')
	cut.age = 64
	cut.age = 7
	cut.amount_exercise = 'N'
	cut.age = 6
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 207.59
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.bodyfat = -0.33
	cut.amount_exercise = 'S'

