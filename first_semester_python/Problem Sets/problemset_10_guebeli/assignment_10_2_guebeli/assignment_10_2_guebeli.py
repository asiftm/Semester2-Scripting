

def import_csv(path):
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    lines = [x.strip().split(",") for x in lines]
    return lines


def convert(data):
    new_data = []
    for i in range(len(data)):
        new_data.append({})
        new_data[i]["name"] = data[i][0]
        new_data[i]["height"] = data[i][1]
        new_data[i]["weight"] = data[i][2]
        new_data[i]["gender"] = data[i][3]
    return new_data


def save_lines_csv(data, file):
    f = open(file, "w")

    title = ""
    for key in data[0].keys():
        title += key+","
    text = title[:-1]+"\n"

    for line in data:
        text += csv_format(line)+"\n"

    f.write(text)
    f.close()


def bmi_calculator(data):
    for person in data:
        person["bmi"] = int(person["weight"])/(float(person["height"])**2)
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


def csv_format(line):
    text = ""
    for value in line.values():
        text += str(value)+","
    return text[:-1]


if __name__ == '__main__':
    people = import_csv("people.csv")
    people = convert(people)

    save_lines_csv(bmi_calculator(people), "bmi.csv")
    save_lines_csv([bmi_highest(people)], "highest_bmi.csv")
    save_lines_csv([bmi_lowest(people)], "lowest_bmi.csv")

    average = [{}]
    average[0]["overall"] = bmi_average(people)
    average[0]["males"] = bmi_average_male(people)
    average[0]["females"] = bmi_average_female(people)
    save_lines_csv(average, "average_bmi.csv")





