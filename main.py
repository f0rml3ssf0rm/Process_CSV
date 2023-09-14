import pandas as pd


select = input("Would you like to 1.Open, 2.View or 3.Exit: ")

if select.startswith("1"):
    with open("data/data.csv", "r") as file:
        data = file.read()
        print(data)
        data_split = data.split(",")
        select = input("Would you like to 1.Create List, 2.Create Dictionary or 3.Exit: ")
        if select.startswith("1"):
            for i in range(len(data_split)):
                data_split[i] = data_split[i].replace("\n", "")
                data_split[i] = data_split[i].replace("Day", "")
                data_split[i] = data_split[i].replace("Temp", "")
                data_split[i] = data_split[i].replace("Mon", "")
                data_split[i] = data_split[i].replace("Tue", "")
                data_split[i] = data_split[i].replace("Wed", "")
                data_split[i] = data_split[i].replace("Thu", "")
                data_split[i] = data_split[i].replace("Fri", "")
                data_split[i] = data_split[i].replace("Sat", "")
                data_split[i] = data_split[i].replace("Sun", "")
            data_split.remove("")
            data_split.remove("")
            print(data_split)

        if select.startswith("2"):
            file = "data/data.csv"
            df = pd.read_csv(file)

            dictionary = df.to_dict(orient="records")
            print(dictionary)

if select.startswith("3"):
    exit()
