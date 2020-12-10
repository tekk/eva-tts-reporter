import sys
import json
from google.cloud import texttospeech
from pyowm.owm import OWM
from pyowm.utils import timestamps, formatting
from pyowm.utils.config import get_default_config
from pygments import highlight
#from pygments.lexers import JsonLexer
#from pygments.formatters import TerminalFormatter
from pygments.lexers.data import JsonLexer 
from pygments.formatters.terminal import TerminalFormatter

config_dict = get_default_config()
config_dict['language'] = 'sk'
owm = OWM('6e4952810a883e9fb0238c0666a0bb1d', config_dict)
reg = owm.city_id_registry()
list_of_locations = reg.locations_for('Banská Bystrica', country='SK')
bb = list_of_locations[0]
lat = bb.lat
lon = bb.lon
mgr = owm.weather_manager()
onecall = mgr.one_call(lat, lon)
weather = onecall.forecast_daily[0]

json_str = json.dumps(weather.__dict__, indent=4, sort_keys=True)
print(highlight(json_str, JsonLexer(), TerminalFormatter()))

raise SystemExit

one_call.forecast_daily[0].temperature('celsius').get('feels_like_morn', None) #Ex.: 7.7


client = texttospeech.TextToSpeechClient()
input_text = texttospeech.SynthesisInput(text="Ahoj, tu je Eva.")

# Note: the voice can also be specified by name.
# Names of voices can be retrieved with client.list_voices().
voice = texttospeech.VoiceSelectionParams(
    language_code="sk-SK", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    request={"input": input_text, "voice": voice, "audio_config": audio_config}
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
