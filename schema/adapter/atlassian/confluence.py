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
@SchemaConfig(
major=1, minor=1,
cacheOption=LayerOpt(expire=86400),
searchOption=LayerOpt(expire=2419200))
class Space(BaseModel, ProfSchema, BaseSchema):
    spaceId:Key = ''
    spaceKey:Key = ''
    homepageId:Key = ''


@SchemaConfig(
major=1, minor=1,
cacheOption=LayerOpt(expire=86400),
searchOption=LayerOpt(expire=2419200))
class Page(BaseModel, ProfSchema, BaseSchema):
    pageId:Key = ''
    body:str = ''

