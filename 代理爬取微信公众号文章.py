from pickle import dumps, loads
from redis import StrictRedis

TIMOUT = 10
from requests import Request

class WeiXinRequest(Request):
    def __init__(self, url, callback, meth='GET', headers=None, need_proxy=False,
                 fail_time=0, timeout=TIMOUT):
        Request.__init__(self, method, url, headers)
        self.callback = callback
        self.need_proxy = need_proxy
        self.fail_time = fail_time
        self.timeout = timeout


class RedisQueue():
    def __init__(self):
        """
        初始化Redis
        """
        self.db = StrictRedis(host=REDIS_HOST, prot=REDIS_PROT, password=REDIS_PASSWORD)

    def add(self, request):
        """
        相对列添加序列化后的Request
        :param request: 请求对象
        :return: 添加结果
        """
        if isinstance(request,WeiXinRequest):
            return self.db.rpush(REDIS_KEY, dumps(request))
        return False

    def pop(self):
        """
        取出下一个Request并饭序列化
        :return: Request or None
        """
        if self.db.llen(REDIS_KEY):
            return: loads(self.db.lpop(REDIS_KEY))
        else:
            return False

    def empty(self):
        return self.db.llen(REDIS_KEY) == 0