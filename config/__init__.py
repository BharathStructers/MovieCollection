from dotenv import find_dotenv,load_dotenv
envf=find_dotenv()
load_dotenv(envf)

import os

DATABASE_URL=os.getenv("DATABASE_URL")