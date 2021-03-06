from typing import Optional, Callable

from slack_sdk.socket_mode.request import SocketModeRequest


class AsyncWebSocketMessageListener(Callable):
    async def __call__(
        client: "AsyncBaseSocketModeClient",  # noqa: F821
        message: dict,
        raw_message: Optional[str] = None,
    ):  # noqa: F821
        raise NotImplementedError()


class AsyncSocketModeRequestListener(Callable):
    async def __call__(
        client: "AsyncBaseSocketModeClient", request: SocketModeRequest,  # noqa: F821
    ):  # noqa: F821
        raise NotImplementedError()
