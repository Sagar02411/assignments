from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType, NameEmail

config = ConnectionConfig(
    
)

@app.post("/emailbackground")
async def send_in_background(
    background_tasks: BackgroundTasks,
    email: EmailSchema
    ) -> JSONResponse:

    message = MessageSchema(
        subject="Fastapi mail module",
        recipients=email.dict().get("email"),
        body="Simple background task",
        subtype=MessageType.plain)

    fm = FastMail(config)

    background_tasks.add_task(fm.send_message,message)

    return JSONResponse(status_code=200, content={
        "message": "email has been sent"
        })