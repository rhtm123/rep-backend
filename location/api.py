from ninja import  Router, Query

# router.py
from .models import City, State
from .schemas import CityCreateSchema, CityOutSchema, CityUpdateSchema
from django.shortcuts import get_object_or_404

from utils.pagination import PaginatedResponseSchema, paginate_queryset

router = Router()

# Create City
@router.post("/cities/", response=CityOutSchema)
def create_city(request, payload: CityCreateSchema):
    state = get_object_or_404(State, id=payload.state_id)
    city = City(name=payload.name, state=state)
    city.save()
    return city

# Read Cities (List)
@router.get("/cities/", response=PaginatedResponseSchema)
def cities(request, state_id: int = None, ordering: str = None , page: int = Query(1), page_size: int = Query(10)):
    qs = City.objects.all()


    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)

    if state_id:
        qs = qs.filter(state=state_id)
    
    if ordering:
        qs = qs.order_by(ordering)

    return paginate_queryset(request, qs, CityOutSchema, page_number, page_size)

# Read Single city (Retrieve)
@router.get("/cities/{city_id}/", response=CityOutSchema)
def retrieve_city(request, city_id: int):
    city = get_object_or_404(City, id=city_id)
    return city

# Update city
@router.put("/cities/{city_id}/", response=CityOutSchema)
def update_city(request, city_id: int, payload: CityUpdateSchema):
    city = get_object_or_404(City, id=city_id)
    for attr, value in payload.dict().items():
        if value is not None:
            setattr(city, attr, value)
    city.save()
    return city

# Delete city
@router.delete("/cities/{city_id}/")
def delete_city(request, city_id: int):
    city = get_object_or_404(City, id=city_id)
    city.delete()
    return {"success": True}
