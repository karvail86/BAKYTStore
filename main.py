from fastapi import FastAPI
from shop_app.api import users, category, auth
from shop_app.admin.setup import setup_admin
import uvicorn

shop_app = FastAPI(title='Bakyt Store')
shop_app.include_router(users.user_router)
shop_app.include_router(category.category_router)
shop_app.include_router(auth.auth_router)
setup_admin(shop_app)

if __name__ == '__main__':
    uvicorn.run('main:shop_app', host="127.0.0.1", port=8080, reload=True)