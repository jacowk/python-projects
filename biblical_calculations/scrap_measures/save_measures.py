import requests

playFile = open("measures.htm", "wb")
res = requests.get("https://biblehub.com/weights-and-measures/")
try:
    res.raise_for_status()  # Always do this
    print(type(res))
    if res.status_code == requests.codes.ok:
        print("status ok")
    print(len(res.text))
    print(res.text[:250])

    for chunk in res.iter_content(100000):
        playFile.write(chunk)
except Exception as exc:
    print("There was a problem: %s" % (exc))
finally:
    playFile.close()