from TTS.api import TTS

# Init TTS with the target model name
tts = TTS(model_name="tts_models/en/ek1/tacotron2", progress_bar=False)
# Run TTS
tts.tts_to_file(text="The quick brown fox jumps over a lazy dog.")