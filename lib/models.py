from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

# company-freebie (many-many) relationship
company_dev = Table(
    'company_devs',
    Base.metadata,
    Column('company_id', ForeignKey('companies.id'), primary_key=True),
    Column('dev_id', ForeignKey('devs.id'), primary_key=True),
    extend_existing=True,
)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    # establishing company-freebie (one-to-many) relationship
    freebies = relationship('Freebie', backref=backref('companies'))
    devs = relationship('Dev', secondary=company_dev, back_populates='companies')

    def __repr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    # establishing dev-freebie (one-to-many) relationship
    freebies = relationship('Freebie', backref=backref('devs'))
    companies = relationship('Company', secondary=company_dev, back_populates='devs')

    def __repr__(self):
        return f'<Dev {self.name}>'
    
class Freebie(Base):
    __tablename__= 'freebies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    value = Column(Integer())
    # creating foreign foreign keys for relationships (company-freebie)
    company_id = Column(Integer(), ForeignKey('companies.id'))
    #creating foreign foreign keys for relationships (dev-freebie)
    dev_id = Column(Integer(), ForeignKey('devs.id'))
    

    def __repr__(self) -> str:
        return f'Freebie(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'value={self.value})'

