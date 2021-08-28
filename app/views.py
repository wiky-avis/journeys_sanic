from sanic_jinja2 import SanicJinja2
from app import app
from sanic.response import json
from app import db_api

from sanic.views import HTTPMethodView

jinja = SanicJinja2(app)
jrender = jinja.render


@app.route('/')
async def index(request):
    page = dict()
    page['header'] = 'No Posts Found :('
    page['text'] = 'Sorry, We couldn\'t find any posts.'
    return jrender('hello.html', request, page=page)


class GetAllToursView(HTTPMethodView):
    async def get(self, request):
        tours = await db_api.get_all_tours()
        return json(tours, status=200)


app.add_route(GetAllToursView.as_view(), '/tours')
