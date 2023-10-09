from wateraware import db

class Enda(db.Model):
    __tablename__ = "endangered"
    id:int = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    c_name:str= db.Column(db.String(100), unique=False, nullable=True)
    sci_name:str= db.Column(db.String(100), unique=False, nullable=True)
    sci_name_url:str= db.Column(db.String(100), unique=False, nullable=True)
    status:str= db.Column(db.String(100), unique=False, nullable=True)
    description:str= db.Column(db.String(100), unique=False, nullable=True)
    list_date:str= db.Column(db.String(100), unique=False, nullable=True)
    species_id:int= db.Column(db.Integer, unique=False, nullable=False)
    poly_env:str= db.Column(db.String(100), unique=False, nullable=True)
    poly_shape: str= db.Column(db.String(100), unique=False, nullable=True)
    poly_url: str= db.Column(db.String(100), unique=False, nullable=True)
    img_url: str= db.Column(db.String(100), unique=False, nullable=True)
    img_url_2: str= db.Column(db.String(100), unique=False, nullable=True)
    img_source: str= db.Column(db.String(100), unique=False, nullable=True)
    county: str= db.Column(db.String(100), unique=False, nullable=True)
    state_abb: str= db.Column(db.String(100), unique=False, nullable=True)
    state: str= db.Column(db.String(100), unique=False, nullable=True)
    foreign: bool= db.Column(db.Boolean, unique=False, nullable=True)

    def __repr__(self):
        return f"<{self.c_name}>, <{self.sci_name}>, <{self.status}>, <{self.description}>, \
            <{self.list_date}>, <{self.species_id}>, \
            <{self.poly_env}>, <{self.poly_shape}>, <{self.poly_url}>, <{self.img_url}>, \
            <{self.img_url_2}>, <{self.img_source}>, <{self.county}>, <{self.state_abb}>, \
            <{self.state}>, <{self.foreign}>"