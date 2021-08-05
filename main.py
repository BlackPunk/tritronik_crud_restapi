from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return RedirectResponse("/docs")


@app.get("/users", response_model=List[schemas.User], tags=["User"])
def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.get("/users/{user_id}", response_model=schemas.User, tags=["User"])
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return user


@app.post("/users", response_model=schemas.User, tags=["User"])
def create_users(user: schemas.Create_user, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@app.put("/users/{user_id}", response_model=schemas.User, tags=["User"])
def update_user(user_id: int, user: schemas.Create_user, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if db_user:
        update_user = crud.update_user(db, user_id, user)
    else:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    return update_user


@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK, tags=["User"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if db_user:
        crud.delete_user(db, user_id)
        return {"detail": "Berhasil hapus data"}
    else:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")


@app.get("/cluster", response_model=List[schemas.NR_Cluster], tags=["NR Cluster"])
def get_nr_cluster(db: Session = Depends(get_db)):
    return crud.get_nr_clusters(db)


@app.get("/cluster/{nr_id}", response_model=schemas.NR_Cluster, tags=["NR Cluster"])
def get_nr_cluster_by_id(nr_id: int, db: Session = Depends(get_db)):
    db_nr = crud.get_nr_cluster_by_id(db, nr_id)
    if db_nr:
        return db_nr
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Cluster tidak ditemukan")


@app.post("/cluster", response_model=schemas.NR_Cluster, tags=["NR Cluster"])
def create_nr_cluster(nr_cluster: schemas.Create_nr_cluster, db: Session = Depends(get_db)):
    return crud.create_nr_cluster(db, nr_cluster)


@app.put("/cluster/{nr_id}", response_model=schemas.NR_Cluster, tags=["NR Cluster"])
def update_nr_cluster(nr_id: int, nr_cluster: schemas.Create_nr_cluster, db: Session = Depends(get_db)):
    db_nr = crud.get_nr_cluster_by_id(db, nr_id)

    if db_nr:
        update_cluster = crud.update_nr_cluster(db, nr_id, nr_cluster)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Cluster tidak dapat ditemukan")

    return update_cluster


@app.delete("/cluster/{nr_id}", status_code=status.HTTP_200_OK, tags=["NR Cluster"])
def delete_cluster(nr_id: int, db: Session = Depends(get_db)):
    db_nr = crud.get_nr_cluster_by_id(db, nr_id)
    if db_nr:
        crud.delete_nr_cluster(db, nr_id)
        return {"detail": "Berhasil hapus data"}
    else:
        raise HTTPException(status_code=404, detail="Cluster tidak ditemukan")


@app.get("/user/nrcluster", response_model=List[schemas.User_NRCluster], tags=["User NRCluster"])
def get_users_nrcluster(db: Session = Depends(get_db)):
    return crud.get_users_nrcluster(db)


@app.get("/user/nrcluster/{id}", response_model=schemas.User_NRCluster, tags=["User NRCluster"])
def get_user_nrcluster_by_id(id: int, db: Session = Depends(get_db)):
    db_unr = crud.get_user_nrcluster_by_id(db, id)
    if db_unr:
        return db_unr
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User NR Cluster tidak dapat ditemukan")


@app.post("/user/nrcluster", response_model=schemas.User_NRCluster, tags=["User NRCluster"])
def create_user_nrcluster(data: schemas.Create_user_nrcluster, db: Session = Depends(get_db)):
    db_unr = crud.create_user_nrcluster(db, data)
    if db_unr:
        return db_unr
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Terjadi kesalahan")


@app.put("/user/nrcluster/{id}", response_model=schemas.User_NRCluster, tags=["User NRCluster"])
def update_user_nrcluster(id: int, data: schemas.Create_user_nrcluster, db: Session = Depends(get_db)):
    db_unr = crud.get_user_nrcluster_by_id(db, id)
    if db_unr:
        update_data = crud.update_users_nrcluster(db, id, data)
        if update_data is None:
            raise HTTPException(status_code=500, detail="Terjadi kesalahan")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User NR Cluster tidak dapat ditemukan")

    return update_data


@app.delete("/user/nrcluster/{id}", status_code=status.HTTP_200_OK, tags=["User NRCluster"])
def delete_user_nrcluster(id: int, db: Session = Depends(get_db)):
    db_unr = crud.get_user_nrcluster_by_id(db, id)

    if db_unr:
        crud.delete_users_nrcluster(db, id)
        return {"detail": "Berhasil hapus data"}
    else:
        raise HTTPException(
            status_code=404, detail="User NR Cluster tidak dapat ditemukan")
