from Demo import db


class Tab01(db.Model):
    __tablename__ = 'test01'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True)
    diseasename = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<Tab01 %d %s %s %s>' % (self.id, self.code, self.diseasename, self.description)


class Tab02(db.Model):
    __tablename__ = 'test02'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True)
    diseasename = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<Tab02 %d %s %s %s>' % (self.id, self.code, self.diseasename, self.description)
