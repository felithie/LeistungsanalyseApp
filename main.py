import my_functions
import my_classes as mc

if __name__ == "__main__":
  sex= input ("Geben sie Ihr Geschlecht an (m/f):")
  first_name= input("Geben sie Ihren Vornamen an:")
  last_name= input ("Geben sie ihren Nachnamen an:")
  age = input ("Geben sie Ihr alter in Jahren an:")
  age_years = int(age)
  print(type(age_years))
  print(age_years)
  person1= mc.Person(first_name, last_name, sex, age_years)
  mc.Person.save(person1, "person.json")

  experiment_name = input("Geben sie den Namen des Experiments an:")
  supervisor = input("Geben sie den Namen des Superivisors an:")
  date = input( "Geben sie das Datum von heute an:")
  subject = input("Geben sie den Namen des Teilnehmers an:")

  experiment1= mc.Experiment(experiment_name, date, supervisor, subject)
  mc.Experiment.save(experiment1, "experiment1.json")