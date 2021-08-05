from sqlalchemy.orm import Session

from . import models, schemas


def get_users(db: Session):
    return db.query(models.User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.User):
    db_user = models.User(name=user.name, address=user.address, email=user.email,
                          phone_number=user.phone_number, date_of_birth=user.date_of_birth)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: schemas.User):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db_user.name = user.name
    db_user.address = user.address
    db_user.email = user.email
    db_user.phone_number = user.phone_number
    db_user.date_of_birth = user.date_of_birth
    db.commit()

    return db_user


def delete_user(db: Session, user_id: int):
    try:
        db_user = db.query(models.User).filter(
            models.User.id == user_id).first()
        db.delete(db_user)
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False


def get_nr_clusters(db: Session):
    return db.query(models.Nr_cluster).all()


def get_nr_cluster_by_id(db: Session, nr_id: int):
    return db.query(models.Nr_cluster).filter(models.Nr_cluster.id == nr_id).first()


def create_nr_cluster(db: Session, nr_cluster: schemas.NR_Cluster):
    db_nr = models.Nr_cluster(name=nr_cluster.name, address=nr_cluster.address,
                              city=nr_cluster.city, latitude=nr_cluster.latitude, longitude=nr_cluster.longitude)
    db.add(db_nr)
    db.commit()
    db.refresh(db_nr)
    return db_nr


def update_nr_cluster(db: Session, nr_id: int, nr_cluster: schemas.NR_Cluster):
    db_nr = db.query(models.Nr_cluster).filter(
        models.Nr_cluster.id == nr_id).first()
    db_nr.name = nr_cluster.name
    db_nr.address = nr_cluster.address
    db_nr.city = nr_cluster.city
    db_nr.latitude = nr_cluster.latitude
    db_nr.longitude = nr_cluster.longitude

    db.commit()
    return db_nr


def delete_nr_cluster(db: Session, nr_id: int):
    try:
        db_nr = db.query(models.Nr_cluster).filter(
            models.Nr_cluster.id == nr_id).first()
        db.delete(db_nr)
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False


def get_users_nrcluster(db: Session):
    return db.query(models.User_NRCluster).all()


def get_user_nrcluster_by_id(db: Session, id: int):
    return db.query(models.User_NRCluster).filter(models.User_NRCluster.id == id).first()


def create_user_nrcluster(db: Session, data: schemas.User_NRCluster):
    try:
        db_unr = models.User_NRCluster(
            user_id=data.user_id, nr_cluster_id=data.nr_cluster_id, role=data.role)
        db.add(db_unr)
        db.commit()
        db.refresh(db_unr)
        return db_unr
    except Exception as e:
        print(e)
        return False


def update_users_nrcluster(db: Session, id: int, data: schemas.User_NRCluster):
    try:

        db_unr = db.query(models.User_NRCluster).filter(
            models.User_NRCluster.id == id).first()
        db_unr.user_id = data.user_id
        db_unr.nr_cluster_id = data.nr_cluster_id
        db_unr.role = data.role
        db.commit()
        return db_unr
    except Exception as e:
        print(e)
        return None


def delete_users_nrcluster(db: Session, id: int):
    try:
        db_unr = db.query(models.User_NRCluster).filter(
            models.User_NRCluster.id == id).first()
        db.delete(db_unr)
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False
