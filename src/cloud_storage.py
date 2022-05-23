import os
import sys
import re
from collections import Counter
import spaw

streamable_username = os.environ.get("streamable_username")
streamable_password = os.environ.get("streamable_password")


_spaw = spaw.SPAW()
_spaw.auth(streamable_username, streamable_password)

def upload2streamable(videofile_name,remoteurl):
                        # upload video
    print(f"uploading video...")
    response = _spaw.videoUpload(videofile_name)
    print(response)
def upload2streamja():
# https://streamja.com/drj0q
# https://github.com/eXhumer/pyeXVHP/tree/d481aaad6ddd6d771ebb11c4491dc7a9f4ee2d9d
# https://github.com/eXhumer/pyeXMB/blob/python3/exmb/client.py