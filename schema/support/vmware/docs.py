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
from common import ID, Key, BaseSchema, ProfSchema, TagSchema, MetaSchema


#===============================================================================
# Implement
#===============================================================================
class KnowledgebaseContent(BaseModel):
    title:Key = ''
    text:str = ''


class Knowledgebase(BaseModel, BaseSchema):
    title:str = ''
    docId:Key = ''
    docType:Key = ''
    updateDate:Key = ''
    products:List[str] = ''
    contents:List[KnowledgebaseContent] = []
