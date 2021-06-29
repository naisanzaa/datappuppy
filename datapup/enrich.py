import re
import pydnsbl
import geoip2.webservice

from automon.log.logger import Logging, DEBUG, ERROR

log = Logging('enrich', level=DEBUG)


def PupBlacklistCheck(ip):
    check = pydnsbl.DNSBLIpChecker().check(ip)
    log.debug(f'{ip} {check.blacklisted} {check}')
    return check.blacklisted


def UserAgentCheck(user_agent):
    return


# class PupBlacklistCheck:
#     def __init__(self, ip: str):
#         self.ip = ip
#         self.blocked = pydnsbl.DNSBLIpChecker().check(ip)
#
#     def __repr__(self):
#         return f'{self.ip} {self.blocked}'


class PupGeo:
    def __init__(self, ip: str):
        self.ip = ip
        self.geo = None
