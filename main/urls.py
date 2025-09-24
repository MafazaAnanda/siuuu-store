from django.urls import path
from main.views import show_main, add_item, show_item, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_item, delete_item

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-item/', add_item, name='add_item'),
    path('item/<str:id>/' , show_item, name="show_item"),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:item_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:item_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('item/<uuid:id>/edit', edit_item, name='edit_item'),
    path('item/<uuid:id>/delete', delete_item, name='delete_item'),
]