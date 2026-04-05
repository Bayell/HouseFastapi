import streamlit as st
import requests

nei_list = ['_Blueste', '_BrDale', '_BrkSide', '_ClearCr', '_CollgCr',
            '_Crawfor', '_Edwards', '_Gilbert', '_IDOTRR', '_MeadowV',
            '_Mitchel', '_NAmes', '_NPkVill', '_NWAmes', '_NoRidge',
            '_NridgHt', '_OldTown', '_SWISU', '_Sawyer', '_SawyerW',
            '_Somerst', '_StoneBr', '_Timber', '_Veenker']


api_url = 'http://127.0.0.1:8000/predict/'
st.title('Прогноз Цены')

area = st.number_input('Площадь:', value=0)
year= st.number_input('Год:', value=0)
garage= st.number_input('Вместимость:', value=0)
bsmt = st.number_input('Площадь Дома:', value=0)
bath =st.number_input('Кол.ванн:', value=0)
overall_qual = st.number_input('Качество:', value=0)
neighborhood = st.selectbox('район', nei_list)

data = {
    "GrLivArea": area,
    "YearBuilt": year,
    "GarageCars": garage,
    "TotalBsmtSF": bsmt,
    "FullBath": bath,
    "OverallQual": overall_qual,
    "Neighborhood": neighborhood
}


if st.button('Проверка'):

    try:
        answer = requests.post(api_url, json=data,timeout=10)
        if answer.status_code == 200:
            result = answer.json()
            st.success(f'Результат: {result.get('price')}')

        else:
            st.error(f'Error: {answer.status_code}')
    except requests.exceptions.RequestException:
        st.error(f'Не удалось подключиться к API')