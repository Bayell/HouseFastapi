from fastapi import FastAPI
import uvicorn
from myproject.api import predict_price

house_app = FastAPI(tittle='BayHouse')
house_app.include_router(predict_price.predict_router)

from myproject.api.users import user_router
from myproject.api.region import region_router
from myproject.api.city import city_router
from myproject.api.property import property_router
from myproject.api.review import review_router
from myproject.api.districts import district_router
from myproject.api.auth import auth_router

from myproject.admin.setup import setup_admin


house_app.include_router(user_router, prefix="/users", tags=["users"])
house_app.include_router(region_router, prefix="/region", tags=["regions"])
house_app.include_router(district_router, prefix="/districts", tags=["districts"])
house_app.include_router(property_router, prefix="/property", tags=["property"])
house_app.include_router(city_router, prefix="/city", tags=["city"])
house_app.include_router(review_router, prefix="/review", tags=["review"])
house_app.include_router(auth_router, prefix="/auth", tags=["auth"])

setup_admin(house_app)

if __name__ == "__main__":
    uvicorn.run("main:house_app", reload=True)