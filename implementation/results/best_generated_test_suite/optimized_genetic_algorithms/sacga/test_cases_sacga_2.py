from cut import *

def test_case_0():
	cut = calorie_intake_calc(164.64,145.4,59,'M',0.25,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(35.18,186.82,78,'M',0.76,'L')
	cut.bodyfat = 0.76
	cut.height = 173.29
	cut.bodyfat = -0.23
	cut.weight = 89.97

def test_case_2():
	cut = calorie_intake_calc(35.18,186.82,78,'M',0.76,'L')
	cut.bodyfat = 0.76
	cut.height = 173.29
	cut.bodyfat = -0.23
	cut.weight = 89.97

def test_case_3():
	cut = calorie_intake_calc(57.27,176.01,31,'N',0.21,'M')
	cut.weight = 156.74
	cut.amount_exercise = 'E'
	cut.gender = 'F'

def test_case_4():
	cut = calorie_intake_calc(143.88,154.92,38,'M',-0.42,'M')
	cut.age = 73
	cut.bodyfat = 0.21
	result_tdee_calculation = cut.tdee_calculation()

def test_case_5():
	cut = calorie_intake_calc(60.68,222.27,82,'F',0.18,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(54.31,173.22,15,'F',-0.41,'L')
	cut.weight = 131.55
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_7():
	cut = calorie_intake_calc(116.79,201.85,35,'M',0.5,'S')

def test_case_8():
	cut = calorie_intake_calc(168.81,221.68,8,'F',0.54,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 188.63
	cut.weight = 74.24
	cut.height = 172.61

def test_case_9():
	cut = calorie_intake_calc(116.79,201.85,35,'M',0.5,'S')

def test_case_10():
	cut = calorie_intake_calc(75.89,210.46,16,'N',-0.46,'N')
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 138.97
	cut.bodyfat = 0.46

def test_case_11():
	cut = calorie_intake_calc(84.96,215.82,74,'N',0.44,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_12():
	cut = calorie_intake_calc(157.7,206.42,16,'F',0.58,'L')
	cut.bodyfat = 0.51
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.41

def test_case_13():
	cut = calorie_intake_calc(131.18,163.34,17,'F',-0.42,'V')
	cut.bodyfat = 0.61
	result_tdee_calculation = cut.tdee_calculation()

def test_case_14():
	cut = calorie_intake_calc(49.67,191.15,74,'M',0.1,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_15():
	cut = calorie_intake_calc(207.19,152.22,39,'F',-0.45,'S')
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_16():
	cut = calorie_intake_calc(59.88,211.43,61,'N',0.74,'V')
	cut.age = 30
	cut.age = 31

def test_case_17():
	cut = calorie_intake_calc(142.05,187.03,8,'M',0.41,'V')
	cut.bodyfat = 0.08

def test_case_18():
	cut = calorie_intake_calc(136.01,156.05,36,'M',0.2,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.amount_exercise = 'M'

def test_case_19():
	cut = calorie_intake_calc(117.53,208.97,33,'F',0.13,'M')
	cut.age = 53
	cut.weight = 102.31
	cut.amount_exercise = 'M'

def test_case_20():
	cut = calorie_intake_calc(87.51,140.67,10,'F',0.38,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 81.1

def test_case_21():
	cut = calorie_intake_calc(185.54,198.26,29,'F',0.07,'N')
	cut.weight = 182.63
	result_tdee_calculation = cut.tdee_calculation()

def test_case_22():
	cut = calorie_intake_calc(185.54,198.26,29,'F',0.07,'N')
	cut.weight = 182.63
	result_tdee_calculation = cut.tdee_calculation()

def test_case_23():
	cut = calorie_intake_calc(55.44,143.51,74,'F',0.68,'S')
	cut.weight = 183.62
	cut.height = 160.9

def test_case_24():
	cut = calorie_intake_calc(88.41,219.83,11,'N',0.56,'L')

def test_case_25():
	cut = calorie_intake_calc(114.66,160.97,46,'M',0.74,'L')
	cut.weight = 45.33
	cut.gender = 'N'

def test_case_26():
	cut = calorie_intake_calc(52.56,179.24,24,'N',0.68,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_27():
	cut = calorie_intake_calc(50.34,224.75,9,'M',0.72,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 68

def test_case_28():
	cut = calorie_intake_calc(192.91,210.42,16,'F',-0.37,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 62
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_29():
	cut = calorie_intake_calc(186.28,193.77,19,'N',-0.21,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_30():
	cut = calorie_intake_calc(70.21,143.56,37,'N',0.78,'L')
	cut.amount_exercise = 'L'
	cut.age = 73
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

