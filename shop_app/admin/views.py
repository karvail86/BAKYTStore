from pydantic_core.core_schema import model_field

from shop_app.dataset.models import UserProfile, Category, Product, RefreshToken
from sqladmin import ModelView

class UserProfileAdmin(ModelView, model= UserProfile):
    column_list = [UserProfile.first_name, UserProfile.last_name]


class CategoryAdmin(ModelView, model= Category):
    column_list = [Category.id, Category.category_name]

class ProductAdmin(ModelView, model=Product):
    column_list = [Product.product_name]