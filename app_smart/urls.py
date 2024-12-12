from django.urls import path, include
from . import views
from .api.viewsets import TemperatureDataList, UmidadeDataList, LuminosidadeDataList, ContadorDataList 
from .views import RegisterView, LoginView, load_temperature_data, load_umidade_data, load_luminosidade_data, load_contador_data
from app_smart.api.viewsets import CreateUser, SensorViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from app_smart.views import CSVUploadView, process_csv_upload
from app_smart.api.viewsets import(
    CreateUser,
    SensorViewSet,
    TemperaturaDataViewSet,
)

router = DefaultRouter()
router.register(r'sensores', SensorViewSet)
router.register(r'temperatura', TemperaturaDataViewSet)

urlpatterns = [
    path('', views.abre_index, name='abre_index'),
    path('api/create_user/', CreateUser.as_view(), name='create_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('process-upload/', process_csv_upload, name='process-upload'),
     path('api/register', RegisterView.as_view(), name='register'),
    path('api/login', LoginView.as_view(), name='login'),
    path('api/temp', load_temperature_data, name='temperatura_data'),
    path('api/temperatura', TemperatureDataList.as_view(), name='temperatura'),

    
     path('api/umi/', load_umidade_data, name='umidade_data'),
    path('api/umidade/', UmidadeDataList.as_view(), name='umidade'),
    path('api/lumi/', load_luminosidade_data, name='luminosidade_data'),
    path('api/luminosidade/', LuminosidadeDataList.as_view(), name='luminosidade'),
    path('api/cont/', load_contador_data, name='contador_data'),
    path('api/contador/', ContadorDataList.as_view(), name='contador'),
]
    # path('api/upload/temperatura/', TemperaturaDataViewSet.as_view({'post': 'upload'}), name='upload_temperatura'),
