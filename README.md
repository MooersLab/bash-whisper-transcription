![Version](https://img.shields.io/static/v1?label=bash-whisper-transcription&message=0.2&color=brightcolor)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


# bash-whisper-transcription: Bash function to ease the transcription of audio files to text with OpenAI's whisper

## Introduction
I need to transcribe audio 1-2 times a day automatically.
I could reuse previously issued commands, but the bash function below makes this redundant task easier.
This bash function reduces the effort required to apply OpenAI's whisper to the transcription of audio files.
Files of the following types are supported: mp3, mp4, mpeg, mpga, m4a, wav, and webm.

I store this function in a `.bashFunctions` file in my home directory.
I source this file from my `.zshrc` file.
The function is loaded whenever I open a new terminal session.
I enter `wh311 <audiofile>` in the directory with the audio file and wait 1 minute per 6 minutes of audio recording.

The output is a plain text file.
You will have to post-process the transcribed text because spoken punctuation marks 
and new paragraph commands are not recognized. 

You may have to install several software packages (e.g., openai-whisper, Rust, ffpmeg, torch).
You can use pip to install openai-whisper.

```bash
wh311()
{
echo "Run whisper using Python3.11 on a <audiofile> to transcribe it into text."
echo "Works with file types:  mp3, mp4, mpeg, mpga, m4a, wav, and webm."
echo "The base model works with CPUs. Requires 1 minute per 6 minutes of audio."
echo "You may need to reset the path to the Python interperter that you want to use."
if [ $# -lt 1 ]; then
  echo 1>&2 "$0: not enough arguments"
  echo "Supply the mp3 file stem."
  echo "Usage: wh311 230113_1649.mp3"
  return 2
elif [ $# -gt 1 ]; then
  echo 1>&2 "$0: too many arguments"
  echo "Supply the mp3 file stem."
  echo "Usage: wh311 230113_1649.mp3"
fi
/opt/local/bin/python3.11 -c "import whisper;model = whisper.load_model('base');result = model.transcribe('$1');print(result['text'])" > $1.txt
}
```

## Installation
1. Copy the code above or download the bashFunctions file.
2. Customize the path for the Python interpreter you want to use.
3. Source the bashFunctions file in a terminal.
4. Enter `wh311 <audiofile>` at the prompt in the terminal. You have to be in the directory with the audio file or provide the path to the audio file.
5. Wait 1 minute per 6 minutes of audio recording. Faster transcriptions are possible with a Nvidia GPU.

## Optional audio notification when finished
A audio message indicating that that transcription has finished would be helpful here because the transcription is such a slow process.
Unfortunatley, the the code for generating a audio message varies between operating system and revise on external software.
See this [stack overflow post](https://stackoverflow.com/questions/16573051/sound-alarm-when-code-finishes) for numerous options: 

For macOS, add the following to the command on the second to last line in the script file:

```bash
&& say 'Your audio transcription has finished.'
```
Now, that is really convenient!!

## Optional removal of the audio recording and opening of transcript

If you have no future need for the audio, you might as well remove it after that transcription is finished.
Below is an example command.

```bash
wh311 230114_0846.mp3 && rm -rf 230114_0846.mp3
```

You might as well open the transcript with a text editor (textmate is this case) while you are at it.

```bash
wh311 230114_0846.mp3 && rm -rf 230114_0846.mp3 && mate 230114_0846.mp3.txt &
```

   
## Testing
Tested in a zsh shell in a iTerm2 terminal on a 2018 MacBookPro running macOS 13.6 and Python3.11 from macports. 
Should work with Python 3.8 to 3.11. Edit the second to last line in the function accordingly.

