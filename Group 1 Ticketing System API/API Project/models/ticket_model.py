from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from models.base_model import Base
from datetime import datetime
from dateutil.parser import parse

class Ticket(Base):
    __tablename__ = 'fact_tickets'
    
    ticket_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('dim_users.user_id'))
    department_id = Column(Integer, ForeignKey('dim_departments.department_id'))
    prior_ticket_id = Column(Integer)
    ticket_category = Column(String, nullable=False)
    open_date_time = Column(DateTime, nullable=False)
    close_date_time = Column(DateTime)
    status = Column(String)
    description = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    
    # Relationships
    user = relationship('User', back_populates='tickets')
    ticket_lines = relationship('TicketLine', back_populates='ticket')

    Session = sessionmaker(bind=Base.engine)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    #show ticket record based on the ticket_id
    @classmethod
    def read_ticketid(cls, ticket_id):
        with cls.Session() as session:
            ticket = session.query(cls).filter(cls.ticket_id == ticket_id).first()
            if ticket is None:
                return {'Error': 'Ticket not found', 'status': 404}
            return ticket.as_dict()

    #show all ticket records
    @classmethod
    def read_all_tickets(cls):
        with cls.Session() as session:
            query = session.query(cls)
            tickets = []
            for row in query.all():
                ticket = {
                    'Ticket ID' : row.ticket_id, 
                    'User ID' : row.user_id, 
                    'Department ID' : row.department_id, 
                    'Prior Ticket ID' : row.prior_ticket_id, 
                    'Ticket Category' : row.ticket_category, 
                    'Open Date Time' : row.open_date_time, 
                    'Close Date Time' : row.close_date_time, 
                    'Status': row.status, 
                    'Description' : row.description, 
                    'Subject' : row.subject}
                tickets.append(ticket)
        return tickets

    #show (param) of records in the Ticket tables
    @classmethod
    def read_tickets(cls, start, limit):
        with cls.Session() as session:
            query = session.query(cls)
            if start is not None:
                query = query.offset(start)
            if limit is not None:
                query = query.limit(limit)
            tickets = []
            for row in query.all():
                ticket = {
                    'Ticket ID' : row.ticket_id, 
                    'User ID' : row.user_id, 
                    'Department ID' : row.department_id, 
                    'Prior Ticket ID' : row.prior_ticket_id, 
                    'Ticket Category' : row.ticket_category, 
                    'Open Date Time' : row.open_date_time, 
                    'Close Date Time' : row.close_date_time, 
                    'Status': row.status, 
                    'Description' : row.description, 
                    'Subject' : row.subject}
                tickets.append(ticket)
        return tickets
    
    #Adds a new ticket
    @classmethod
    def create_ticket(cls, ticket_data):
        with cls.Session() as session:
            # open_date_time1 = datetime.strptime(ticket_data['open_date_time'], '%a, %d %b %Y %H:%M:%S %Z')
            # close_date_time1 = datetime.strptime(ticket_data['close_date_time'], '%a, %d %b %Y %H:%M:%S %Z')
            open_date_time1 = parse(ticket_data['open_date_time'])
            
            new_ticket = cls(user_id=ticket_data['user_id']
                             , department_id=ticket_data['department_id']
                             , prior_ticket_id=ticket_data['prior_ticket_id']
                             , ticket_category=ticket_data['ticket_category']
                             , open_date_time=open_date_time1
                             , status=ticket_data['status']
                             , description=ticket_data['description']
                             , subject=ticket_data['subject'])
            session.add(new_ticket)
            session.commit()
            session.refresh(new_ticket)

            return new_ticket.as_dict()
        

    #Updates a ticket
    @classmethod
    def update_ticket(cls, ticket_id, ticket_data):
        with cls.Session() as session:
            ticket = session.query(cls).filter(cls.ticket_id == ticket_id).first()
            # open_date_time1 = datetime.strptime(ticket_data['open_date_time'], '%a, %d %b %Y %H:%M:%S %Z')
            # close_date_time1 = datetime.strptime(ticket_data['close_date_time'], '%a, %d %b %Y %H:%M:%S %Z')
            
            ticket.user_id = ticket_data['user_id']
            ticket.department_id = ticket_data['department_id']
            ticket.prior_ticket_id = ticket_data['prior_ticket_id']
            ticket.ticket_category = ticket_data['ticket_category']
            ticket.description = ticket_data['description']
            ticket.subject = ticket_data['subject']
            session.commit()
            session.refresh(ticket)
            return ticket.as_dict()
    
    @classmethod
    def delete_ticket(cls, ticket_id):
        with cls.Session() as session:
            ticket = session.query(cls).filter(cls.ticket_id == ticket_id).first()
            if ticket is None:
                return {'Error': 'Ticket not found', 'status': 404}
            session.delete(ticket)
            session.commit()
        return True

        