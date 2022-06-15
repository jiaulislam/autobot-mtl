from sqlalchemy import Column, Integer, String, Identity, DATE, func, Date, DateTime
from database import Base

class ChangeRequest(Base):
    __tablename__ = "change_requests"

    id = Column(Integer, primary_key=True, server_default=Identity())
    cr_no = Column(String(15), unique=True, nullable=False)
    cr_date = Column(Date(), nullable=False)
    project_name = Column(String(50), nullable=False)
    activity_details = Column(String(600), nullable=False)
    impact_list = Column(String(300), nullable=False)
    service_type = Column(String(30), nullable=False)
    downtime_type = Column(String(30), nullable=False)
    zone = Column(String(30), nullable=False)
    robi_pm = Column(String(30), nullable=False)
    lsp_name = Column(String(11), nullable=False)
    coordinator_name = Column(String(50), nullable=True)
    status = Column(String(50), nullable=False)

    created_at = Column(DateTime(timezone=True), nullable=False,server_default=func.sysdate())

    def __repr__(self):
        return f"<ChangeRequest id({self.id}) cr_no({self.cr_no}) lsp_name({self.lsp_name})>"