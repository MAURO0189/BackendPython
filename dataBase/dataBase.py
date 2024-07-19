from sqlalchemy import create_engine, MetaData

engineBD = create_engine("mysql+pymysql://root:12345678@localhost:3306/markbotdb")

metaData = MetaData()

conetion = engineBD.connect()