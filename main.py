from ics import Calendar, Event
import csv

# global variables, make sure you use file paths for your specific system
input_dir = "/Users/briancervantes/Documents/Programming/csv_files/"
output_dir = "/Users/briancervantes/Documents/Programming/ics_output/"
csv_list = []

# accessing csv data
def csv_to_dict(file, name):

    with open(file) as f:
        data = csv.DictReader(f)
        for line in data:

            if line["Puerta_izquerda"].lower() == name.lower():
                print(line["Puerta_izquerda"])
                csv_list.append(line)
            elif line["Puerta_derecha"].lower() == name.lower():
                print(line["Puerta_derecha"])
                csv_list.append(line)
            elif line["Auditorio_izquerda"].lower() == name.lower():
                print(line["Auditorio_izquerda"])
                csv_list.append(line)
            elif line["Auditorio_derecha"].lower() == name.lower():
                print(line["Auditorio_derecha"])
                csv_list.append(line)
            else:
                print("You dont have anything for the week of {}".format(line["Fecha"]))


# Creating Calendar Event
def schedule_event(event_name, event_date, event_time, file_output):

    calendar = Calendar()
    event = Event()
    event.name = event_name
    event.begin = event_date + " " + event_time # format should reflect "2023-01-01 19:00:00"

    calendar.events.add(event)
    print(calendar.events)
    with open(file_output, "w") as test_event:
        test_event.writelines(calendar.serialize_iter())

print("Please type the filename, remember this is case sensitive.")
file_name = input().strip()
input_file_path = input_dir + file_name
print("Please type the name of the person you are looking for.")
users_name = input().strip().lower()


csv_to_dict(input_file_path, users_name)

for line in csv_list:
    event_name = line["Puerta_izquerda"] + " at the outside door left, " + line["Puerta_derecha"] + " is at the outside door right, " + line["Auditorio_izquerda"] + " in the inside left, and " + line["Auditorio_derecha"] + " is in the inside right "
    event_date = line["Fecha"]
    event_time = line["Hora"]
    file_name = output_dir + event_date + event_time + ".ics"

    schedule_event(event_name, event_date, event_time, file_name)


