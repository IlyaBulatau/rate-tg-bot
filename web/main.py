from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
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


COMPETITIONS = {
        "ru": {
            Categories.PRESCHOOL.name: {
                "team": {
                    "tvorcheskaka": "Творческая категория", 
                    "moveLine": "Движение по линии", 
                    "sumo": "Сумо", 
                    "futureInjener": "Миссия 'Будущий инженер'", 
                    "scratch": "Scratch junior"
                    }
                ,
                "individual": {
                    "tvorcheskaka": "Творческая категория", 
                    "moveLine": "Движение по линии", 
                    "sumo": "Сумо", 
                    "futureInjener": "Миссия 'Будущий инженер'", 
                    "scratch": "Scratch junior"
                    }
            },
            Categories.JUNIOR.name: {
                "team": {
                    "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "waterRobot": "Подводные роботы",
                    "modelDDD": "3Д моделирование",
                    "footboll": "Футбол",
                },
                "individual": {
                    "startRobo": "Олимпиада «Старт в робототехнику»",
                    "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "waterRobot": "Подводные роботы",
                    "modelDDD": "3Д моделирование",
                    "scratch": "Scratch",
                }
            },
            Categories.MIDDLE.name: {
                "team": {
                    "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "waterRobot": "Подводные роботы",
                    "modelDDD": "3Д моделирование",
                    "footboll": "Футбол",
                    "virulreal": "Виртуальная реальность",
                    "bpla": "БПЛА",
                    "internetCl": "Интернет вещей",
                    "chpu": "Станки ЧПУ",
                    "neirotech": "Нейротехнологии",
                    "gameDev": "Разработка игр"
                },
                "individual": {
                    "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "waterRobot": "Подводные роботы",
                    "modelDDD": "3Д моделирование",
                    "footboll": "Футбол",
                    "virulreal": "Виртуальная реальность",
                    "bpla": "БПЛА",
                    "chpu": "Станки ЧПУ",
                    "neirotech": "Нейротехнологии",
                    "python": "Python",
                    "gameDev": "Разработка игр"
                }
            },
            Categories.SENIOR.name: {
                "team": {
                    "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "waterRobot": "Подводные роботы",
                    "modelDDD": "3Д моделирование",
                    "footboll": "Футбол",
                    "virulreal": "Виртуальная реальность",
                    "bpla": "БПЛА",
                    "internetCl": "Интернет вещей",
                    "chpu": "Станки ЧПУ",
                    "neirotech": "Нейротехнологии",
                    "gameDev": "Разработка игр"
                },
                "individual": {
                    "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "waterRobot": "Подводные роботы",
                    "modelDDD": "3Д моделирование",
                    "footboll": "Футбол",
                    "virulreal": "Виртуальная реальность",
                    "bpla": "БПЛА",
                    "chpu": "Станки ЧПУ",
                    "neirotech": "Нейротехнологии",
                    "python": "Python",
                    "gameDev": "Разработка игр"
                }
            },
            Categories.TEACHER.name: {},
            Categories.OVZ.name: {},
        },
        "kz": {
            Categories.JUNIOR.name: {
                "team": {
                   "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "waterRobot": "Подводные роботы",
                    "modelDDD": "3Д моделирование",
                    "footboll": "Футбол",  
                },
                "individual": {
                    "startRobo": "Олимпиада «Старт в робототехнику»",
                    "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "waterRobot": "Подводные роботы",
                    "modelDDD": "3Д моделирование",
                    "scratch": "Scratch",
                }
            },
            Categories.MIDDLE.name: {
                "team": {
                    "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "modelDDD": "3Д моделирование",
                    "footboll": "Футбол",
                },
                "individual": {
                    "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "python": "Python",
                    "scratch": "Scratch",
                }
            },
            Categories.SENIOR.name: {
                "team": {
                    "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "modelDDD": "3Д моделирование",
                    "footboll": "Футбол",
                },
                "individual": {
                    "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "python": "Python",
                    "scratch": "Scratch",
                }
            },
        },
        "uz": {
            Categories.JUNIOR.name: {
                "team": {
                   "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "waterRobot": "Подводные роботы",
                    "modelDDD": "3Д моделирование",
                    "footboll": "Футбол",  
                },
                "individual": {
                    "startRobo": "Олимпиада «Старт в робототехнику»",
                    "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "waterRobot": "Подводные роботы",
                    "modelDDD": "3Д моделирование",
                    "scratch": "Scratch",
                }
            },
            Categories.MIDDLE.name: {
                "team": {
                    "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "modelDDD": "3Д моделирование",
                    "footboll": "Футбол",
                },
                "individual": {
                    "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "python": "Python",
                    "scratch": "Scratch",
                }
            },
            Categories.SENIOR.name: {
                "team": {
                    "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "modelDDD": "3Д моделирование",
                    "footboll": "Футбол",
                },
                "individual": {
                    "moveLineDIY": "Движение по линии DIY",
                    "moveLineConst": "Движение по линии Конструкторы",
                    "sumoMech": "Механическое сумо",
                    "sumoIntel": "Интеллектуальное сумо",
                    "circl": "Эстафета",
                    "trip": "Большое путешествие",
                    "missTanos": "Миссия 'Вселенная бесконечна'",
                    "tvorcheskaya": "Творческая категория",
                    "python": "Python",
                    "scratch": "Scratch",
                }
            },
        },
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
    return JSONResponse(content={"categories": CATEGORIES_COUNTRY[category]})


@app.post("/auth")
async def authentication(request: Request):
    """Обработка полученных данных"""
    return RedirectResponse("/auth", status_code=302)


@app.get("/auth/competitions")
async def get_categories(country: str, category: str, practic: str):
    response = COMPETITIONS[country][category][practic]
    return JSONResponse(content=response)

