"""
定义fastapi实例

"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from customer_service.api.router.chat_router import router
from customer_service.api.router.avatar_router import router as avatar_router
from customer_service.api.router.avatar_ws_router import router as avatar_ws_router
from customer_service.infrastructure.database import init_db_engine, close_db_engine
from customer_service.api.dependencies import init_dialogue_engine
from customer_service.infrastructure.http import init_http_client, close_http_client
from customer_service.infrastructure.avatar import init_avatar_client

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    1.回调 lifespan 的时机：在服务一启动的时候会先来调用（初始化 HTTP 客户端、Redis客户端、MySQL数据库的连接池...）
    2.参数 app 以及类型必须要指定，因为底层 FastAPI 对资源做共享和传递
    3.yield: 让 FASTAPI 处理请求，等应用关闭,才执行 close_db_engine
    :return:
    """
    init_db_engine()
    init_http_client()
    init_dialogue_engine()
    init_avatar_client()
    yield  # FASTAPI 处理请求....
    await close_db_engine()  # 应用关闭的时候才执行到
    await  close_http_client()


app = FastAPI(description="电商小二智能客服应用", lifespan=lifespan)

app.include_router(router)

app.include_router(avatar_router)
app.include_router(avatar_ws_router)
