# -*- coding: utf8 -*-
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类：
Base = declarative_base()

# 定义User对象：
class User(Base):
    # 表的名字：
    __tablename__ = 'user'

    # 表的结构：
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    password = Column(String(20))
    age = Column(Integer)
    address = Column(String(200))

# 初始化数据库连接：
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/sqlalchemystudy')
# 创建DBSession类型：
DBSession = sessionmaker(bind=engine)

# 创建Session:
session = DBSession()

# 创建新的User对象：
new_user = User(id=3, name='wanglan', password='123456', age=30, address='No 63, Block 809, Road, HongXing, Provision Beijing')
#new_user2 = User(name='xuelian', age='27')

# 添加到session：
session.add(new_user)
#session.add(new_user2)

# 提交,即保存到数据库：
session.commit()

# 创建Query查询， filter是where条件，最后调用one()
user = session.query(User).filter(User.id=='2').one()

# 打印类型和对象的name属性：
print 'type:', type(user)
print 'name:', user.name

# 关闭session：
session.close()

