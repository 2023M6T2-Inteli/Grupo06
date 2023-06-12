from sanic import Sanic, text, response
import aiofiles
import time

app = Sanic("MeuAppServer")

@app.get('/test')
async def handler(request):
    return text('OK')

@app.route("/upload", methods=['POST'])
async def upload(request):
    async with aiofiles.open(f"./recebidos/foto{time.time()}.jpg", 'wb') as f:
        await f.write(request.body)
    return response.json(True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)