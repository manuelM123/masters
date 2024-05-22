from cut import *

def test_case_0():
	cut = calorie_intake_calc(111.82,168.04,27,'M',0.63,'L')
	cut.bodyfat = -0.32
	cut.bodyfat = 0.55
	cut.height = 152.2
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(107.78,194.47,66,'F',0.54,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 199.75
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 198.88

def test_case_2():
	cut = calorie_intake_calc(154.83,189.6,32,'F',-0.07,'E')
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.age = 65
	cut.height = 188.65
	cut.age = 36
	cut.bodyfat = 0.02
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(154.83,189.6,32,'F',-0.07,'E')
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.age = 65
	cut.height = 188.65
	cut.age = 36
	cut.bodyfat = 0.02
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(129.67,182.87,62,'M',-0.3,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.59
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 208.47

def test_case_5():
	cut = calorie_intake_calc(100.05,165.62,45,'F',-0.05,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	cut.weight = 168.24
	cut.weight = 189.79
	cut.amount_exercise = 'S'
	cut.gender = 'M'
	cut.gender = 'F'

def test_case_6():
	cut = calorie_intake_calc(133.25,176.0,40,'F',0.78,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.42
	cut.bodyfat = -0.18
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 202.76
	cut.gender = 'M'
	cut.age = 70
	cut.height = 193.95
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_7():
	cut = calorie_intake_calc(134.6,143.73,50,'M',0.6,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'
	cut.height = 179.28
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'

def test_case_8():
	cut = calorie_intake_calc(50.47,165.17,54,'F',0.33,'S')
	cut.bodyfat = 0.56
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.52

def test_case_9():
	cut = calorie_intake_calc(50.47,165.17,54,'F',0.33,'S')
	cut.bodyfat = 0.56
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.52

def test_case_10():
	cut = calorie_intake_calc(195.19,169.45,7,'F',0.22,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	cut.weight = 121.18
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.42

def test_case_11():
	cut = calorie_intake_calc(115.54,141.08,48,'F',0.73,'E')
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 53

def test_case_12():
	cut = calorie_intake_calc(49.71,163.27,21,'F',0.15,'V')

def test_case_13():
	cut = calorie_intake_calc(85.84,209.8,41,'N',0.2,'E')
	cut.weight = 120.85
	cut.bodyfat = 0.37
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 180.41
	cut.weight = 64.16

def test_case_14():
	cut = calorie_intake_calc(158.31,206.02,75,'M',0.25,'S')
	cut.bodyfat = 0.19
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_15():
	cut = calorie_intake_calc(48.91,160.3,80,'N',0.2,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_16():
	cut = calorie_intake_calc(67.95,136.18,10,'N',-0.04,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.2
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.54
	cut.gender = 'M'
	cut.gender = 'M'
	cut.height = 177.6
	result_determine_calorie_intake = cut.determine_calorie_intake()

