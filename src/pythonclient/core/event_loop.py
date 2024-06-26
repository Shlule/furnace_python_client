"""
@author Elouan Rogliano

the event loop is running in a different thread to not freeze the dcc.

"""

import asyncio
import traceback
from concurrent import futures
from contextlib import suppress
from threading import Thread
from typing import Coroutine
import gc

from pythonclient.utils.log import logger

class EventLoop:
    """
    Class responsible to manage the async event loop, to deal with websocket
    connection, and action execution
    """
    JOIN_THREAD_TIMEOUT = 2

    def __init__(self) -> None:
        self.loop: asyncio.AbstractEventLoop = asyncio.new_event_loop()
        self.thread: Thread = Thread()

    @property
    def is_running(self) -> bool:
        return self.loop.is_running()
    
    def _start_event_loop(self) -> None:
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

        #clear it once complete
        self._clear_event_loop()
    
    def _clear_event_loop(self) -> None : 
        if self.is_running:
            logger.warning("cannot clear loop because already in use, must be stop ")
            return
        logger.info("clearing event loop ")

        for task in asyncio.all_tasks(self.loop):
            task.cancel()
            with suppress(asyncio.CancelledError):
                self.loop.run_until_complete(task)

                 # Create a new loop and let the old one get garbage collected
        self.loop = asyncio.new_event_loop()
        # Trigger the garbage collection
        gc.collect()

        logger.info("Event loop cleared")

    def start(self) -> None:
        """
        initialize the event loop's task and run it in a different thread
        """
        if self.is_running:
            logger.warning("Could not start event loop: The loop is already running")
            return

        logger.info("Starting the event loop")
        self.thread = Thread(target=self._start_event_loop, daemon=True)
        self.thread.start()
        
    def stop(self) -> None:
        """
        Ask to all the event loop's tasks to stop and join the thread to the main thread
        if there is one running
        """
        if not self.loop.is_running():
            return

        self.loop.call_soon_threadsafe(self.loop.stop)
        self.thread.join(self.JOIN_THREAD_TIMEOUT)
        if self.thread.is_alive():
            logger.error("Could not stop the event loop thread: timout exeded")
        else:
            logger.info("Event loop stopped")

    def register_task(self, coroutine: Coroutine) -> futures.Future:
        """
        Helper to add tasks to the event loop from a different thread
        """
        # Test if the function is called from the event loop or from outside
        if not self.is_running:
            logger.warning(
                "Could not register task %s: The event loop is not running", coroutine
            )
            future: futures.Future = futures.Future()
            future.set_result(None)
            return future

        future = asyncio.run_coroutine_threadsafe(coroutine, self.loop)

        def callback(task_result: futures.Future):
            if task_result.cancelled():
                return

            exception = task_result.exception()
            if exception:
                logger.error(
                    "Exception raised in the task %s: %s", coroutine, exception
                )
                traceback.print_tb(exception.__traceback__)
        future.add_done_callback(callback)
        return future
        