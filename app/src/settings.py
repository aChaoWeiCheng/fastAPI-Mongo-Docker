
import os
import motor.motor_asyncio

#----------------- Database variables (MongoDB) --------------------------
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["DB_URL"])
db = client.TestDB