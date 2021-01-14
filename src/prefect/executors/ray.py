import asyncio
import logging
import uuid
import sys
import weakref
from contextlib import contextmanager
from typing import Any, Callable, Iterator, TYPE_CHECKING, Union, Optional

from prefect import context
from prefect.executors.base import Executor
from prefect.utilities.importtools import import_object


class RayExecutor(Executor):
    def __init__(
        self):
      pass

    @contextmanager
    def start(self) -> Iterator[None]:
        pass


    def wait(self, futures: Any) -> Any:
        pass
