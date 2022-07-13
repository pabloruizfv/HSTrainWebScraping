import configparser
from tkinter import *


def button_function(root, variables, origin_entry, destination_entry):
    """
    :return:
    """
    variables.append(origin_entry.get())
    variables.append(destination_entry.get())
    print(variables)


def main_function2(config_file_path):
    """
    :return:
    """
    icon_path = r"C:\Users\pablo\ProjectsData\HSTrainWebScraping\gui\train.ico"
    root = Tk()
    root.title('High Speed Train - Round Trip Finder')
    root.iconbitmap(icon_path)

    variables = []

    my_button = Button(root, text='Next', state="normal", padx=50,
                       command=lambda: button_function(root, variables,
                                                       origin_entry,
                                                       destination_entry))

    # my_entry = Entry(root, width=50, bg="green", fg="white", borderwidth=5)
    origin_label = Label(root, text='Origin')
    origin_entry = Entry(root)
    destination_label = Label(root, text='Destination')
    destination_entry = Entry(root)
    avlo_label = Label(root, text='AVLO')
    avlo_checkbutton = Checkbutton(root)
    ouigo_label = Label(root, text='OUGO')
    ouigo_checkbutton = Checkbutton(root)

    default_value = StringVar()
    default_value.set('1')

    origin_dropdown = OptionMenu(root, default_value, '1', '2', '3')

    # my_label.grid(row=0, column=0)
    origin_label.grid(row=0, column=0)
    origin_entry.grid(row=0, column=1)
    destination_label.grid(row=1, column=0)
    destination_entry.grid(row=1, column=1)
    avlo_label.grid(row=2, column=0)
    avlo_checkbutton.grid(row=2, column=1)
    ouigo_label.grid(row=3, column=0)
    ouigo_checkbutton.grid(row=3, column=1)
    origin_dropdown.grid(row=4, column=1)
    my_button.grid(row=10, column=0)
    root.mainloop()


if __name__ == '__main__':
    cfg_path = r"C:\Users\pablo\ProjectsData\HSTrainWebScraping\configuration_files\round_trip_finder.cfg"
    main_function2(cfg_path)
