from typing import Optional, List, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from ..types import Hospital as HospitalType
from ..types.requests import CreateHospitalRequest, UpdateHospitalRequest
from ..db_models import Hospital as HospitalModel
from ..db_models.database import SessionLocal


class Service:

    def __init__(self):
        self.name = "hospital"
        self.description = "Hospital service for managing hospital operations."
    
    def _get_db_session(self) -> Session:
        """Get a database session"""
        return SessionLocal()
    
    def create_hospital(self, hospital_request: CreateHospitalRequest) -> Dict[str, Any]:
        """Create a new hospital"""
        db = self._get_db_session()
        try:
            db_obj = HospitalModel(
                name=hospital_request.name,
                address=hospital_request.address or "",
                phone=hospital_request.phone,
                email=hospital_request.email
            )
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            
            return {
                "status": "success",
                "hospital": db_obj.to_dict()
            }
        except SQLAlchemyError as e:
            db.rollback()
            return {
                "status": "error",
                "message": f"Failed to create hospital: {str(e)}"
            }
        finally:
            db.close()
    
    def get_hospital_by_id(self, hospital_id: int) -> Dict[str, Any]:
        """Get a hospital by ID"""
        db = self._get_db_session()
        try:
            hospital = db.query(HospitalModel).filter(HospitalModel.id == hospital_id).first()
            if not hospital:
                return {
                    "status": "error",
                    "message": "Hospital not found",
                    "hospital": None
                }
            
            return {
                "status": "success",
                "hospital": hospital.to_dict()
            }
        except SQLAlchemyError as e:
            return {
                "status": "error",
                "message": f"Failed to get hospital: {str(e)}",
                "hospital": None
            }
        finally:
            db.close()
    
    def get_all_hospitals(self, skip: int = 0, limit: int = 100) -> Dict[str, Any]:
        """Get all hospitals with pagination"""
        db = self._get_db_session()
        try:
            hospitals = db.query(HospitalModel).offset(skip).limit(limit).all()
            
            return {
                "status": "success",
                "hospitals": [hospital.to_dict() for hospital in hospitals],
                "total": db.query(HospitalModel).count()
            }
        except SQLAlchemyError as e:
            return {
                "status": "error",
                "message": f"Failed to get hospitals: {str(e)}",
                "hospitals": []
            }
        finally:
            db.close()
    
    def update_hospital(self, hospital_id: int, hospital_request: UpdateHospitalRequest) -> Dict[str, Any]:
        """Update a hospital by ID"""
        db = self._get_db_session()
        try:
            hospital = db.query(HospitalModel).filter(HospitalModel.id == hospital_id).first()
            if not hospital:
                return {
                    "status": "error",
                    "message": "Hospital not found",
                    "hospital": None
                }
            
            # Update only provided fields
            if hospital_request.name is not None:
                hospital.name = hospital_request.name
            if hospital_request.address is not None:
                hospital.address = hospital_request.address
            if hospital_request.phone is not None:
                hospital.phone = hospital_request.phone
            if hospital_request.email is not None:
                hospital.email = hospital_request.email
            
            db.commit()
            db.refresh(hospital)
            
            return {
                "status": "success",
                "hospital": hospital.to_dict()
            }
        except SQLAlchemyError as e:
            db.rollback()
            return {
                "status": "error",
                "message": f"Failed to update hospital: {str(e)}",
                "hospital": None
            }
        finally:
            db.close()
    
    def delete_hospital(self, hospital_id: int) -> Dict[str, Any]:
        """Delete a hospital by ID"""
        db = self._get_db_session()
        try:
            hospital = db.query(HospitalModel).filter(HospitalModel.id == hospital_id).first()
            if not hospital:
                return {
                    "status": "error",
                    "message": "Hospital not found"
                }
            
            db.delete(hospital)
            db.commit()
            
            return {
                "status": "success",
                "message": f"Hospital {hospital_id} deleted successfully"
            }
        except SQLAlchemyError as e:
            db.rollback()
            return {
                "status": "error",
                "message": f"Failed to delete hospital: {str(e)}"
            }
        finally:
            db.close()


service = Service()
__all__ = [
    "service",
]