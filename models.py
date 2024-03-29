from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime
from typing import List

class OrganizationModel(BaseModel):
    Id: str = Field(default_factory=lambda: str(uuid4()))
    OrganizationName: str
    OrganizationEmail: str
    Contact: str
    Website: str
    Address: str
    CreatedBy: str
    CreatedDate: datetime = Field(default_factory=datetime.utcnow)

class UserModel(BaseModel):
    Id: str
    FirstName: str
    LastName: str
    EmpId:str
    Contact: str
    Email: str
    Password: str
    Designation: str
    SpaceName:List[str]
    Status: str
    Access: List[str]
    CreatedDate: datetime = datetime.utcnow()
    CreatedBy: str
    LastUpdatedDate: datetime = datetime.utcnow()
    LastUpdatedBy: str

class UseraccessModel(BaseModel):
    Access: str
    Description: str
    CreatedBy: str
    CreatedDate: datetime = datetime.utcnow()

class SpaceModel(BaseModel):
    Id: str
    SpaceName: str
    CreatedBy: str
    CreatedDate: datetime = datetime.utcnow()
    UpdatedDate: datetime = datetime.utcnow()
    UpdatedBy: str
    SpaceKey: str

class DocumentModel(BaseModel):
    Id: str
    UploadedBy: str
    SpaceID:str
    SpaceName: str
    FileName: str
    FilePath: str
    CreatedDate: datetime = datetime.utcnow()
    UpdatedDate: datetime = datetime.utcnow()
    
class UserModel(BaseModel):
    Id: str
    FirstName: str
    LastName: str
    Contact: str
    Email: str
    Password: str
    Designation: str
    Status: str
    Access: List[str]
    CreatedDate: datetime = datetime.utcnow()
    CreatedBy: str
    LastUpdatedDate: datetime = datetime.utcnow()
    LastUpdatedBy: str

