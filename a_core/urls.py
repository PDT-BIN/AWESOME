from django.conf import settings
from django.conf.urls.static import static as url_static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

from a_posts.views import *
from a_users.views import *

# SITEMAP.
from django.contrib.sitemaps.views import sitemap
from a_posts.sitemaps import *

sitemaps = {
    "static": StaticSitemap,
    "categories": CategorySitemap,
    "postpages": PostpageSitemap,
}

urlpatterns = [
    path(
        "sitemap.xml/",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path(
        "robots.txt/",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path("theboss/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", home_view, name="home"),
    path("category/<str:tag>", home_view, name="category"),
    path("post/create/", post_create_view, name="post-create"),
    path("post/delete/<str:pk>", post_delete_view, name="post-delete"),
    path("post/edit/<str:pk>", post_edit_view, name="post-edit"),
    path("post/<str:pk>", post_page_view, name="post"),
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", profile_edit_view, name="profile-edit"),
    path("profile/delete/", profile_delete_view, name="profile-delete"),
    path("profile/onboarding/", profile_edit_view, name="profile-onboarding"),
    path("profile/verify-email/", profile_verify_email, name="profile-verify-email"),
    path("commentsent/<str:pk>", comment_sent, name="comment-sent"),
    path("comment/delete/<str:pk>", comment_delete_view, name="comment-delete"),
    path("replysent/<str:pk>", reply_sent, name="reply-sent"),
    path("reply/delete/<str:pk>", reply_delete_view, name="reply-delete"),
    path("post/like/<str:pk>", like_post, name="like-post"),
    path("comment/like/<str:pk>", like_comment, name="like-comment"),
    path("reply/like/<str:pk>", like_reply, name="like-reply"),
    path("inbox/", include("a_inbox.urls")),
    path("_/", include("a_landingpages.urls")),
    path("<str:username>/", profile_view, name="userprofile"),
]

urlpatterns += url_static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
