#
# Серверное приложение для соединений
#

import asyncio
from asyncio import transports
from typing import Optional


class ServerProtocol(asyncio.Protocol):
    login: str = None
    server: 'Server'
    transport: transports.Transport

    def __init__(self, server: 'Server'):
        self.server = server

    def data_received(self, data: bytes) -> None:
        print(data)
        decoded = data.decode()
        if self.login is not None:
            self.send_message(decoded)
        else:
            if decoded.startswith("login:"):
                self.handle_login(decoded)
            else:
                self.transport.write("Неправильный логин \n".encode())


    def connection_made(self, transport: transports.BaseTransport) -> None:
        self.server.clients.append(self)
        self.transport = transport

        print("Пришёл новый клиент!!")

    def connection_lost(self, exc: Optional[Exception]) -> None:
        self.server.clients.remove(self)
        print("Клиент вышел")

    def send_message(self, content: str):
        message = f"{self.login}: {content}\n"
        self.server.message_pool.append(message)
        for user in self.server.clients:
            user.transport.write(message.encode())

    def handle_login(self, decoded: str):
        login = decoded.replace("login:", "").replace("\r\n", "")
        if not self.is_exist_login(login):
            self.login = login
            self.transport.write(f"Привет, {self.login} !\n".encode())
            self.send_history()
        else:
            self.transport.write(f"Логин {login} занят, попробуйте другой\n".encode())

    def is_exist_login(self, login: str) -> bool:
        for client in self.server.clients:
            if login == client.login:
                return True
        return False

    def send_history(self):
        for msg in self.server.message_pool[-10:]:
            self.transport.write(msg.encode())

class Server:
    clients: list
    message_pool: list

    def __init__(self):
        self.clients = []
        self.message_pool = []

    def build_protocol(self):
        return ServerProtocol(self)

    async def start(self):
        loop = asyncio.get_event_loop()

        coroutine = await loop.create_server(
            self.build_protocol,
            "127.0.0.1",
            8888
        )

        print("Сервер запущен ....")
        await coroutine.serve_forever()


process = Server()
try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print("Сервер остановлен вручную")
