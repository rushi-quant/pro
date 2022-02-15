# -*- coding:utf-8 -*-
# cython: language_level=3
"""
Tools Bag.

Author: HuangTao
Date:   2018/04/28
Email:  huangtao@ifclover.com
"""

import uuid
import time
import decimal
import datetime
import hmac
import base64
import hashlib
from urllib import parse

# 休眠函数
# 参数值：secs为数值类型。参数为秒数，例如：Sleep(1)为休眠1秒。
def Sleep(secs):
    time.sleep(secs)

# 返回秒级别时间戳
def Unix():
    t = time.time()
    return int(t)

def get_cur_timestamp():
    """Get current timestamp(second)."""
    ts = int(time.time())
    return ts


def get_cur_timestamp_ms():
    """Get current timestamp(millisecond)."""
    ts = int(time.time() * 1000)
    return ts


def get_datetime_str(fmt="%Y-%m-%d %H:%M:%S"):
    """Get date time string, year + month + day + hour + minute + second.

    Args:
        fmt: Date format, default is `%Y-%m-%d %H:%M:%S`.

    Returns:
        str_dt: Date time string.
    """
    today = datetime.datetime.today()
    str_dt = today.strftime(fmt)
    return str_dt


def get_date_str(fmt="%Y%m%d", delta_days=0):
    """Get date string, year + month + day.

    Args:
        fmt: Date format, default is `%Y%m%d`.
        delta_days: Delta days for currently, default is 0.

    Returns:
        str_d: Date string.
    """
    day = datetime.datetime.today()
    if delta_days:
        day += datetime.timedelta(days=delta_days)
    str_d = day.strftime(fmt)
    return str_d


def ts_to_datetime_str(ts=None, fmt="%Y-%m-%d %H:%M:%S"):
    """Convert timestamp to date time string.

    Args:
        ts: Timestamp, millisecond.
        fmt: Date time format, default is `%Y-%m-%d %H:%M:%S`.

    Returns:
        Date time string.
    """
    if not ts:
        ts = get_cur_timestamp()
    dt = datetime.datetime.fromtimestamp(int(ts))
    return dt.strftime(fmt)


def datetime_str_to_ts(dt_str, fmt="%Y-%m-%d %H:%M:%S"):
    """Convert date time string to timestamp.

    Args:
        dt_str: Date time string.
        fmt: Date time format, default is `%Y-%m-%d %H:%M:%S`.

    Returns:
        ts: Timestamp(second).
    """
    ts = int(time.mktime(datetime.datetime.strptime(dt_str, fmt).timetuple()))
    return ts


def datetime_to_datetime_str(dt=None, fmt="%Y%m%d", delta_day=0):
    """Convert date time string to date time string.

    Args:
        dt: datetime object.
        fmt: Date time format, default is `%Y-%m-%d`.
        delta_day: Delta days, default is 0.

    Returns:
        str_d: Date time string.
    """
    if not dt:
        dt = datetime.datetime.today()
    if delta_day:
        dt += datetime.timedelta(days=delta_day)
    str_d = dt.strftime(fmt)
    return str_d


def get_utc_time():
    """Get current UTC time."""
    utc_t = datetime.datetime.utcnow()
    return utc_t


def utctime_str_to_ts(utctime_str, fmt="%Y-%m-%dT%H:%M:%S.%fZ"):
    """Convert UTC time string to timestamp(second).

    Args:
        utctime_str: UTC time string, e.g. `2019-03-04T09:14:27.806Z`.
        fmt: UTC time format, e.g. `%Y-%m-%dT%H:%M:%S.%fZ`.

    Returns:
        timestamp: Timestamp(second).
    """
    dt = datetime.datetime.strptime(utctime_str, fmt)
    timestamp = int(dt.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None).timestamp())
    return timestamp


def utctime_str_to_ms(utctime_str, fmt="%Y-%m-%dT%H:%M:%S.%fZ"):
    """Convert UTC time string to timestamp(millisecond).

    Args:
        utctime_str: UTC time string, e.g. `2019-03-04T09:14:27.806Z`.
        fmt: UTC time format, e.g. `%Y-%m-%dT%H:%M:%S.%fZ`.

    Returns:
        timestamp: Timestamp(millisecond).
    """
    dt = datetime.datetime.strptime(utctime_str, fmt)
    timestamp = int(dt.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None).timestamp() * 1000)
    return timestamp


def ms_to_utctime_str(ms: int, fmt="%Y-%m-%dT%H:%M:%S.%fZ"):
    """Convert timestamp(millisecond) to UTC time string.

    Args:
        ms: Timestamp(millisecond).
        fmt: UTC time format, e.g. `%Y-%m-%dT%H:%M:%S.%fZ`.

    Returns:
        utctime_str: UTC time string, e.g. `2019-03-04T09:14:27.806Z`.
    """
    utc_dt = datetime.datetime.utcfromtimestamp(ms / 1000.)
    utc_dt.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
    utctime_str = utc_dt.strftime(fmt)
    return utctime_str


def get_utctime_str(fmt="%Y-%m-%dT%H:%M:%S.%fZ"):
    """Get current UTC time string.

    Args:
        fmt: UTC time format, e.g. `%Y-%m-%dT%H:%M:%S.%fZ`.

    Returns:
        utctime_str: UTC time string, e.g. `2019-03-04T09:14:27.806Z`.
    """
    utctime = get_utc_time()
    utctime_str = utctime.strftime(fmt)
    return utctime_str


def get_uuid1():
    """Generate a UUID based on the host ID and current time

    Returns:
        s: UUID1 string.
    """
    uid1 = uuid.uuid1()
    s = str(uid1)
    return s


def get_uuid3(str_in):
    """Generate a UUID using an MD5 hash of a namespace UUID and a name

    Args:
        str_in: Input string.

    Returns:
        s: UUID3 string.
    """
    uid3 = uuid.uuid3(uuid.NAMESPACE_DNS, str_in)
    s = str(uid3)
    return s


def get_uuid4():
    """Generate a random UUID.

    Returns:
        s: UUID5 string.
    """
    uid4 = uuid.uuid4()
    s = str(uid4)
    return s


def get_uuid5(str_in):
    """Generate a UUID using a SHA-1 hash of a namespace UUID and a name

    Args:
        str_in: Input string.

    Returns:
        s: UUID5 string.
    """
    uid5 = uuid.uuid5(uuid.NAMESPACE_DNS, str_in)
    s = str(uid5)
    return s


def float_to_str(f, p=20):
    """Convert the given float to a string, without resorting to scientific notation.

    Args:
        f: Float params.
        p: Precision length.

    Returns:
        s: String format data.
    """
    if type(f) == str:
        f = float(f)
    ctx = decimal.Context(p)
    d1 = ctx.create_decimal(repr(f))
    s = format(d1, 'f')
    return s


class TelegramBot:
    """ Telegram Bot.
        Docs: https://core.telegram.org/api
    """
    BASE_URL = "https://api.telegram.org"

    @classmethod
    async def send_text_msg(cls, token: str, chat_id: str, content: str):
        """ Send text message.

        Args:
            token: Telegram bot token.
            chat_id: Telegram chat id.
            content: The message string that you want to send.

        Returns:
            success: HTTP response data. If something wrong, this field is None.
            error: If something wrong, this field will holding a Error information, otherwise it's None.
        """
        url = "{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={content}".format(
            base_url=cls.BASE_URL,
            token=token,
            chat_id=chat_id,
            content=content
        )
        from aioquant.utils.web import AsyncHttpRequests
        _, success, error = await AsyncHttpRequests.fetch("GET", url)
        return success, error


class DingTalk:
    """ DingTalk Bot API.
        Docs: https://open-doc.dingtalk.com/microapp/serverapi2/qf2nxq
    """
    BASE_URL = "https://oapi.dingtalk.com/robot/send?access_token="

    @classmethod
    async def send_text_msg(cls, access_token: str, content: str, phones: list = None, is_at_all: bool = False,
                            secret_key: str = None):
        """ Send text message.

        Args:
            access_token: DingTalk Access Token.
            content: Message content to be sent.
            phones: Phone numbers to be @.
            is_at_all: Is @ all members? default is False.
            secret_key: Secret key for generate signature.

        Returns:
            success: HTTP response data. If something wrong, this field is None.
            error: If something wrong, this field will holding a Error information, otherwise it's None.
        """
        body = {
            "msgtype": "text",
            "text": {
                "content": content
            }
        }
        if is_at_all:
            body["at"] = {"isAtAll": True}
        if phones:
            body["at"] = {"atMobiles": phones}
        if secret_key:
            timestamp = get_cur_timestamp_ms()
            string_to_sign_enc = "{}\n{}".format(timestamp, secret_key).encode("utf-8")
            hmac_code = hmac.new(secret_key.encode("utf-8"), string_to_sign_enc, digestmod=hashlib.sha256).digest()
            sign = parse.quote(base64.b64encode(hmac_code))
            url = cls.BASE_URL + access_token + "&timestamp={}".format(timestamp) + "&sign={}".format(sign)
        else:
            url = cls.BASE_URL + access_token
        headers = {"Content-Type": "application/json"}
        from aioquant.utils.web import AsyncHttpRequests
        _, success, error = await AsyncHttpRequests.post(url, data=body, headers=headers)
        return success, error

    @classmethod
    async def send_markdown_msg(cls, access_token: str, title: str, text: str, phones: list = None,
                                is_at_all: bool = False):
        """ Send markdown message.

        Args:
            access_token: DingTalk Access Token.
            title: Message title.
            text: Message content to be sent.
            phones: Phone numbers to be @.
            is_at_all: Is @ all members? default is False.

        Returns:
            success: HTTP response data. If something wrong, this field is None.
            error: If something wrong, this field will holding a Error information, otherwise it's None.
        """
        body = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": text
            }
        }
        if is_at_all:
            body["at"] = {"isAtAll": True}
        if phones:
            body["at"] = {"atMobiles": phones}
        url = cls.BASE_URL + access_token
        headers = {"Content-Type": "application/json"}
        from aioquant.utils.web import AsyncHttpRequests
        _, success, error = await AsyncHttpRequests.post(url, data=body, headers=headers)
        return success, error


class SendEmail:
    """ Send email.

    Attributes:
        host: Mail server host.
        port: Mail server port.
        username: Email username, e.g. test@gmail.com
        password: Email password.
        to_emails: Email list, which mails to be send.
        subject: Email subject(title).
        content: Email content(body).
        timeout: Send timeout time(seconds), default is 30s.
        tls: If use TLS, default is True.
    """

    def __init__(self, host: str, port: int, username: str, password: str, to_emails: list, subject: str, content: str,
                 timeout: int = 30, tls: bool = True):
        """Initialize."""
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._to_emails = to_emails
        self._subject = subject
        self._content = content
        self._timeout = timeout
        self._tls = tls

    async def send(self):
        """Send a email."""
        import email
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        import aiosmtplib
        from aioquant.utils import logger

        message = MIMEMultipart("related")
        message["Subject"] = self._subject
        message["From"] = self._username
        message["To"] = ",".join(self._to_emails)
        message["Date"] = email.utils.formatdate()
        message.preamble = "This is a multi-part message in MIME format."
        ma = MIMEMultipart("alternative")
        mt = MIMEText(self._content, "plain", "GB2312")
        ma.attach(mt)
        message.attach(ma)

        smtp = aiosmtplib.SMTP(hostname=self._host, port=self._port, timeout=self._timeout, use_tls=self._tls)
        await smtp.connect()
        await smtp.login(self._username, self._password)
        await smtp.send_message(message)
        logger.info("send email success! FROM:", self._username, "TO:", self._to_emails, "CONTENT:", self._content,
                    caller=self)


class AliyunPhoneCall:
    """ Aliyun Phone Call API.
        Docs: https://dyvms.console.aliyun.com/dyvms.htm
    """

    @classmethod
    async def call_phone(cls, access_key: str, secret_key: str, _from: str, to: str, code: str,
                         region_id: str = "cn-hangzhou"):
        """ Initialize.

        Args:
            access_key: Aliyun Access Key.
            secret_key: Aliyun Secret Key.
            _from: Call out phone, eg: 08177112233
            to: Which phone to be called, eg: 13123456789
            code: Phone ring code, e.g. `64096325-d22e-4cf8-9f52-abc12345.wav`
            region_id: Which region to be used, default is `cn-hangzhou`.

        Returns:
            success: HTTP response data. If something wrong, this field is None.
            error: If something wrong, this field will holding a Error information, otherwise it's None.
        """
        def percent_encode(s):
            res = parse.quote_plus(s.encode("utf8"))
            res = res.replace("+", "%20").replace("*", "%2A").replace("%7E", "~")
            return res

        url = "http://dyvmsapi.aliyuncs.com/"
        out_id = get_uuid1()
        nonce = get_uuid1()
        timestamp = datetime_to_datetime_str(get_utc_time(), fmt="%Y-%m-%dT%H:%M:%S.%fZ")
        params = {
            "VoiceCode": code,
            "OutId": out_id,
            "CalledNumber": to,
            "CalledShowNumber": _from,
            "Version": "2017-05-25",
            "Action": "SingleCallByVoice",
            "Format": "JSON",
            "RegionId": region_id,
            "Timestamp": timestamp,
            "SignatureMethod": "HMAC-SHA1",
            "SignatureType": "",
            "SignatureVersion": "1.0",
            "SignatureNonce": nonce,
            "AccessKeyId": access_key
        }
        query = "&".join(["{}={}".format(percent_encode(k), percent_encode(params[k])) for k in sorted(params.keys())])
        str_to_sign = "GET&%2F&" + percent_encode(query)
        h = hmac.new(bytes(secret_key + "&", "utf8"), bytes(str_to_sign, "utf8"), digestmod=hashlib.sha1)
        signature = base64.b64encode(h.digest()).decode()
        params["Signature"] = signature
        from aioquant.utils.web import AsyncHttpRequests
        _, success, error = await AsyncHttpRequests.fetch("GET", url, params=params)
        return success, error


class Twilio:
    """ Twilio Phone Call API.
        Docs: https://www.twilio.com/
    """
    BASE_URL = "https://api.twilio.com"

    @classmethod
    async def call_phone(cls, account_sid: str, token: str, _from: str, to: str, voice_url: str = None):
        """ Call phone.

        Args:
            account_sid: Twilio account id.
            token: Twilio Auth Token.
            _from: Call out phone, eg: +17173666666
            to: Which phone to be called, eg: +8513123456789
            voice_url: Phone ring url, e.g. http://demo.twilio.com/docs/voice.xml

        Returns:
            success: HTTP response data. If something wrong, this field is None.
            error: If something wrong, this field will holding a Error information, otherwise it's None.
        """
        url = "https://{account_sid}:{token}@api.twilio.com/2010-04-01/Accounts/{account_sid}/Calls.json".format(
            account_sid=account_sid,
            token=token
        )
        if not voice_url:
            voice_url = "http://demo.twilio.com/docs/voice.xml"
        data = {
            "Url": voice_url,
            "To": to,
            "From": _from
        }
        from aioquant.utils.web import AsyncHttpRequests
        _, success, error = await AsyncHttpRequests.fetch("POST", url, body=data)
        return success, error


class AES_ENCRYPT:
    """ AES encrypt.

    Attributes:
        key: AES key, length must be 16|24|32.
    """

    def __init__(self, key):
        from Crypto.Cipher import AES
        self.key = key.encode("utf8")  # length must be 16|24|32.
        self.mode = AES.MODE_CBC
        self.IV = key[:16].encode("utf8")

    def encrypt(self, text):
        from Crypto.Cipher import AES
        from binascii import b2a_hex
        if isinstance(text, bytes):
            text = text.decode()
        cryptor = AES.new(self.key, self.mode, self.IV)
        length = 16
        count = len(text)
        if count % length != 0:
            add = length - (count % length)
        else:
            add = 0
        text = text + ("\0" * add)
        ciphertext = cryptor.encrypt(text.encode())
        return b2a_hex(ciphertext).decode()

    def decrypt(self, text):
        from Crypto.Cipher import AES
        from binascii import a2b_hex
        cryptor = AES.new(self.key, self.mode, self.IV)
        if not isinstance(text, bytes):
            text = text.encode()
        plain_text = cryptor.decrypt(a2b_hex(text)).decode()
        return plain_text.rstrip("\0")
