from aiohttp import web
from async_models import Advertisement, Session,Base, engine
from typing import Type
import json
from sqlalchemy.exc import IntegrityError
from aiohttp.typedefs import Handler
app = web.Application()

'''пробный запрос'''
# async def hello_world(request: web.Request):
#     # response = web.Response(text='Hello,world')
#     response = web.json_response({"Hello":"Word"})
#     return response
# app.add_routes([
#     web.post('/hello/world',hello_world)])
# web.run_app(app)

async def orm_context(app:web.Application):
    print('Starting')
    async with engine.begin() as conn:
        await conn.run_sync(Advertisement.metadata.create_all)
    yield
    await engine.dispose()
    print('Finish')
app.cleanup_ctx.append(orm_context)
@web.middleware
async def session_middleware(request: web.Request,handler: Handler):
    async with Session() as session:
        request.session = session
        response = await handler(request)
        return response


app.middlewares.append(session_middleware)

'''шаблон'''
def get_http_error(error_class:Type[web.HTTPClientError], massage):
    return error_class(text=json.dumps({'error':massage}),
                       content_type= "application/json")

async def get_advertisement_by_id(session: Session,advertisement_id:int)->Advertisement:
    advertisement = await session.get(Advertisement,advertisement_id)
    if advertisement is None:
        raise get_http_error(web.HTTPNotFound,f'Avertisement with id: {advertisement_id} is not found')
    return advertisement


async def add_advertisement(session: Session, advertisement: Advertisement):
    try:
        session.add(advertisement)
        await session.commit()
    except IntegrityError as error:
        raise get_http_error(web.HTTPConflict,'User is already exists')
    return advertisement

'''создаю бд'''


class AdvertisementView(web.View):
    @property
    def advertisement_id(self):
        return int(self.request.match_info['advertisement_id'])
    @property
    def session(self) -> Session:
        return self.request.session
    async def get(self):
        advertisement = await get_advertisement_by_id(self.session, self.advertisement_id)
        return web.json_response(advertisement.dict)


    async def post(self):
        advertisement_data = await self.request.json()
        advertisement = Advertisement(**advertisement_data)
        advertisement = await add_advertisement(self.session, advertisement)
        return web.json_response({'id': advertisement.id})

    async def patch(self):
        advertisement = await get_advertisement_by_id(self.session,self.advertisement_id)
        advertisement_data = await self.request.json()
        for field, value in advertisement_data.items():
            setattr(advertisement, field, value)
            await add_advertisement(self.session,advertisement)
        return web.json_response({'id': advertisement.id})

    async def delete(self):
        advertisement = await get_advertisement_by_id(self.session, self.advertisement_id)
        await self.session.delete(advertisement)
        await self.session.commit()
        return web.json_response({'Status':'Deleted'})

app.add_routes([
    web.get('/advertisement/{advertisement_id:\d+}',AdvertisementView),
    web.patch('/advertisement/{advertisement_id:\d+}',AdvertisementView),
    web.delete('/advertisement/{advertisement_id:\d+}',AdvertisementView),
    web.post('/advertisement',AdvertisementView)])
web.run_app(app)