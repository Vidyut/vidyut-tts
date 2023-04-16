import streamlit as st
import time
from TTS.api import TTS

st.title("Vidyut's Coqui TTS Streamlit Frontend")
st.header('Text to speech generation')

# List available TTS models and choose the first one
model_types = ["Single Speaker Models", "Multi-Speaker Models", "YourTTS", "Coqui Studio Voices", "FreeVC"]
model_type = st.selectbox("Choose a model type",model_types)
if model_type == "Coqui Studio Voices":
    st.subheader('Coqui Studio Voices')

    voices = ["coqui_studio/en/Damien Black/coqui_studio","coqui_studio/en/Gitta Nikolina/coqui_studio","coqui_studio/en/Claribel Dervla/coqui_studio","coqui_studio/en/Ana Florence/coqui_studio","coqui_studio/en/Vjollca Johnnie/coqui_studio","coqui_studio/en/Viktor Menelaos/coqui_studio","coqui_studio/en/Baldur Sanjin/coqui_studio","coqui_studio/en/Zacharie Aimilios/coqui_studio","coqui_studio/en/Viktor Eka/coqui_studio","coqui_studio/en/Torcull Diarmuid/coqui_studio"]
    voice = st.selectbox('Choose a voice',voices)

    #import os
    #os.environ["COQUI_STUDIO_TOKEN"] = "Add your API here"
    from TTS.api import CS_API
    tts = CS_API()
    emotions = tts.emotions
        
    tts = TTS(model_name=voice, progress_bar=False, gpu=False)
    text = st.text_area('Enter text to convert to audio format!!')

    emo = st.selectbox('Choose an emotion',emotions)

    speed = st.slider('Speed', 0.1, 1.99, 1.0, 0.01)

    if st.button('Convert text to audio!'):
        # Run TTS
        tts.tts_to_file(text=text, emotion = emo, speed=speed, file_path="out.wav")
        st.success('Converted to audio successfully')

        audio_file = open('out.wav', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/wav')
        st.success("You can now play the audio by clicking on the play button!!")


if model_type == "Single Speaker Models":
    st.subheader("Single Speaker Models")
    models = ["tts_models/en/ljspeech/tacotron2-DDC", "tts_models/en/ljspeech/tacotron2-DDC_ph", "tts_models/en/ljspeech/glow-tts", "tts_models/en/ljspeech/speedy-speech", "tts_models/en/ljspeech/tacotron2-DCA", "tts_models/en/ljspeech/vits", "tts_models/en/ljspeech/vits--neon", "tts_models/en/ljspeech/fast_pitch", "tts_models/en/ljspeech/overflow", "tts_models/en/ljspeech/neural_hmm", "tts_models/en/sam/tacotron-DDC"]
    model = st.selectbox('Choose a model',models)
    tts = TTS(model_name=model, progress_bar=True, gpu=False)
    text = st.text_area('Enter text to convert to audio format!!')
    speed = st.slider('Speed', 0.1, 1.99, 1.0, 0.01)
    if st.button('Convert text to audio!'):
        # Run TTS
        tts.tts_to_file(text=text, speed=speed, file_path="out.wav")
        st.success('Converted to audio successfully')

        audio_file = open('out.wav', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/wav')
        st.success("You can now play the audio by clicking on the play button!!")


if model_type == "Multi-Speaker Models":
    st.subheader("Multi-Speaker Models")
    models = ["tts_models/en/vctk/vits", "tts_models/en/vctk/fast_pitch", "tts_models/en/blizzard2013/capacitron-t2-c50", "tts_models/en/blizzard2013/capacitron-t2-c150_v2"]
    model = st.selectbox('Choose a model',models)
    tts = TTS(model_name=model, progress_bar=False, gpu=False)
    text = st.text_area('Enter text to convert to audio format!!')
    speed = st.slider('Speed', 0.1, 1.99, 1.0, 0.01)
    speakers = tts.speakers
    speaker = st.selectbox('Choose a speaker',speakers)
    if st.button('Convert text to audio!'):
        # Run TTS
        tts.tts_to_file(text=text, speed=speed, speaker=speaker, file_path="out.wav")
        st.success('Converted to audio successfully')

        audio_file = open('out.wav', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/wav')
        st.success("You can now play the audio by clicking on the play button!!")


if model_type == "YourTTS":
    st.subheader("YourTTS")
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=False)
    text = st.text_area('Enter text to convert to audio format!!')
    speed = st.slider('Speed', 0.1, 1.99, 1.0, 0.01)
    speakers = tts.speakers
    speaker = st.selectbox('Choose a speaker',speakers)
    vc = st.checkbox('model cloning?')
    if vc:
        speaker_wav = st.file_uploader('Choose a .wav file for model cloning', 'wav')
        if st.button('Convert text to audio!'):
            # Run TTS
            tts.tts_to_file(text=text, speed=speed, speaker_wav=speaker_wav, language = "en", file_path="out.wav")
            st.success('Converted to audio successfully')

            audio_file = open('out.wav', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
            st.success("You can now play the audio by clicking on the play button!!")
    else:
        if st.button('Convert text to audio!'):
            # Run TTS
            tts.tts_to_file(text=text, speed=speed, speaker=speaker, language = "en", file_path="out.wav")
            st.success('Converted to audio successfully')

            audio_file = open('out.wav', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
            st.success("You can now play the audio by clicking on the play button!!")


if model_type == "FreeVC":
    st.subheader("FreeVC")
    st.subheading("I didn't really need FreeVC, so I haven't implemented it, but if enough people are interested, I'll figure it out. Do buy me a coffee to motivate me. Though I'll probably do it anyway when I get some time.")
