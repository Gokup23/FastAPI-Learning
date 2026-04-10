from sqlalchemy import Column , Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Meal(Base):
    __tablename__ = 'Meals'
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    allowed_macro = Column(String)

class FoodItem(Base):
    __tablename__ = "food_items"
    id = Column(Integer,primary_key = True, index =True)
    name = Column(String)
    is_soy_free = Column(Boolean,default = True)
    is_seed_free = Column(Boolean,default = True)

    meal_id = Column(Integer,ForeignKey("meals.id"))

#Relationship is for python and Foreign key is for database  

# Back up in your Meal class...
    foods = relationship("FoodItem", back_populates="meal")

# Down in your FoodItem class...
    meal = relationship("Meal", back_populates="foods")