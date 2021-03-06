from rich import print
import datetime

from actions.action import (
    CreateNewChangeRequest,
    CloseChangeRequest,
    CancelChangeRequests,
    ParserLDMA,
)
from prettify import prettify_ldma
from prettify.driver_prettify import MenuLayout, get_menu_choice
from sys import exit
# from utilites.db import export_data

from xlsx_writer.writer import Writer

"""
Module Name: Autobot.py
----------------------
This is the main class for running the application. From here
all the functions can be called. This will be the user interface
from here. User's will choose the actions to do on BMC Remedy.

written by: jiaul_islam
"""


def get_advance_date() -> str:
    return (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%d-%b-%Y")


def main():
    """The typical main function to start the program"""
    try:
        while True:
            print(MenuLayout())
            choice: int = get_menu_choice()
            if choice == 1:
                # Create Change Request
                create = CreateNewChangeRequest()
                create.createRequest()
                create.tearDownDriver()
                break
            elif choice == 2:
                # Close Change Request
                close = CloseChangeRequest()
                close.closeRequest()
                close.tearDownDriver()
                break
            elif choice == 3:
                # Cancel Change Request
                cancel = CancelChangeRequests()
                cancel.cancelRequests()
                cancel.tearDownDriver()
                break
            elif choice == 4:
                # Parse Link Budget from LDMA
                while True:
                    print(prettify_ldma.MainMenuLayout())
                    choice: int = prettify_ldma.get_choice()
                    if choice == 1:
                        LinkID = input("\nPlease Enter LinkID: ")
                        link_ids = LinkID.split(",")
                        parse = ParserLDMA()
                        parse.parseLDMA(link_ids=link_ids)
                        parse.tearDownDriver()
                    elif choice == 2:
                        site_id = input("\nPlease Enter SiteID: ")
                        site_ids = site_id.split(",")
                        parse = ParserLDMA()
                        parse.parseLDMA(site_ids=site_ids)
                        parse.tearDownDriver()
                    elif choice == 0:
                        break
            elif choice == 5:
                _date: str = get_advance_date()
                db_data: list = export_data(_date)
                try:
                    with Writer(f"{_date}_GENARATED_CR.xlsx") as writer:
                        writer.write_to_excel(db_data)
                        print(f"\nExported data to {writer.file_name}")
                except Exception as e:
                    raise e
                break
            elif choice == 0:
                break
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
