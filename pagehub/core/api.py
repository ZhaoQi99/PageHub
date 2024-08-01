from ninja import NinjaAPI
from record.api import router as record_router

api = NinjaAPI()

api.add_router("/record/", record_router)
