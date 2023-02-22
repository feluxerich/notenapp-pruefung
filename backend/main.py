import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from settings import settings
from database import engine
from student import models
from student.router import router as student_router
from marks.router import router as mark_router

models.Base.metadata.create_all(bind=engine)


def create_app():
    app = FastAPI(
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
        debug=settings.DEBUG,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers=['*'],
        allow_credentials=True,
    )
    app.include_router(student_router, prefix=f'{settings.API_ROUTE}/student')

    app.include_router(mark_router, prefix=f'{settings.API_ROUTE}/marks')

    @app.get('/', name='Index, redirects to openapi docs')
    async def root():
        return RedirectResponse(url='/docs')

    return app


if __name__ == '__main__':
    uvicorn.run(create_app(), host='0.0.0.0', port=1337)
