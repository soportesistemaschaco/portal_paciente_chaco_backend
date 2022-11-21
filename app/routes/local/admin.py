from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from app.gear.local.admin import (
    remove_a_person,
    not_accept_a_person,
    accept_a_person,
    list_of_persons_to_accept,
    list_of_persons_accepted,
    list_of_persons_in_general
)
from app.main import get_db
from app.routes.common import router_admin
from app.schemas.persons import PersonUsername, PersonsReduced
from app.schemas.returned_object import ReturnMessage
from app.schemas.responses import ResponseOK, ResponseNOK
from app.schemas.person_user import (
    PersonUser as schema_person_user,
    CreatePersonUser as schema_create_person_user,
)
from app.gear.local.local_impl import LocalImpl

@router_admin.post(
    "/createpersonuser",
    name="Crear Usuario Administrador",
    response_model=ResponseOK,
    responses={417: {"model": ResponseNOK}},
    tags=["User and person"],
)
async def create_person(personUser: schema_create_person_user, db: Session = Depends(get_db)):
    return LocalImpl(db).create_person(personUser)

@router_admin.get(
    "/getpersonuserbyid",
    response_model=schema_person_user,
    responses={417: {"model": ResponseNOK}},
    tags=["User and person"],
)
async def get_person_by_id(person_id: int, db: Session = Depends(get_db)):
    return LocalImpl(db).get_person_by_id(person_id)

@router_admin.put(
    "/updatepersonuser",
    response_model=ResponseOK,
    responses={417: {"model": ResponseNOK}},
    tags=["User and person"],
)
async def update_person(person: schema_person_user, db: Session = Depends(get_db)):
    return LocalImpl(db).update_person(person)


@router_admin.put(
    "/deletepersonuser",
    response_model=ResponseOK,
    responses={417: {"model": ResponseNOK}},
    tags=["User and person"],
)
async def delete_person(person_id: int, db: Session = Depends(get_db)):
    return LocalImpl(db).delete_person(person_id)



@router_admin.delete("/person", name="Remove a Person",
                     response_model=ReturnMessage, description="Remove a Person from the system")
async def delete_person(person_username: PersonUsername, db: Session = Depends(get_db)):
    return remove_a_person(person_username, db)


@router_admin.put("/notaccept", name="Deny access to a Person",
                  response_model=ReturnMessage, description="Denied access to a person")
async def not_accept_person(person_username: PersonUsername, db: Session = Depends(get_db)):
    return not_accept_a_person(person_username, db)


@router_admin.put("/id_admin_status", name="Accept a Person",
                  response_model=ReturnMessage, description="Accept a Person in the system")
async def accept_person(person_username: PersonUsername, db: Session = Depends(get_db)):
    return accept_a_person(person_username, db)


@router_admin.get("/persons_accepted", name="List of id_admin_status Person", response_model=List[PersonsReduced], description="List of Persons id_admin_status in the system")
async def persons_accepted(db: Session = Depends(get_db)):
    return list_of_persons_accepted(db)


@router_admin.get("/persons_to_be_accepted", name="List of id_admin_status Person", response_model=List[PersonsReduced], description="List of Persons to be id_admin_status in the system")
async def persons_accepted(db: Session = Depends(get_db)):
    return list_of_persons_to_accept(db)


@router_admin.get("/persons", name= "List of persons", response_model=List[PersonsReduced], description="List of all Persons in the system")
async def persons(db: Session = Depends(get_db)):
    return list_of_persons_in_general(db)

