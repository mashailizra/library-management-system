from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from models import (
    Library,
    Member,
    DuplicateMemberError,
    MemberNotFoundError,
)


class MemberCreate(BaseModel):
    name: str
    age: int
    member_id: str
    membership_type: str

class MemberUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    membership_type: str | None = None

app = FastAPI()

library = Library.load_from_json("members.json")


@app.exception_handler(DuplicateMemberError)
async def duplicate_member_handler(request: Request, exc: DuplicateMemberError):
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc)},
    )


@app.exception_handler(MemberNotFoundError)
async def member_not_found_handler(request: Request, exc: MemberNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc)},
    )


@app.post("/members")
def create_member(member_data: MemberCreate):
    member = Member(
        member_data.name,
        member_data.age,
        member_data.member_id,
        member_data.membership_type,
    )

    library.add_member(member)
    library.save_to_json("members.json")

    return member.to_dict()

@app.get("/members")
def get_members(sort: str | None = None):
    members = library.members

    if sort == "name":
        members = sorted(members)

    return [member.to_dict() for member in members]

@app.get("/members/{member_id}")
def get_member(member_id: str):
    member = library.find_member(member_id)

    return member.to_dict()

@app.put("/members/{member_id}")
def update_member(member_id: str, member_data: MemberUpdate):
    member = library.find_member(member_id)

    updated_member = Member(
        member_data.name if member_data.name is not None else member.name,
        member_data.age if member_data.age is not None else member.age,
        member_id,
        (
            member_data.membership_type
            if member_data.membership_type is not None
            else member.membership_type
        ),
    )

    updated_member.borrowed_books = member.borrowed_books

    index = library.members.index(member)
    library.members[index] = updated_member

    library.save_to_json("members.json")

    return updated_member.to_dict()

@app.delete("/members/{member_id}")
def delete_member(member_id: str):
    member = library.find_member(member_id)

    library.members.remove(member)
    library.save_to_json("members.json")

    return {
        "message": f"Member {member_id} deleted successfully."
    }