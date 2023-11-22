# Должны
# быть
# реализованы
# методы
# создания / удаления / редактирования
# объявления.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer,String, DateTime, func
from datetime import datetime
# POSTGRES_DSN = f'postgresql://app:secret@127.0.0.1:5431/app'
POSTGRES_DSN =f'postgresql://postgres:Sqlzaebal@127.0.0.1:5432/flaskproject'
engine = create_engine(POSTGRES_DSN)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class Advertisement(Base):
    __tablename__ = 'Adverticement'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] =mapped_column(String(50), unique=True,nullable=False)
    publisher: Mapped[str] =mapped_column(String(120))
    publicationtion_time: Mapped[datetime]=mapped_column(DateTime,server_default=func.now())
    main_text: Mapped[str] =mapped_column(String(2000), unique=True,nullable=False)



'''СОЗДАЮ МИГРАЦИИ'''
Base.metadata.create_all(bind=engine)