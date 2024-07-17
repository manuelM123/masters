from cut import *

def test_case_0():
	cut = calorie_intake_calc(57.25,176.77,37,'N',-0.27,'N')
	cut.bodyfat = 0.27
	cut.height = 197.55
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(37.21,179.9,46,'N',0.77,'E')
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(103.53,212.44,39,'F',-0.48,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(44.45,186.25,19,'N',-0.12,'E')

def test_case_4():
	cut = calorie_intake_calc(180.29,183.76,20,'F',-0.44,'M')
	cut.height = 162.5
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(116.18,185.62,37,'M',-0.29,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_6():
	cut = calorie_intake_calc(57.46,180.86,20,'F',-0.29,'E')
	cut.gender = 'N'

def test_case_7():
	cut = calorie_intake_calc(170.58,218.83,44,'N',0.36,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_8():
	cut = calorie_intake_calc(91.67,150.38,27,'M',0.75,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.weight = 198.33
	cut.gender = 'N'

def test_case_9():
	cut = calorie_intake_calc(73.89,220.86,50,'M',-0.27,'E')
	cut.height = 201.22
	cut.height = 184.27
	cut.height = 152.95
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_10():
	cut = calorie_intake_calc(70.84,205.22,27,'N',0.31,'S')
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'

def test_case_11():
	cut = calorie_intake_calc(39.82,164.34,10,'N',0.18,'M')

def test_case_12():
	cut = calorie_intake_calc(117.74,187.13,80,'N',0.11,'N')
	cut.amount_exercise = 'V'

def test_case_13():
	cut = calorie_intake_calc(174.82,179.94,6,'M',0.53,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.27
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_14():
	cut = calorie_intake_calc(108.21,176.04,68,'F',0.09,'V')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_15():
	cut = calorie_intake_calc(164.5,204.87,79,'M',-0.38,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_16():
	cut = calorie_intake_calc(144.07,143.67,12,'N',0.26,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_17():
	cut = calorie_intake_calc(153.83,219.66,16,'N',-0.08,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_18():
	cut = calorie_intake_calc(189.51,219.25,34,'N',0.42,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_19():
	cut = calorie_intake_calc(61.87,209.46,74,'M',-0.1,'E')
	cut.gender = 'N'

def test_case_20():
	cut = calorie_intake_calc(118.43,153.34,73,'M',0.38,'E')
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'

def test_case_21():
	cut = calorie_intake_calc(109.13,202.59,19,'M',0.35,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 196.54
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_22():
	cut = calorie_intake_calc(167.31,213.11,85,'N',0.66,'M')
	cut.bodyfat = 0.27
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 210.4

def test_case_23():
	cut = calorie_intake_calc(152.78,144.13,18,'M',0.29,'V')
	cut.age = 19
	cut.amount_exercise = 'L'
	cut.height = 181.72
	cut.weight = 128.36

def test_case_24():
	cut = calorie_intake_calc(196.1,171.91,32,'N',0.28,'M')

def test_case_25():
	cut = calorie_intake_calc(67.05,205.14,15,'M',0.3,'E')
	result_tdee_calculation = cut.tdee_calculation()

