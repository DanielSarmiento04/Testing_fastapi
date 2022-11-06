from functools import wraps
from fastapi import  Request

def do_something_with_request_object(request: Request):
    print(request)

def auth_required(handler):
    async def wrapper(request: Request, *args, **kwargs):
        do_something_with_request_object(request)
        return await handler(*args, **kwargs)

    # Fix signature of wrapper
    import inspect
    wrapper.__signature__ = inspect.Signature(
        parameters = [
            # Use all parameters from handler
            *inspect.signature(handler).parameters.values(),

            # Skip *args and **kwargs from wrapper parameters:
            *filter(
                lambda p: p.kind not in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD),
                inspect.signature(wrapper).parameters.values()
            )
        ],
        return_annotation = inspect.signature(handler).return_annotation,
    )

    return wrapper

