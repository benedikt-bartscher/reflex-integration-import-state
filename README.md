## run test

```bash
poetry install
poetry run pytest tests
```

## traceback

```python
Traceback (most recent call last):
  File "/home/bb/.cache/pypoetry/virtualenvs/reflex-integration-import-state-h_rutTEK-py3.11/lib/python3.11/site-packages/reflex/state.py", line 1116, in _process_event
    yield state._as_state_update(handler, events, final=True)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bb/.cache/pypoetry/virtualenvs/reflex-integration-import-state-h_rutTEK-py3.11/lib/python3.11/site-packages/reflex/state.py", line 1062, in _as_state_update
    delta = state.get_delta()
            ^^^^^^^^^^^^^^^^^
  File "/home/bb/.cache/pypoetry/virtualenvs/reflex-integration-import-state-h_rutTEK-py3.11/lib/python3.11/site-packages/reflex/state.py", line 1186, in get_delta
    delta.update(substates[substate].get_delta())
                 ~~~~~~~~~^^^^^^^^^^
KeyError: 'reuseable_app_state'

---------------------------------------------------------------------------- Captured stderr call ----------------------------------------------------------------------------
INFO:     ('127.0.0.1', 54288) - "WebSocket /?EIO=4&transport=websocket" [accepted]
INFO:     connection open
----------------------------------------------------------------------------- Captured log call ------------------------------------------------------------------------------
ERROR    asyncio:base_events.py:1771 Task exception was never retrieved
future: <Task finished name='Task-25' coro=<AsyncServer._handle_event_internal() done, defined at /home/bb/.cache/pypoetry/virtualenvs/reflex-integration-import-state-h_rutTEK-py3.11/lib/python3.11/site-packages/socketio/async_server.py:605> exception=KeyError('reuseable_app_state')>
Traceback (most recent call last):
  File "/home/bb/.cache/pypoetry/virtualenvs/reflex-integration-import-state-h_rutTEK-py3.11/lib/python3.11/site-packages/reflex/state.py", line 1116, in _process_event
    yield state._as_state_update(handler, events, final=True)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bb/.cache/pypoetry/virtualenvs/reflex-integration-import-state-h_rutTEK-py3.11/lib/python3.11/site-packages/reflex/state.py", line 1062, in _as_state_update
    delta = state.get_delta()
            ^^^^^^^^^^^^^^^^^
  File "/home/bb/.cache/pypoetry/virtualenvs/reflex-integration-import-state-h_rutTEK-py3.11/lib/python3.11/site-packages/reflex/state.py", line 1186, in get_delta
    delta.update(substates[substate].get_delta())
                 ~~~~~~~~~^^^^^^^^^^
KeyError: 'reuseable_app_state'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/bb/.cache/pypoetry/virtualenvs/reflex-integration-import-state-h_rutTEK-py3.11/lib/python3.11/site-packages/socketio/async_server.py", line 607, in _handle_event_internal
    r = await server._trigger_event(data[0], namespace, sid, *data[1:])
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bb/.cache/pypoetry/virtualenvs/reflex-integration-import-state-h_rutTEK-py3.11/lib/python3.11/site-packages/socketio/async_server.py", line 643, in _trigger_event
    return await handler.trigger_event(event, *args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bb/.cache/pypoetry/virtualenvs/reflex-integration-import-state-h_rutTEK-py3.11/lib/python3.11/site-packages/socketio/async_namespace.py", line 37, in trigger_event
    ret = await handler(*args)
          ^^^^^^^^^^^^^^^^^^^^
  File "/home/bb/.cache/pypoetry/virtualenvs/reflex-integration-import-state-h_rutTEK-py3.11/lib/python3.11/site-packages/reflex/app.py", line 1113, in on_event
    async for update in process(self.app, event, sid, headers, client_ip):
  File "/home/bb/.cache/pypoetry/virtualenvs/reflex-integration-import-state-h_rutTEK-py3.11/lib/python3.11/site-packages/reflex/app.py", line 928, in process
    async for update in state._process(event):
  File "/home/bb/.cache/pypoetry/virtualenvs/reflex-integration-import-state-h_rutTEK-py3.11/lib/python3.11/site-packages/reflex/state.py", line 997, in _process
    async for update in self._process_event(
  File "/home/bb/.cache/pypoetry/virtualenvs/reflex-integration-import-state-h_rutTEK-py3.11/lib/python3.11/site-packages/reflex/state.py", line 1122, in _process_event
    yield state._as_state_update(
          ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bb/.cache/pypoetry/virtualenvs/reflex-integration-import-state-h_rutTEK-py3.11/lib/python3.11/site-packages/reflex/state.py", line 1062, in _as_state_update
    delta = state.get_delta()
            ^^^^^^^^^^^^^^^^^
  File "/home/bb/.cache/pypoetry/virtualenvs/reflex-integration-import-state-h_rutTEK-py3.11/lib/python3.11/site-packages/reflex/state.py", line 1186, in get_delta
    delta.update(substates[substate].get_delta())
                 ~~~~~~~~~^^^^^^^^^^
KeyError: 'reuseable_app_state'
```
