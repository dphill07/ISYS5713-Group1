from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from database_models.base_model import Base

class TicketLine(Base):
    __tablename__ = 'fact_ticket_lines'
    
    ticket_line_id = Column(Integer, primary_key=True, autoincrement=True)
    ticket_id = Column(Integer, ForeignKey('fact_tickets.ticket_id'))
    technician_id = Column(Integer, ForeignKey('dim_technicians.technician_id'))
    assignment_date_time = Column(DateTime, nullable=False)
    completion_date_time = Column(DateTime)
    notes = Column(String)
    
    # Relationships
    technician = relationship('Technician', back_populates='ticket_lines')
    ticket = relationship('Ticket', back_populates='ticket_lines')

    Session = sessionmaker(bind=Base.engine)
    
