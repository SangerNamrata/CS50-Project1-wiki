from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:titlename>",views.title,name="title"),
    path("searchPage",views.search,name="searchContent"),
    path("newpage",views.create,name="createnewpage"),
    path("saveFile",views.save,name="saveFile"),
    path("editContent",views.edit,name="editPage"),
    path("modified",views.modify,name="modifiedContent"),
    path("randPage",views.randomPage,name="viewrandomPage")
]