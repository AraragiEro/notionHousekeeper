from functools import wraps
import traceback

class InfoAndPass(Exception):
    def __init__(self, info) -> None:
        self.info = info

    def PrintInfo(self):
        print(self.info)

def TryToDo(Func):
    @wraps(Func)
    def wrapTheFunction(*args, **kwargs):
        try:
            return Func(*args, **kwargs)
        except InfoAndPass as err:
            err.PrintInfo
        except:
            traceback.print_exc()
    return wrapTheFunction
