from fastapi import APIRouter, HTTPException, Query
from typing import Dict, Any, List

from ...types import Hospital
from ...types.requests import CreateHospitalRequest, UpdateHospitalRequest
from ...services.hospital import service

router = APIRouter()


@router.post("")
async def create_hospital(
    hospital: CreateHospitalRequest,
) -> Dict[str, Any]:
    """Create a new hospital"""
    result = service.create_hospital(hospital)
    
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    
    return result


@router.get("/{hospital_id}")
async def get_hospital_by_id(
    hospital_id: int,
) -> Dict[str, Any]:
    """Get a hospital by ID"""
    result = service.get_hospital_by_id(hospital_id)
    
    if result["status"] == "error":
        raise HTTPException(status_code=404, detail=result["message"])
    
    return result


@router.get("")
async def get_all_hospitals(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return")
) -> Dict[str, Any]:
    """Get all hospitals with pagination"""
    result = service.get_all_hospitals(skip=skip, limit=limit)
    
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["message"])
    
    return result


@router.put("/{hospital_id}")
async def update_hospital(
    hospital_id: int,
    hospital: UpdateHospitalRequest,
) -> Dict[str, Any]:
    """Update a hospital by ID"""
    result = service.update_hospital(hospital_id, hospital)
    
    if result["status"] == "error":
        if "not found" in result["message"].lower():
            raise HTTPException(status_code=404, detail=result["message"])
        else:
            raise HTTPException(status_code=400, detail=result["message"])
    
    return result


@router.delete("/{hospital_id}")
async def delete_hospital(
    hospital_id: int,
) -> Dict[str, Any]:
    """Delete a hospital by ID"""
    result = service.delete_hospital(hospital_id)
    
    if result["status"] == "error":
        if "not found" in result["message"].lower():
            raise HTTPException(status_code=404, detail=result["message"])
        else:
            raise HTTPException(status_code=500, detail=result["message"])
    
    return result


__all__ = ["router"]
