import csv


class Person:

    def __init__(self, name, height, weight, gender, bmi=0):
        self.name = name
        self.height = float(height)
        self.weight = float(weight)
        self.gender = gender
        self.bmi = float(bmi)

    def calculate_bmi(self):
        self.bmi = self.weight / (self.height ** 2)

    def as_dict(self):
        return self.__dict__


class People:

    def __init__(self, people):
        self.people = people


    def calculate_people_bmi(self):
        for person in self.people:
            person.calculate_bmi()


    def calculate_highest_bmi(self):
        highest = self.people[0]
        for person in self.people:
            if person.bmi > highest.bmi:
                highest = person
        return highest


    def calculate_lowest_bmi(self):
        lowest = self.people[0]
        for person in self.people:
            if person.bmi < lowest.bmi:
                lowest = person
        return lowest


    def calculate_average_bmi(self):
        sum = 0

        for person in self.people:
            sum += person.bmi

        return sum / len(self.people)


    def calculate_male_average_bmi(self):
        sum = 0
        count = 0

        for person in self.people:
            if person.gender == "male":
                sum += person.bmi
                count += 1

        return sum / count


    def calculate_female_average_bmi(self):
        sum = 0
        count = 0

        for person in self.people:
            if person.gender == "female":
                sum += person.bmi
                count += 1

        return sum / count


    def as_dict(self):
        people = []

        for person in self.people:
            people.append(person.as_dict())

        return people


class FileInterface:


    def load_people(self, file):
        with open(file, newline='') as csvfile:
            people_csv = csv.reader(csvfile, delimiter=",")
            people_list = []

            for person in people_csv:
                people_list.append(Person(person[0], person[1], person[2], person[3]))

        return people_list


    def save_dict_to_csv(self, file, list_csv, fieldnames=None):
        if fieldnames is None:
            fieldnames = ["name", "height", "weight", "gender", "bmi"]

        with open(file, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            csv_writer.writeheader()
            csv_writer.writerows(list_csv)

            print(f"Data saved successfully in file: {file}")




if __name__ == '__main__':
    fi = FileInterface()
    people = People(fi.load_people("people.csv"))
    people.calculate_people_bmi()

    fi.save_dict_to_csv("bmi.csv", people.as_dict())
    fi.save_dict_to_csv("lowest_bmi.csv", [(people.calculate_lowest_bmi()).as_dict()])
    fi.save_dict_to_csv("highest_bmi.csv", [(people.calculate_highest_bmi()).as_dict()])

    fi.save_dict_to_csv("average_bmi.csv", [{"average": people.calculate_average_bmi(),
                                             "average_male": people.calculate_male_average_bmi(),
                                             "average_female": people.calculate_female_average_bmi()}],
                        fieldnames=["average", "average_male", "average_female"])



