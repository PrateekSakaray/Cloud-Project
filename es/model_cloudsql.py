from flask import Flask
from flask_sqlalchemy import SQLAlchemy


builtin_list = list


db = SQLAlchemy()


def init_app(app):
    # Disable track modifications, as it unnecessarily uses memory.
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    db.init_app(app)


def from_sql(row):
    """Translates a SQLAlchemy model instance into a dictionary"""
    data = row.__dict__.copy()
    data['id'] = row.id
    data.pop('_sa_instance_state')
    return data


# [START model]
class Airport(db.Model):
    __tablename__ = 'Airport'

    id = db.Column(db.Integer, primary_key=True)
    Airport_name = db.Column(db.String(255))
    Overall_rating = db.Column(db.Float)
    Queuing_rating = db.Column(db.Float)
    Terminal_cleanliness_rating = db.Column(db.Float)
    Recommended = db.Column(db.Integer)

    def __repr__(self):
        return "<Airport(Airport_name='%s', Overall_rating='%s', Queueing_rating='%s', " \
               "Terminal_cleanliness_rating='%s', Recommended='%s')" % \
               (self.Airport_name, self.Overall_rating, self.Queueing_rating, self.Terminal_cleanliness_rating,
                self.Recommended)


class Airline(db.Model):
    __tablename__ = 'Airlines'

    id = db.Column(db.Integer, primary_key=True)
    Airline_name = db.Column(db.String(255))
    Overall_rating = db.Column(db.Float)
    Seat_rating = db.Column(db.Float)
    Staff_rating = db.Column(db.Float)
    Food_rating = db.Column(db.Float)
    Entertainment_rating = db.Column(db.Float)
    Value_money_rating = db.Column(db.Float)
    Recommended = db.Column(db.Integer)

    def __repr__(self):
        return "<Airline(Airline_name='%s', Overall_rating='%s', Seat_rating='%s', Staff_rating='%s'," \
               "Food_rating='%s', Entertainment_rating='%s', Value_money_rating='%s', Recommended='%s')"\
               % (self.Airline_name, self.Overall_rating, self.Seat_rating, self.Staff_rating, self.Food_rating,
                  self.Entertainment_rating, self.Value_money_rating, self.Recommended)


class Lounge(db.Model):
    __tablename__ = 'Lounge'

    id = db.Column(db.Integer, primary_key=True)
    Airline_name = db.Column(db.String(255))
    Overall_rating = db.Column(db.Float)
    Comfort_rating = db.Column(db.Float)
    Cleanliness_rating = db.Column(db.Float)
    Washroom_rating = db.Column(db.Float)
    Wifi_connection = db.Column(db.Float)
    Staff_service = db.Column(db.Float)
    Recommended = db.Column(db.Integer)

    def __repr__(self):
        return "<Lounge(Airline_name='%s', Overall_rating='%s', Comfort_rating='%s', Cleanliness_rating='%s'," \
               "Washroom_rating='%s', Wifi_connection='%s', Staff_service='%s', Recommended='%s')" % \
               (self.Airline_name, self.Overall_rating, self.Comfort_rating, self.Cleanliness_rating,
                self.Washroom_rating, self.Wifi_connection, self.Staff_service, self.Recommended)


# [START list]
def list(page, dropdown="", cursor=None):
    if page == "default":
        cursor = int(cursor) if cursor else 0
        query = (Airport.query
                 .order_by(Airport.Overall_rating.desc())
                 .limit(5)
                 .offset(cursor))
        list1 = builtin_list(map(from_sql, query.all()))
        cursor = 0
        query = (Airline.query
                 .order_by(Airline.Overall_rating.desc())
                 .limit(5)
                 .offset(cursor))
        list2 = builtin_list(map(from_sql, query.all()))
        cursor = 0
        query = (Lounge.query
                 .order_by(Lounge.Overall_rating.desc())
                 .limit(5)
                 .offset(cursor))
        list3 = builtin_list(map(from_sql, query.all()))
        return list1, list2, list3

    if page == "airport":
        cursor = int(cursor) if cursor else 0
        query = (Airport.query
                 .order_by(Airport.Overall_rating.desc())
                 .limit(20)
                 .offset(cursor))
        list_item = builtin_list(map(from_sql, query.all()))
        return list_item

    if page == "airport_dropdown":
        cursor = int(cursor) if cursor else 0
        query = (Airport.query
                 .order_by(Airport.__table__.c[dropdown].desc())
                 .limit(20)
                 .offset(cursor))
        list_item = builtin_list(map(from_sql, query.all()))
        return list_item

    if page == "airline":
        cursor = int(cursor) if cursor else 0
        query = (Airline.query
                 .order_by(Airline.Overall_rating.desc())
                 .limit(20)
                 .offset(cursor))
        list_item = builtin_list(map(from_sql, query.all()))
        return list_item

    if page == "airline_dropdown":
        cursor = int(cursor) if cursor else 0
        query = (Airline.query
                 .order_by(Airline.__table__.c[dropdown].desc())
                 .limit(20)
                 .offset(cursor))
        list_item = builtin_list(map(from_sql, query.all()))
        return list_item

    if page == "lounge":
        cursor = int(cursor) if cursor else 0
        query = (Lounge.query
                 .order_by(Lounge.Overall_rating.desc())
                 .limit(20)
                 .offset(cursor))
        list_item = builtin_list(map(from_sql, query.all()))
        return list_item

    if page == "lounge_dropdown":
        cursor = int (cursor) if cursor else 0
        query = (Lounge.query
                 .order_by(Lounge.__table__.c[dropdown].desc())
                 .limit(20)
                 .offset(cursor))
        list_item = builtin_list(map(from_sql, query.all()))
        return list_item
# [END list]


def _create_database():
    """
    If this script is run directly, create all the tables necessary to run the
    application.
    """
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    init_app(app)
    with app.app_context():
        db.create_all()
    print("All tables created")


if __name__ == '__main__':
    _create_database()
