# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from typing import List
from pydantic import BaseModel
from common import SchemaConfig, LayerOpt, Reference, ID, Key, BaseSchema, ProfSchema, TagSchema, MetaSchema


#===============================================================================
# Implement
#===============================================================================
@SchemaConfig(3,
cacheOption=LayerOpt(expire=86400),
searchOption=LayerOpt(expire=2419200))
class Ticket(BaseModel, BaseSchema):
    ticketId:int = 0
    title:str = ''
    username:str = ''
    email:str = ''
    source:str = ''
    created:str = ''
    priority:str = ''
    status:str = ''