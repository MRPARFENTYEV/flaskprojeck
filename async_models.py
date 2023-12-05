import datetime
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, func

POSTGRES_DSN =f'postgresql+asyncpg://postgres:Sqlzaebal@127.0.0.1:5432/flask_async'
engine = create_async_engine(POSTGRES_DSN)
Session = async_sessionmaker(engine,expire_on_commit=False)

class Base(AsyncAttrs,DeclarativeBase):
    pass

class Advertisement(Base):
    __tablename__ = 'advertisement'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] =mapped_column(String(50), unique=True,index=True,nullable=False)
    publisher: Mapped[str] =mapped_column(String(120))
    publicationtion_time: Mapped[datetime.datetime]=mapped_column(DateTime,server_default=func.now())
    main_text: Mapped[str] =mapped_column(String(2000), unique=True,nullable=False)
    @property
    def dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'publisher': self.publisher,
            'publication time': self.publicationtion_time.isoformat(),
            'main text': self.main_text
        }