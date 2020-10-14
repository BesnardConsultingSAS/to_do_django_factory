from to_do_item.views import ToDoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", ToDoViewSet)
urlpatterns = router.urls
