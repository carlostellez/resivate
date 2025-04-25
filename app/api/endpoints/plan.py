"""
Plan API endpoints.

This module provides API endpoints for managing plans.
"""
from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, status

from app.core.deps import DB
from app.models.plan import Plan as PlanModel
from app.schemas.plan import Plan, PlanCreate, PlanUpdate

router = APIRouter()


@router.get("/", response_model=List[Plan])
def read_plans(
    db: DB,
    skip: int = 0,
    limit: int = 100,
) -> List[Dict[str, Any]]:
    """
    Retrieve all plans.
    
    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return
        
    Returns:
        List of plans
    """
    plans = db.query(PlanModel).offset(skip).limit(limit).all()
    return [
        {
            "id": plan.id,
            "title": plan.title,
            "description": plan.description,
            "price": float(plan.price),  # Ensure proper JSON serialization
            "btnMessage": plan.btnMessage,
            "blueBtn": plan.blueBtn
        }
        for plan in plans
    ]


@router.post("/", response_model=Plan, status_code=status.HTTP_201_CREATED)
def create_plan(
    *,
    db: DB,
    plan_in: PlanCreate,
) -> Dict[str, Any]:
    """
    Create a new plan.
    
    Args:
        db: Database session
        plan_in: Plan data to create
        
    Returns:
        Created plan
    """
    plan = PlanModel(
        title=plan_in.title,
        description=plan_in.description,
        price=plan_in.price,
        btnMessage=plan_in.btnMessage,
        blueBtn=plan_in.blueBtn
    )
    db.add(plan)
    db.commit()
    db.refresh(plan)
    
    return {
        "id": plan.id,
        "title": plan.title,
        "description": plan.description,
        "price": float(plan.price),  # Ensure proper JSON serialization
        "btnMessage": plan.btnMessage,
        "blueBtn": plan.blueBtn
    }


@router.get("/{plan_id}", response_model=Plan)
def read_plan(
    *,
    db: DB,
    plan_id: int,
) -> Dict[str, Any]:
    """
    Get a specific plan by ID.
    
    Args:
        db: Database session
        plan_id: ID of the plan to retrieve
        
    Returns:
        Plan with the specified ID
        
    Raises:
        HTTPException: If plan not found
    """
    plan = db.query(PlanModel).filter(PlanModel.id == plan_id).first()
    if not plan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plan not found",
        )
    
    return {
        "id": plan.id,
        "title": plan.title,
        "description": plan.description,
        "price": float(plan.price),  # Ensure proper JSON serialization
        "btnMessage": plan.btnMessage,
        "blueBtn": plan.blueBtn
    }


@router.put("/{plan_id}", response_model=Plan)
def update_plan(
    *,
    db: DB,
    plan_id: int,
    plan_in: PlanUpdate,
) -> Dict[str, Any]:
    """
    Update a plan.
    
    Args:
        db: Database session
        plan_id: ID of the plan to update
        plan_in: New plan data
        
    Returns:
        Updated plan
        
    Raises:
        HTTPException: If plan not found
    """
    plan = db.query(PlanModel).filter(PlanModel.id == plan_id).first()
    if not plan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plan not found",
        )
    
    if plan_in.title is not None:
        plan.title = plan_in.title
    if plan_in.description is not None:
        plan.description = plan_in.description
    if plan_in.price is not None:
        plan.price = plan_in.price
    if plan_in.btnMessage is not None:
        plan.btnMessage = plan_in.btnMessage
    if plan_in.blueBtn is not None:
        plan.blueBtn = plan_in.blueBtn
    
    db.add(plan)
    db.commit()
    db.refresh(plan)
    
    return {
        "id": plan.id,
        "title": plan.title,
        "description": plan.description,
        "price": float(plan.price),  # Ensure proper JSON serialization
        "btnMessage": plan.btnMessage,
        "blueBtn": plan.blueBtn
    }


@router.delete("/{plan_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_plan(
    *,
    db: DB,
    plan_id: int,
) -> None:
    """
    Delete a plan.
    
    Args:
        db: Database session
        plan_id: ID of the plan to delete
        
    Raises:
        HTTPException: If plan not found
    """
    plan = db.query(PlanModel).filter(PlanModel.id == plan_id).first()
    if not plan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plan not found",
        )
    
    db.delete(plan)
    db.commit() 