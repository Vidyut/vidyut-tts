# vidyut-tts
Streamlit frontend for Coqui-tts
I love coqui-tts and how it works fuss free even without a gpu. Less lovable is typing out endless commands to generate an audiobook - which is what I'm considering, for the sci-fi book, Marginally Human. with 120k words in the book... it seemed to tedious. Not at all happy with the default server we get, so I wrote this up with Streamlit.

There are just two files as of now and I don't expect that to change. You can duplicate the repository or just grab the app.py and install the dependencies yourself - it's just TTS and streamlit:

`pip install TTS streamlit`

If you want to use Coqui Studio Voice, you'll need to get an api key from your account page https://app.coqui.ai/account (scroll down) and insert the key online 18 of the app.py file and uncomment both line 17 and 18. It is better to set it as an environmental variable. This is just provided in case you don't know how to do that.

Then run

`streamlit run app.py`

And that should be all you need to do to get started.

Disclaimer:

I did this to save me effort and shared it in case anyone else had the same problem, but I'm not really a coder, just a champion copy-paste-improviser. I can't guarantee this will work for everyone, but if it does, this is such an easy tool. I've made a video to show how simple it is to use. I'm generating the voice over for the video itself as I demonstrate. Edited a touch for brevity and generated some voices for parts without audio, but other than that, it is pretty much how it looks.

Lastly, there are many features not implemented. This is just English for now (though no reason why it shouldn't work with other models - I just didn't have time to test, or interest since I was using only English. I could add other features. FreeVC isn't yet implemented. I don't need it, and I don't know if this code will be useful to anyone else, so didn't seem to be a point investing the effort. I can add if needed.

Totally lastly, I'm a single mom with a disabled child, so life is expensive and usually broke and going out to work isn't an option. If you find this useful, do consider buying me a coffee and it will motivate me to spend time furthering this rather than other food-on-table stuff not related to coding or sci-fi writing.
