from pika.adapters import base_connection as base_connection
from pika.adapters.utils import nbio_interface as nbio_interface, selector_ioloop_adapter as selector_ioloop_adapter
from typing import Any, Optional

LOGGER: Any

class TornadoConnection(base_connection.BaseConnection):
    def __init__(self, parameters: Optional[Any] = ..., on_open_callback: Optional[Any] = ..., on_open_error_callback: Optional[Any] = ..., on_close_callback: Optional[Any] = ..., custom_ioloop: Optional[Any] = ..., internal_connection_workflow: bool = ...) -> None: ...
    @classmethod
    def create_connection(cls, connection_configs: Any, on_done: Any, custom_ioloop: Optional[Any] = ..., workflow: Optional[Any] = ...): ...
