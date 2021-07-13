from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_event", views.create_event, name = "create_event"),
    path("event/<int:event_id>", views.event, name = "event"),
    path("register_event/<int:event_id>", views.register_event, name = "register_event"),
    path("unregister_event/<int:event_id>", views.unregister_event, name = "unregister_event"),
    path("comment", views.comment, name = "comment"),
    path("authorize_comments", views.authorize_comments, name="authorize_comments"),
    path("authorize", views.authorize, name = "authorize"),
    path("reject", views.reject, name = "reject"),
    path("edit/<int:event_id>", views.edit, name = "edit")
]