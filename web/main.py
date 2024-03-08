from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from enum import Enum

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class Categories(Enum):
    PRESCHOOL = "Дошкольники (5-6 лет)"
    JUNIOR = "Младшая категория (7-9 лет)"
    MIDDLE = "Средняя категория (10-13 лет)"
    SENIOR = "Старшая категория (14-17 лет)"
    TEACHER = "Регистрация наставников"
    OVZ = "Категория для детей с ОВЗ"

    @classmethod
    def to_dict(cls):
        return {item.name: item.value for item in Categories}

COUNTIRES = {
    "ru": "Россия",
    "by": "Беларусь",
    "kz": "Казахстан",
    "uz": "Узбекистан",
    "oth": "Иное",
}


CATEGORIES_COUNTRY = {
    "ru": [
        {Categories.PRESCHOOL.name: Categories.PRESCHOOL.value}, 
        {Categories.JUNIOR.name: Categories.JUNIOR.value}, 
        {Categories.MIDDLE.name: Categories.MIDDLE.value}, 
        {Categories.SENIOR.name: Categories.SENIOR.value}, 
        {Categories.TEACHER.name :Categories.TEACHER.value}, 
        {Categories.OVZ.name: Categories.OVZ.value}
        ],
    "kz": [
        {Categories.JUNIOR.name: Categories.JUNIOR.value}, 
        {Categories.MIDDLE.name: Categories.MIDDLE.value}, 
        {Categories.SENIOR.name: Categories.SENIOR.value}
        ],
    "uz": [
        {Categories.JUNIOR.name: Categories.JUNIOR.value}, 
        {Categories.MIDDLE.name: Categories.MIDDLE.value}, 
        {Categories.SENIOR.name: Categories.SENIOR.value}
        ],
}

@app.get("/auth", response_class=HTMLResponse)
async def form_authentication(request: Request):
    """Страница с формой"""
    context = {
        "countries": COUNTIRES,
        "categories": Categories.to_dict()
    }
    return templates.TemplateResponse(request=request, name="auth.html", context=context)


@app.get("/auth/categories")
async def get_categories(category: str):
    return {"cateogries": CATEGORIES_COUNTRY[category]}


@app.post("/auth")
async def authentication(request: Request):
    """Обработка полученных данных"""
    print(request.__dict__)
    return RedirectResponse("/auth", status_code=302)


