from loguru import logger
from itertools import takewhile
import sys
import traceback
import re


def custom_format(record):
    frames = [_ for _ in traceback.extract_stack() if not re.findall('(/loguru/|/env|/Library)', _.filename)]
    stack = []
    for n, f in enumerate(frames):
        filename = re.sub(r'^.*/(.*?)\..{1,3}$', r'\g<1>', f.filename)
        filename = '' if n and frames[n - 1].filename == f.filename else filename
        name = f.name.replace('<module>', '')
        stack.append(f'{filename}:{name}:{f.lineno}')
    record["extra"]["stack"] = ' > '.join(stack)
    # return "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {extra[stack]} | {message}\n{exception}"
    # return "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> |
    # <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    return '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>' \
           ' | ' \
           '<level>{level: <8}</level>' \
           ' | ' \
           '<level>{message}</level>' \
           ' | ' \
           '<fg #666>{extra[stack]}</>' \
           ''


def foo():
    logger.info("Test")


def bar():
    foo()


logger.remove()
logger.add(sys.stderr, format=custom_format)

bar()
