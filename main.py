import my_functions
import my_classes

sex= input ("Geben sie Ihr Geschlecht an (m/f):")
first_name= input("Geben sie Ihren Vornamen an:")
last_name= input ("Geben sie ihren Nachnamen an:")
age = input ("Geben sie Ihr alter in Jahren an:")
age_years = int(age)
print(type(age_years))
print(age_years)

#if __name__=="__main__":
    #estimateHR = my_functions.estimate_max_hr(age_years, sex)


if __name__ == "__main__":
  person1= Person (self, first_name, last_name, sex, age_years, __dict__) 

    #person= my_functions.build_person(first_name, last_name, sex, age_years)
    #print(person)

experiment_name = input("Geben sie den Namen des Experiments an:")
supervisor = input("Geben sie den Namen des Superivisors an:")
date = input( "Geben sie das Datum von heute an:")
#subject = input("Geben sie den Namen des Teilnehmers an:")

if __name__ == "__main__":
  experiment1= Experiment (self,experiment_name, date, supervisor, subject, __dict1__)
    #experiment= my_functions.build_experiment(experiment_name, date, supervisor, person)
    #print(experiment)