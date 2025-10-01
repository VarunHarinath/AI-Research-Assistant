from fastapi import FastAPI
from contextlib import asynccontextmanager
from RPC.rpcConsumer import Rpc
import threading

app = FastAPI(title="Ai research Assistant")

rpc_worker = Rpc()

@asynccontextmanager
async def lifespan(app: FastAPI):
    rpc_worker.QueueDeclareAndBind()
    
    thread = threading.Thread(target=rpc_worker.consumeMessages,daemon=True)
    thread.start()
    yield

app.router.lifespan = lifespan
    

@app.get("/")
def home():
    return "Hello World"


