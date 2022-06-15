from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DIALECT = "oracle"
SQL_DRIVER = "cx_oracle"
USERNAME = "jibon"  # enter your username
PASSWORD = "Cgj2mcftxy$#"  # enter your password
SERVICE = "xepdb1"  # enter the oracle db service name
tns = (
    "(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = localhost)(PORT = 1521))"
    "(CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = xepdb1)))"
)

ENGINE_PATH_WIN_AUTH = (
    DIALECT + "+" + SQL_DRIVER + "://" + USERNAME + ":" + PASSWORD + "@" + tns
)


engine = create_engine(ENGINE_PATH_WIN_AUTH, echo=True)

LocalSession = sessionmaker(bind=engine, future=True)

Base = declarative_base()
