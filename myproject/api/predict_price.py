import joblib
from fastapi import APIRouter
from myproject.database.schema import HouseSchema

nei_list = ['_Blueste', '_BrDale', '_BrkSide', '_ClearCr', '_CollgCr',
            '_Crawfor', '_Edwards', '_Gilbert', '_IDOTRR', '_MeadowV',
            '_Mitchel', '_NAmes', '_NPkVill', '_NWAmes', '_NoRidge',
            '_NridgHt', '_OldTown', '_SWISU', '_Sawyer', '_SawyerW',
            '_Somerst', '_StoneBr', '_Timber', '_Veenker']

model = joblib.load('myproject/ml_models/model (1).pkl')
scaler = joblib.load('myproject/ml_models/scaler (1).pkl')

predict_router = APIRouter(prefix ='/predict', tags = ['House_Price'])

@predict_router.post('/')
async def predict_price(house: HouseSchema):
    house_dict = house.dict()

    name_nei = house_dict.pop('Neighborhood')
    name_nei1_0 =[
        1 if name_nei == i else 0 for i in nei_list
    ]

    house_data = list(house_dict.values()) + name_nei1_0
    scaled_data = scaler.transform([house_data])
    pred = model.predict(scaled_data)[0]
    return{'price':round(pred)}