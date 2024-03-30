![Version](https://img.shields.io/static/v1?label=bash-whisper-transcription&message=0.4&color=brightcolor)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


# bash-whisper-transcription: Bash function to ease the transcription of audio files to text with OpenAI's whisper

## Introduction
I transcribe audio files that I have generated during my daily commutes using a Digital Voice Recorder (DVR).
DVRs work better than cell phones for capturing human speech at a distance.

I could reuse previously issued commands in a terminal, but the bash function below makes this redundant task easier.
This bash function reduces the effort required to apply OpenAI's whisper to the transcription of audio files.
I use the recommended base model with my CPUs.
The word error rate (WER) is low.
The following file types are supported: mp3, mp4, mpeg, mpga, m4a, wav, and webm.

I store this function in a `.bashFunctions` file in my home directory.
I source this file from my `.zshrc` file.
The function is loaded whenever I open a new terminal session.
I enter `wh3 <audiofile filename>` in the directory with the audio file and wait 1 minute per 6 minutes of audio recording.

The output is a plain text file.
You will have to post-process the transcribed text because the text is returned in one big block.
I often only reuse snippets of text and then delete the transcript.

You may have to install several software packages (e.g., openai-whisper, Rust, ffpmeg, torch).
You can use pip to install `openai-whisper`.
It works with Python3.9 and Python3.11.
I use the latter.

```bash
wh3()
{
echo "Run whisper using Python3.11 on a <audiofile> to transcribe it into text."
echo "Works with file types:  mp3, mp4, mpeg, mpga, m4a, wav, and webm."
echo "The base model works with CPUs. Requires 1 minute per 6 minutes of audio."
echo "You may need to reset the path to the Python interpreter that you want to use."
if [ $# -lt 1 ]; then
  echo 1>&2 "$0: not enough arguments"
  echo "Supply the mp3 file stem."
  echo "Usage: wh3 230113_1649.mp3"
  return 2
elif [ $# -gt 1 ]; then
  echo 1>&2 "$0: too many arguments"
  echo "Supply the mp3 file stem."
  echo "Usage: wh3 230113_1649.mp3"
fi
/opt/local/bin/python3.11 -c "import whisper;model = whisper.load_model('base');result = model.transcribe('$1');print(result['text'])" > $1.txt
}
```

## Installation and Usage
1. Copy the code above when displayed in the RAW form or download the bashFunctions file.
2. Customize the path for the Python interpreter you want to use.
3. Source the bashFunctions file in a terminal.
4. Enter wh3 audiofile filename> at the terminal prompt. You must be in the directory with the audio file or provide the path to the audio file.
5. Wait 1 minute per 6 minutes of audio recording. Faster transcriptions are possible with a Nvidia GPU.

## Optional audio notification when finished
An audio message indicating that transcription has finished is helpful here because the transcription is a slow process.
Unfortunately, the code for generating an audio message varies between operating systems and relies on external software.
See this [stack overflow post](https://stackoverflow.com/questions/16573051/sound-alarm-when-code-finishes) for numerous options: 

For macOS, add the following to the command on the second to last line in the script file:

```bash
&& say 'Your audio transcription has finished.'
```
Now, that is convenient!!

## Optional removal of the audio recording and opening of transcript

If you will no longer need the audio file, you might as well remove it after the transcription is finished.
Below is an example command.

```bash
wh3 230114_0846.mp3 && rm -rf 230114_0846.mp3
```

You can automatically open the transcript with a text editor (textmate is this case) when the transcription is finished.

```bash
wh3 230114_0846.mp3 && rm -rf 230114_0846.mp3 && mate 230114_0846.mp3.txt &
```

## Trouble shooting

If you use home brew as a package manager and if an upgrade to home brew leaves you with the error message 
`Library Not Loaded - libmbedcrypto.14.dylib` when you run `wh3`, then run the following commands in the order that is listed:


```python
brew uninstall scrcpy
brew uninstall --ignore-dependencies ffmpeg
brew uninstall --ignore-dependencies librist
brew uninstall --ignore-dependencies mbedtls
brew install scrcpy
```
   
## Testing
I tested it in a zsh shell in an iTerm2 terminal on a 2018 MacBookPro running macOS 13.6 and Python3.11 from macports. 
Should work with Python 3.8 to 3.11. 
Edit the path to the Python interpreter in the second to last line in the function as needed.

