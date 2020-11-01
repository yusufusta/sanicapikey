from sanic import Sanic
from sanic.response import text, json
from SanicApiKey import SanicApiKey

app = Sanic('test')

async def test(request):
    return json({ "error": 'invalid api key' })

auth = SanicApiKey(app, 'api_key', keys=['hello', 'world'], error=test)

# Header:
# auth = SanicApiKey(app, header='api_key', keys=['hello', 'world'], error=test)

# Form
# auth = SanicApiKey(app, form='api_key', keys=['hello', 'world'], error=test)

@app.route('/')
@auth.key_required
async def test(request):
    return json({'success': True, 'key': auth.get_token()})

if __name__ == '__main__':
    app.run(host='localhost', port=8000)
