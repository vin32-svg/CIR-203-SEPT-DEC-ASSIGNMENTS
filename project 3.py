patient_info=('Caleb','25','75mmHg','72bpm')
name=patient_info[0]
age=patient_info[1]
Blood_pressure=patient_info[2]
Heart_rate=patient_info[3]
print( '\npatient age is:',age)
print("\npatient heart rate is:",Heart_rate)
print("\nsafe for database keys,\npermanent records cannot be changed,\neasy access,\nordered")
patient_info_list=list(patient_info)
print(patient_info_list)
patient_info_list[3]="78bpm"
print(patient_info_list)
patient_info=tuple(patient_info_list)
print(patient_info)
patient=(("millicent",20),
                  (" shiundu",30),
                  ("davis",40),
                  (" Lewis",35),
                  (" njeri",27))

names=tuple(patient[0]for patient in patient)
print(names)



