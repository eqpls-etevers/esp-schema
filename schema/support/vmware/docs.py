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
class KnowledgebaseContent(BaseModel):
    title:Key = ''
    text:str = ''


@SchemaConfig( 1 ,
cacheOption=LayerOpt(expire=86400),
searchOption=LayerOpt(expire=2419200))
class Knowledgebase(BaseModel, BaseSchema):
    title:str = ''
    docId:Key = ''
    docType:Key = ''
    updateDate:Key = ''
    products:List[str] = []
    contents:List[KnowledgebaseContent] = []
