from google.cloud import texttospeech
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'sk'
owm = OWM('6e4952810a883e9fb0238c0666a0bb1d', config_dict)
reg = owm.city_id_registry()
list_of_locations = reg.locations_for('Banská Bystrica', country='SK')
moscow = list_of_locations[0]
lat = moscow.lat
lon = moscow.lon
mgr = owm.weather_manager()
daily_forecast = mgr.one_call(lat, lon)
tomorrow = timestamps.tomorrow()                                   # datetime object for tomorrow
weather = daily_forecaster.get_weather_at(tomorrow)                # the weather you're looking for

print(weather)

sys.exit(0)

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
