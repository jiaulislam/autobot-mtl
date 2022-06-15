from database import LocalSession
from models.change_model import ChangeRequest
from typing import List
from sqlalchemy import update


class Modifier:
    def __init__(self, listOfCr: str, status: str):
        self.listOfCr: List[str] = listOfCr.split(',')
        self.status = status

    def modify_all(self):
        if len(self.listOfCr):
            with LocalSession.begin() as session:
                for cr_no in self.listOfCr:
                    stmt = update(ChangeRequest).where(ChangeRequest.cr_no == cr_no).values(status=self.status)
                    session.execute(stmt) 

def update_status(cr_no: str, cr_status: str):
    with LocalSession.begin() as session:
        stmt = update(ChangeRequest).where(ChangeRequest.cr_no == cr_no).values(status=cr_status)
        session.execute(stmt)