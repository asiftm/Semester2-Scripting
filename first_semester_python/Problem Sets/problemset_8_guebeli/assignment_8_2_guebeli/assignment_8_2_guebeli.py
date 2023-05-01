people = [
    {"name": "Sarah Taylor", "height": 1.88, "weight": 52, "gender": "female"},
    {"name": "Daniel Mitchell", "height": 1.53, "weight": 45, "gender": "male"},
    {"name": "Jess Rodriguez", "height": 1.55, "weight": 57, "gender": "female"},
    {"name": "Lisa Moore", "height": 1.64, "weight": 95, "gender": "female"},
    {"name": "Robert Martinez", "height": 1.64, "weight": 72, "gender": "male"},
    {"name": "Patricia White", "height": 1.79, "weight": 80, "gender": "female"},
    {"name": "Carol Thomas", "height": 1.68, "weight": 96, "gender": "female"},
    {"name": "Andrew Hill", "height": 1.77, "weight": 69, "gender": "male"},
    {"name": "Carol Allen", "height": 1.76, "weight": 85, "gender": "female"},
    {"name": "Edward Mitchell", "height": 1.77, "weight": 59, "gender": "male"},
    {"name": "Andrew Robinson", "height": 1.69, "weight": 102, "gender": "male"},
    {"name": "Edward Robinson", "height": 1.64, "weight": 57, "gender": "male"},
    {"name": "Andrew Nelson", "height": 1.8, "weight": 102, "gender": "male"},
    {"name": "James Robinson", "height": 1.75, "weight": 67, "gender": "male"},
    {"name": "Ashley Nelson", "height": 1.7, "weight": 67, "gender": "female"},
    {"name": "Brian Roberts", "height": 1.82, "weight": 101, "gender": "male"},
    {"name": "Jennifer Wright", "height": 1.62, "weight": 107, "gender": "female"},
    {"name": "George Lee", "height": 1.76, "weight": 79, "gender": "male"},
    {"name": "Donna Perez", "height": 1.79, "weight": 73, "gender": "female"},
    {"name": "Emily Brown", "height": 1.92, "weight": 56, "gender": "female"},
    {"name": "Michael Hernandez", "height": 1.92, "weight": 47, "gender": "male"},
    {"name": "George Martin", "height": 1.78, "weight": 67, "gender": "male"},
    {"name": "Jess Mitchell", "height": 1.76, "weight": 76, "gender": "female"},
    {"name": "Sarah Lewis", "height": 1.55, "weight": 88, "gender": "female"},
    {"name": "Sandra Clark", "height": 1.51, "weight": 82, "gender": "female"},
    {"name": "Brian Rivera", "height": 1.7, "weight": 66, "gender": "male"},
    {"name": "Sandra Williams", "height": 1.8, "weight": 71, "gender": "female"},
    {"name": "Mary Roberts", "height": 1.91, "weight": 73, "gender": "female"},
    {"name": "Mary Harris", "height": 1.62, "weight": 72, "gender": "female"},
    {"name": "Edward Davis", "height": 1.53, "weight": 89, "gender": "male"},
    {"name": "Jess Williams", "height": 1.73, "weight": 71, "gender": "female"},
    {"name": "Brian Perez", "height": 1.86, "weight": 70, "gender": "male"},
    {"name": "Matthew Scott", "height": 1.64, "weight": 72, "gender": "male"},
    {"name": "Robert Lopez", "height": 1.66, "weight": 47, "gender": "male"},
    {"name": "John Flores", "height": 1.72, "weight": 60, "gender": "male"},
    {"name": "Patricia Adams", "height": 1.78, "weight": 71, "gender": "female"},
    {"name": "Emily Jones", "height": 1.58, "weight": 85, "gender": "female"},
    {"name": "James King", "height": 1.91, "weight": 59, "gender": "male"},
    {"name": "Margaret Allen", "height": 1.68, "weight": 59, "gender": "female"},
    {"name": "George Nguyen", "height": 1.79, "weight": 91, "gender": "male"},
]


def bmi_calculator(data):
    for person in data:
        person["bmi"] = person["weight"]/(person["height"]**2)
    return data


def bmi_highest(data):
    data = bmi_calculator(data)
    hp = data[0]
    for person in data:
        if person["bmi"] > hp["bmi"]:
            hp = person
    return hp


def bmi_lowest(data):
    data = bmi_calculator(data)
    lp = data[0]
    for person in data:
        if person["bmi"] < lp["bmi"]:
            lp = person
    return lp


def bmi_average(data):
    data = bmi_calculator(data)
    total = 0
    for person in data:
        total += person["bmi"]
    return round(total/len(data))


def bmi_average_male(data):
    data = bmi_calculator(data)
    total = 0
    count = 0
    for person in data:
        if person["gender"] == "male":
            total += person["bmi"]
            count += 1
    return round(total/count)


def bmi_average_female(data):
    data = bmi_calculator(data)
    total = 0
    count = 0
    for person in data:
        if person["gender"] == "female":
            total += person["bmi"]
            count += 1
    return round(total/count)


def bmi_print(person):
    print(f"Name: {person['name']}, Height: {person['height']}, Weight: {person['weight']}, Gender: {person['gender']}, "
          f"BMI: {person['bmi']}")


if __name__ == '__main__':
    people = bmi_calculator(people)
    print("First 5 BMI:")
    for i in range(5):
        bmi_print(people[i])
    print("\nHighest BMI:")
    bmi_print(bmi_highest(people))
    print("\nLowest BMI:")
    bmi_print(bmi_lowest(people))
    print(f"\nAverage BMI:\t\t{bmi_average(people)}")
    print(f"Average Male BMI:\t{bmi_average_male(people)}")
    print(f"Average Female BMI:\t{bmi_average_female(people)}")
