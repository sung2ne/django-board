from django.urls import path
from . import views


app_name = 'board'

urlpatterns = [
    path("board_list/", views.board_list, name="board_list"),
    path("board_create/", views.board_create, name="board_create"),
    path("board_read/<int:board_id>", views.board_read, name="board_read"),
    path("board_update/<int:board_id>", views.board_update, name="board_update"),
    path("board_delete/<int:board_id>", views.board_delete, name="board_delete"),
]
