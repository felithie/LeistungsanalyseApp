import my_functions
import my_classes as mc

if __name__ == "__main__":
  sex= input ("Geben sie Ihr Geschlecht an (m/f):")
  first_name= input("Geben sie Ihren Vornamen an:")
  last_name= input("Geben sie ihren Nachnamen an:")
  birthdate = input("Geben sie Ihr Geburtsdatum an:")

  subject= mc.Subject(first_name, last_name, sex, birthdate)
  mc.Subject.save(subject, "subject.json")

  supervisor_vorname = input("Geben sie den Vornamen des Betreuers an:")
  supervisor_nachname = input("Geben sie den Nachnamen des Betreuers an:")

  supervisor= mc.Supervisor(supervisor_vorname, supervisor_nachname)
  mc.Supervisor.save(supervisor, "supervisor.json")

  experiment_name = input("Geben sie den Namen des Experiments an:")
  date = input( "Geben sie das Datum von heute an:")

  experiment1= mc.Experiment(experiment_name, date, supervisor.__dict__, subject.__dict__)
  mc.Experiment.save(experiment1, "experiment1.json")