def plant():
    # geef aan welke dag de tuinman moet komen
    dag_tuinman = int(input("welke dag moet de tuinman komen? "))
    # counter van aantal planten
    plant_counter = 1
    # counter van welke dag het is
    dag = 0
    # de range geeft het aantal dagen dat je wilt berekenen aan
    for i in range(100):
        # als het de dag is dat de tuinman langs moet komen
        if i == dag_tuinman:
            # de volgende tuinman dag is 3 dagen later
            dag_tuinman += 3
            # planten verdubbelen
            plant_counter = (plant_counter * 2)
            # print welke dag het is en het aantal planten
            print("dag", dag, ", aantal planten: ", plant_counter)
            dag += 1
            # als er minder dan 60 planten zijn word aantal planten 0
            # anders gaat die ver in de min
            if plant_counter < 60:
                print("de tuinman heeft 60 planten weg gehaald")
                plant_counter = 0
            # als er meer dan 60 planten zijn gaan er 60 vanaf
            else:
                print("de tuinman heeft 60 planten weg gehaald")
                plant_counter = plant_counter - 60
        # als het niet een tuinman dag is
        else:
            # aantal planten verdubbeld
            plant_counter = (plant_counter * 2)
            # print dag en aantal planten
            print("dag", dag, ", aantal planten: ", plant_counter)
            dag += 1


def main():
    plant()

main()


