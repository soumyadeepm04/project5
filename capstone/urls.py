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
    path("edit/<int:event_id>", views.edit, name = "edit"),
    path("favorite/<int:event_id>", views.favorite, name = "favorite"),
    path("unfavorite/<int:event_id>", views.unfavorite, name = "unfavorite"),
    path("favorite_events", views.favorite_events, name = "favorite_events"),
    path("delete_event/<int:event_id>", views.delete_event, name = "delete_event"),
    path("deleted_events", views.deleted_events, name = "deleted_events"),
    path("restore_approval/<int:event_id>", views.restore_approval, name = "restore_approval"),
    path("remove_approval/<int:event_id>", views.remove_approval, name = "remove_approval"),
    path("approve_restore_requests", views.approve_restore_requests, name = "approve_restore_requests"),
    path("approve_restoration/<int:event_id>", views.approve_restoration, name="approve_restoration"),
    path("reject_restoration/<int:event_id>", views.reject_restoration, name="reject_restoration")
]