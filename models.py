import db

from sqlalchemy import Column, Integer, String, Float, Numeric
from sqlalchemy.dialects.oracle import \
            BFILE, BLOB, CHAR, CLOB, DATE, \
            DOUBLE_PRECISION, FLOAT, INTERVAL, LONG, NCLOB, NCHAR, \
            NUMBER, NVARCHAR, NVARCHAR2, RAW, TIMESTAMP, VARCHAR, \
            VARCHAR2




class People_log(db.Base):
    __tablename__ = 'P_PEOPLE_LOG'
    MAN_ID_VIGENTE = Column(NUMBER, primary_key=True)
    MAND_ID_INSIS = Column(NUMBER)
    PATH_JSON = Column(VARCHAR2(1000))
    PATH_API = Column(VARCHAR2(1000))    
    TIMESTAMP_POST = Column(DATE)
    TIMESTAMP_GET = Column(DATE)
    ERROR_POST = Column(VARCHAR2(1000))
    ERROR_GET = Column(VARCHAR2(1000))
    STATUS = Column(VARCHAR2(50))

    __table_args__ = {'schema': 'INSIS_PEOPLE_V10_TRACE'}

    def __init__(self, MAN_ID_VIGENTE, MAND_ID_INSIS, PATH_JSON, PATH_API, TIMESTAMP_POST, TIMESTAMP_GET, ERROR_POST, ERROR_GET, STATUS):
        self.MAN_ID_VIGENTE = MAN_ID_VIGENTE
        self.MAND_ID_INSIS = MAND_ID_INSIS
        self.PATH_JSON = PATH_JSON
        self.PATH_API = PATH_API
        self.TIMESTAMP_POST = TIMESTAMP_POST
        self.TIMESTAMP_GET = TIMESTAMP_GET
        self.ERROR_POST = ERROR_POST
        self.ERROR_GET = ERROR_GET
        self.STATUS = STATUS
    def __repr__(self):
        return f'''People_log({self.MAN_ID_VIGENTE},{self.MAND_ID_INSIS}, {self.PATH_JSON}, {self.PATH_API}, 
                {self.TIMESTAMP_POST}, {self.TIMESTAMP_GET}, {self.ERROR_POST}, {self.ERROR_GET}, {self.STATUS})'''

    def __str__(self):
        return self.MAN_ID_VIGENTE



class People(db.Base):
    __tablename__ = 'P_PEOPLE'
    MAN_ID = Column(NUMBER, primary_key=True)
    MAN_COMP = Column(NUMBER)
    EGN = Column(VARCHAR2(50))
    NAME = Column(VARCHAR2(400))
    GNAME = Column(VARCHAR2(100))
    SNAME = Column(VARCHAR2(100))
    FNAME = Column(VARCHAR2(100))
    BIRTH_DATE= Column(DATE)
    SEX = Column(NUMBER(1,0))   
    NOTES = Column(VARCHAR2(200))
    NATIONALITY = Column(VARCHAR2(15))
    COMP_TYPE = Column(VARCHAR2(2))
    NAME_SUFFIX = Column(VARCHAR2(30))
    NAME_PREFIX = Column(VARCHAR2(30))
    DATA_SOURCE = Column(VARCHAR2(15))
    LANGUAGE = Column(VARCHAR2(15))
    HOME_COUNTRY = Column(VARCHAR2(2))
    REGISTRATION_DATE = Column(DATE)
    INDUSTRY_CODE = Column(VARCHAR2(50))
    SUB_INDUSTRY_CODE = Column(VARCHAR2(50))
    FISCAL_PERIOD = Column(NUMBER)
    CLASS_CODE = Column(VARCHAR2(50))
    CLASS_SUB_CODE = Column(VARCHAR2(50))
    ATTR1 = Column(VARCHAR2(50))
    ATTR2 = Column(VARCHAR2(50))
    ATTR3 = Column(VARCHAR2(50))
    ATTR4 = Column(VARCHAR2(50))
    ATTR5 = Column(VARCHAR2(50))
    UPDATE_DATE = Column(DATE)
    INSERT_DATE = Column(DATE)
    BATCH_ID = Column(NUMBER)

    def __init__(self, MAN_ID, MAN_COMP, EGN, NAME, GNAME, SNAME, FNAME, BIRTH_DATE, SEX, NOTES, NATIONALITY, COMP_TYPE, NAME_SUFFIX, 
                NAME_PREFIX, DATA_SOURCE, LANGUAGE, HOME_COUNTRY, REGISTRATION_DATE, INDUSTRY_CODE, SUB_INDUSTRY_CODE, FISCAL_PERIOD, 
                CLASS_CODE, CLASS_SUB_CODE, ATTR1, ATTR2, ATTR3, ATTR4, ATTR5, UPDATE_DATE, INSERT_DATE, BATCH_ID):
        self.MAN_ID  = MAN_ID
        self.MAN_COMP  = MAN_COMP
        self.EGN  = EGN
        self.NAME  = NAME
        self.GNAME  = GNAME
        self.SNAME  = SNAME
        self.FNAME  = FNAME
        self.BIRTH_DATE = BIRTH_DATE
        self.SEX  = SEX
        self.NOTES  = NOTES
        self.NATIONALITY  = NATIONALITY
        self.COMP_TYPE  = COMP_TYPE
        self.NAME_SUFFIX  = NAME_SUFFIX
        self.NAME_PREFIX  = NAME_PREFIX
        self.DATA_SOURCE  = DATA_SOURCE
        self.LANGUAGE  = LANGUAGE
        self.HOME_COUNTRY  = HOME_COUNTRY
        self.REGISTRATION_DATE  = REGISTRATION_DATE
        self.INDUSTRY_CODE  = INDUSTRY_CODE
        self.SUB_INDUSTRY_CODE  = SUB_INDUSTRY_CODE
        self.FISCAL_PERIOD  = FISCAL_PERIOD
        self.CLASS_CODE  = CLASS_CODE
        self.CLASS_SUB_CODE  = CLASS_SUB_CODE
        self.ATTR1  = ATTR1
        self.ATTR2  = ATTR2
        self.ATTR3  = ATTR3
        self.ATTR4  = ATTR4
        self.ATTR5  = ATTR5
        self.UPDATE_DATE  = UPDATE_DATE
        self.INSERT_DATE  = INSERT_DATE
        self.BATCH_ID  = BATCH_ID

    def __repr__(self):
        return f'''People( {self.MAN_ID}, {self.MAN_COMP}, {self.EGN},{self.NAME},{self.GNAME}, 
        {self.SNAME}, 
        {self.FNAME}, 
        {self.BIRTH_DATE},	 
        {self.SEX}, 
        {self.NOTES}, 
        {self.NATIONALITY}, 
        {self.COMP_TYPE}, 
        {self.NAME_SUFFIX}, 
        {self.NAME_PREFIX}, 
        {self.DATA_SOURCE}, 
        {self.LANGUAGE}, 
        {self.HOME_COUNTRY}, 
        {self.REGISTRATION_DATE}, 
        {self.INDUSTRY_CODE}, 
        {self.SUB_INDUSTRY_CODE}, 
        {self.FISCAL_PERIOD}, 
        {self.CLASS_CODE}, 
        {self.CLASS_SUB_CODE}, 
        {self.ATTR1}, 
        {self.ATTR2}, 
        {self.ATTR3}, 
        {self.ATTR4}, 
        {self.ATTR5}, 
        {self.UPDATE_DATE}, 
        {self.INSERT_DATE}, 
        {self.BATCH_ID})'''
    def __str__(self):
        return self.MAN_ID


