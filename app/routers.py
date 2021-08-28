from app.views import GetAllToursView
from app import app


app.add_route(GetAllToursView.as_view(), '/tours')
