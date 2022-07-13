import configparser
from tkinter import *


def button_function(root):
    """
    :return:
    """
    my_label = Label(root, text='High Speed Train - Round Trip Finder')
    my_label.pack()


def main_function2(config_file_path):
    """
    :return:
    """
    icon_path = r"C:\Users\pablo\ProjectsData\HSTrainWebScraping\gui\train.ico"
    root = Tk()
    root.title('High Speed Train - Round Trip Finder')
    root.iconbitmap(icon_path)

    my_button = Button(root, text='Next', state="normal", padx=50,
                       command=lambda: button_function(root))

    # my_entry = Entry(root, width=50, bg="green", fg="white", borderwidth=5)
    o_station_label = Label(root, text='Origin station')
    o_station_entry = Entry(root)

    # my_label.grid(row=0, column=0)
    o_station_label.grid(row=0, column=0)
    o_station_entry.grid(row=0, column=1)
    my_button.grid(row=10, column=0)
    root.mainloop()


def main_function(config_file_path):
    """
    Main function of the OUIGO Web Scraping project. Reads a set of parameters
    from the configuration file, executes the request to the OUIGO website
    and writes the resulting information in an output file.
    :param config_file_path: (string) path to the configuration file.
    """
    # Load parameters from configuration file:
    parser = configparser.ConfigParser()
    parser.read(config_file_path)

    origin_station = parser.get("config", "origin_station")
    destination_station = parser.get("config", "destination_station")
    trip_days = [int(d) for d in parser.get("config", "trip_days").split(',')]
    travel_dates = \
        load_dates_inbetween(*parser.get("config",
                                         "travel_date_boundaries").split('-'))
    train_services_info_file_path = \
        parser.get("config", "train_services_info_file_path")
    output_path = parser.get("config", "output_path")

    available_go_trains = {}
    for line in DictReader(open(train_services_info_file_path, 'r'),
                           delimiter='|'):
        if line['origin_station'] == origin_station:
            if line['destination_station'] == destination_station:
                travel_date = line['travel_date']
                try:
                    price = float(line['price'].replace(',', '.').replace('€', ''))
                except ValueError:
                    continue
                if travel_date not in available_go_trains:
                    available_go_trains[travel_date] = []
                available_go_trains[travel_date].append(((line['departure_time'],
                                                         line['arrival_time']),
                                                         price, line['company'],
                                                         travel_date))

    available_return_trains = {}
    for line in DictReader(open(train_services_info_file_path, 'r'),
                           delimiter='|'):
        if line['origin_station'] == destination_station:
            if line['destination_station'] == origin_station:
                travel_date = line['travel_date']
                try:
                    price = float(line['price'].replace(',', '.').replace('€', ''))
                except ValueError:
                    continue
                if travel_date not in available_return_trains:
                    available_return_trains[travel_date] = []
                available_return_trains[travel_date].append(((line['departure_time'],
                                                         line['arrival_time']),
                                                         price, line['company'],
                                                             travel_date))
    '''
    #
    date_to_cheapest_trains = {}
    for date, trains in available_trains.items():
        cheapest_trains_day = [(('00:00','00:00'), float('inf'))]
        for train_info in trains:
            price = train_info[1]
            if price == cheapest_trains_day[0][1]:
                cheapest_trains_day.append(train_info)
            elif price < cheapest_trains_day[0][1]:
                cheapest_trains_day = [train_info]
        date_to_cheapest_trains[date] = cheapest_trains_day

    #
    combination_to_price = {}
    for go_date in travel_dates:
        if go_date in date_to_cheapest_trains:
            go_trains = date_to_cheapest_trains[go_date]

            return_date = go_date + trip_days  # TODO: bien
            if return_date in date_to_cheapest_trains:
                return_trains = date_to_cheapest_trains[return_date]
                combination_to_price[]
    '''
    combinations = {}

    for go_date in travel_dates:
        if go_date in available_go_trains:
            go_trains = available_go_trains[go_date]
            for t_day in trip_days:
                return_date = add_to_date(go_date, t_day)
                if return_date in travel_dates:
                    if return_date in available_return_trains:
                        return_trains = available_return_trains[return_date]

                        for go_train in go_trains:
                            for return_train in return_trains:
                                total_price = go_train[1] + return_train[1]
                                combinations[(go_train, return_train)] = total_price

    print( sorted(combinations.items(), key=lambda item: item[1]))

    max_i = 50  # TODO:
    max_price = float('inf')
    output_file = open(output_path,'w')
    i = 0
    for combi, price in sorted(combinations.items(), key=lambda item: item[1]):

        if i == max_i:
            max_price = price

        if price > max_price:
            break

        output_file.write('{}|{}€|'.format(i, price) +
                          '{}|{}€|{}|{}|{}|'
                          .format(combi[0][2], combi[0][1],
                                  combi[0][0][0], combi[0][3],
                                  origin_station) +
                           '{}|{}|'
                           .format(combi[0][0][1], destination_station ) +
                           '|{}|{}€|{}|{}|{}\n'
                           .format(combi[1][2], combi[1][1],
                                  combi[1][0][0], combi[1][3],
                                  destination_station) )
        '''
        output_file.write('Train combination {} ({}€): '.format(i, price) +
                          '{} train ({}€) starting at {} {} from {} '
                          .format(combi[0][2], combi[0][1],
                                  combi[0][0][0], combi[0][3],
                                  origin_station) +
                           'arriving at {} at {}, and return train '
                           .format(combi[0][0][1], destination_station ) +
                           'which is an {} ({}€) departing at {} {} from {} \n'
                           .format(combi[1][2], combi[1][1],
                                  combi[1][0][0], combi[1][3],
                                  destination_station) )
        '''

        i += 1

    output_file.close()


if __name__ == '__main__':
    cfg_path = r"C:\Users\pablo\ProjectsData\HSTrainWebScraping\configuration_files\round_trip_finder.cfg"
    main_function2(cfg_path)
