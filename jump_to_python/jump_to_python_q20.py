import re

input_string = """
park@naver.com
kim@daum.net
lee@myhome.co.kr
"""


pat = re.compile(".*[@].*[.](?=com$|net$)")
for v in input_string.split("\n"):
    print(pat.match(v))
