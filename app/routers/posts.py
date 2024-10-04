from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..database import Base, engine,  get_db
from sqlalchemy.orm import Session
from .. import models, schemas,oauth2
from typing import List,Optional



router = APIRouter(prefix="/posts",tags=["Posts"])

@router.get("/", response_model=List[schemas.BasePost])
def get_posts(db: Session = Depends(get_db),
              limit: int=10, skip:int=0,search:Optional[str]=""):
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit=limit).offset(offset=skip)
    return posts  # No need for {"data": posts}, return the posts directly



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.BasePost)
def create_post(post: schemas.CreatePost, db: Session = Depends(get_db), 
                get_current_user: int=Depends(oauth2.get_current_user)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post



@router.get("/{id}", response_model=schemas.BasePost)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} not found")
    return post



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # Corrected: Call the first() method with parentheses
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} not found")
    
    db.delete(post)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.BasePost)
def update_post(id: int, updated_post: schemas.UpdatePost, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} not found")

    # Update fields conditionally
    if updated_post.title is not None:
        post.title = updated_post.title
    if updated_post.content is not None:
        post.content = updated_post.content
    if updated_post.publish is not None:
        post.publish = updated_post.publish
    if updated_post.rating is not None:
        post.rating = updated_post.rating

    db.commit()
    db.refresh(post)
    return post
