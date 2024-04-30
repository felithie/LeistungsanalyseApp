import my_classes

persontest= my_classes.Person ("Max", "Mustermann")
subjecttest= my_classes.Subject("Max", "Mustermann", "m", "01.01.1990", "max@gmail.com")

print( persontest.__dict__, subjecttest.__dict__)

my_classes.Person.put(persontest)
my_classes.Subject.update_email(subjecttest)
