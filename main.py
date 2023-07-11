import db
from models import People,People_log
from datetime import date

def run():

    pp = People_log(1,1,'jjj','aa', date.today(),date.today(),'ddd','sss','500')
    db.session.add(pp)
    db.session.commit()
  



if __name__ == '__main__':
    consulta = db.session.query(People).count()
    run()
    print(consulta)