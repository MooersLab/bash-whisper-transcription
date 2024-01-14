# bash-whisper-transcription: Bash function to ease the transcription of audio files to text with OpenAI's whisper

## Introduction
I need to automatically transcribe audio 1-2 times a day.
I could reuse previously issued commands but the bash 
function below makes this redundant task a little easier.

This bash function reduces effort required to apply OpenAI's whisper to the transcription of audio files.

I store this function a `.bashFunctions` file in my home directory.
I source this file from my `.zshrc` file.
The function is loaded whenever I open a new terminal session.
I enter `wh311 <audiofile>` in the directory with the audio file and wait 1 minute per 6 minutes of audio recording.

The output is directed to a plain text file.
You will have to postprocess the transcribed text because spoken punctuation marks 
and new paragraph commands are not recognized. 

Note that you may have to several software packages (e.g., openai-whisper, Rust, ffpmeg).
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
  echo "Usage: wh311 230113_1649.map3"
fi
/opt/local/bin/python3.11 -c "import whisper;model = whisper.load_model('base');result = model.transcribe('$1');print(result['text'])" > $1.txt
}
```
