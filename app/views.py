from sanic_jinja2 import SanicJinja2
from app import app


jinja = SanicJinja2(app)
jrender = jinja.render


@app.route('/')
async def index(request):
    page = dict()
    page['header'] = 'No Posts Found :('
    page['text'] = 'Sorry, We couldn\'t find any posts.'
    return jrender('hello.html', request, page=page)
