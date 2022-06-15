from database import engine, Base, LocalSession
from models.change_model import ChangeRequest


def create_db():
    Base.metadata.create_all(bind=engine)


def create_cr():
    cr1 = ChangeRequest(
        cr_no="CRQ000000474088",
        cr_date="31-Mar-22",
        project_name="DHK RRU 2100 Mod project",
        activity_details="TNSKP04-RX Diversity Lost, 3_B1_1 SFP RX power too high Near-end for RRU3",
        impact_list="TNSKP04",
        service_type="Service Effective",
        downtime_type="01:00 Hour",
        zone="e.co_Mymensingh",
        robi_pm="Muhammad Shahed",
        lsp_name="MTL",
        coordinator_name="Abdul Hannan",
        status="REQUEST FOR AUTHORIZATION",
    )
    cr2 = ChangeRequest(
        cr_no="CRQ000000474090",
        cr_date="31-Mar-22",
        project_name="DHK RRU 2100 Mod project",
        activity_details="DHSVR01-SFP Not Present, RRU-3 should be 10g",
        impact_list="DHSVR01",
        service_type="Service Effective",
        downtime_type="01:00 Hour",
        zone="e.co_Dhaka South",
        robi_pm="Fatema Binte Ahmed",
        lsp_name="MTL",
        coordinator_name="Abdul Hannan",
        status="REQUEST FOR AUTHORIZATION",
    )
    with LocalSession.begin() as session:
        session.add(cr1)
        session.add(cr2)


if __name__ == "__main__":
    create_db()
    # create_cr()
