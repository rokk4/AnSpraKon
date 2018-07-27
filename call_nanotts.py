import subprocess


def call_nanotts(nanotts_options, text="Ansprakon bereit."):
    """
Calls nanoTTS in an subprocess. nanoTTS parses text to pico.
-v de-DE flag sets the language to german.
Volume & Speed & Pitch control with flags is possible, see man nanoTTS
    :param nanotts_options:
    :param nanotts_flags:
    :param text: this is the String to speak
    """
    nanotts_flags = ["nanotts-git"] + nanotts_options + ['"' + text + '"']
    print(nanotts_flags)
    print(nanotts_options)
    try:
        subprocess.call(nanotts_flags, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        nanotts_error = "Error code {} while speaking, output: {}".format(e.returncode, e.output)
        print(nanotts_error)
        pass
