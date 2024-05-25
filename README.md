![Version](https://img.shields.io/static/v1?label=bash-whisper-transcription&message=0.6.3&color=brightcolor)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


# Bash and Python functions to improve the transcription of audio files to text with OpenAI's whisper

## Introduction
I transcribe audio files generated during my daily commutes using a Digital Voice Recorder (DVR).
DVRs work better than cell phones for capturing human speech at a distance.

I could reuse previously issued commands in a terminal, but the bash function below makes this redundant task easier.
This bash function reduces the effort required to apply OpenAI's whisper to the transcription of audio files.
I use the recommended base model with my CPUs.
The word error rate (WER) is low.
The following file types are supported. 

- mp3 
- mp4 
- mpeg
- mpga
- m4a
- wav
- webm

## Features

- Run whisper using Python3.11 on an audio file to transcribe it into text.
- Works with file types:  mp3, mp4, mpeg, mpga, m4a, wav, and webm.
- The base model works with CPUs. Requires 1 minute per 6 minutes of audio.
- You may need to reset the path to the Python interpreter you want to use.
- Uses gawk to return one sentence per line to ease deleting whisper's hallucination rubbish text.
- Uses sed to remove leading whitespace on each line.
- Uses TextMate to open the processed transcript.
- Uses the terminal app 'say' on Mac OS to announce when the transcribe is ready for you.


## Installation and use

I store this function in a `.bashFunctions` file in my home directory.
I source this file from my `.zshrc` file.
The function is loaded whenever I open a new terminal session.
I enter `wh3 <audiofile filename>` in the directory with the audio file and wait 1 minute per 6 minutes of audio recording.

The output is a plain text file.
You will have to post-process the transcribed text because the text is returned in one big block.
I often only reuse snippets of text and then delete the transcript.

You may have to install several software packages (e.g., openai-whisper, Rust, ffpmeg, torch).
You can use pip to install `openai-whisper`.
It works in my hands with Python3.9 and Python3.11.
I use the latter.

```bash
wh3()
{
echo "Run whisper using Python3.11 on a <audiofile> to transcribe it into text."
echo "Works with file types:  mp3, mp4, mpeg, mpga, m4a, wav, and webm."
echo "The base model works with CPUs. Requires 1 minute per 6 minutes of audio."
echo "You may need to reset the path to the Python interpreter you want to use."
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

1. Copy the code above when displayed in the RAW form or download the bashFunctions file.
2. Customize the path for the Python interpreter you want to use.
3. Source the bashFunctions file in a terminal.
4. Enter `wh3 audiofile filename>` at the terminal prompt. You must be in the directory with the audio file or provide the path to the audio file.
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

If you no longer need the audio file, you might as well remove it after the transcription.
Below is an example command.

```bash
wh3 230114_0846.mp3 && rm -rf 230114_0846.mp3
```

When the transcription is finished, you can automatically open the transcript with a text editor (TextMate, in this case).

```bash
wh3 230114_0846.mp3 && rm -rf 230114_0846.mp3 && mate 230114_0846.mp3.txt &
```

## Optional text replacements

The processing of the transcript opens up the opportunity to make text replacements.
The script `replacem.py` is a master script.
It calls additional Python modules, which contain lists of text replacements.

The most important file is the contractions.py file because it automatically replaces all English contractions, which are unacceptable in formal nonfiction writing.
People 100 years from now will probably not be familiar with them, so what is the point in using something that will confuse future readers?

The other Python files support using voice commands to insert code or expand acronyms.
The simplest example would be the voice command "new paragraph" to insert two newline characters to start a paragraph in the block format.
This command is very helpful for breaking up your transcript into logical units.
Whisper cannot do this on its own.

## Optional write one sentence per line

This script variant rewrites the transcript with one sentence per line using GNU awk (a.k.a gawk).
Most transcribed sentences end with a period, so the gawk substitution is adequate at least 99% of the time.
The one sentence per line format greatly facilitates deleting unwanted lines using the Control-k keyboard shortcut for the cut line command in most text editors.
This variant also removes the *.mp3 and the initial text files after applying text replacements would *replacem.py*.

```bash
/opt/local/bin/python3.11 -c "import whisper;model = whisper.load_model('base');result = model.transcribe('$1');print(result['text'])" > $1.txt && ./replacem.py $1.txt && rm $1.txt && gawk '{gsub(/\./,"." ORS)} 1' $1.txtcorrected.txt > $1-clean.txt && mate $1.txtcorrected.txt && $1.mp3 && say 'Your audio transcription has finished.'
```

## Troubleshooting

If you use homebrew as a package manager and if an upgrade to homebrew leaves you with the error message 
`Library Not Loaded - libmbedcrypto.14.dylib` when you run `wh3`, then run the following commands in the order listed:


```python
brew uninstall scrcpy
brew uninstall --ignore-dependencies ffmpeg
brew uninstall --ignore-dependencies librist
brew uninstall --ignore-dependencies mbedtls
brew install scrcpy
```
   
## Testing
I tested it in a zsh shell in an iTerm2 terminal on a 2018 MacBookPro running macOS 13.6 and Python3.11 from Macports. 
Should work with Python 3.8 to 3.11. 
Edit the path to the Python interpreter in the second to last line in the function as needed.

## Update history

|Version      | Changes                                                                                                                                    | Date                 |
|:-----------:|:------------------------------------------------------------------------------------------------------------------------------------------|:--------------------:|
| Version 0.6.2 |  Added update table and minor edits for improved clarity in README.md                                                                    | 2024 May 14          |
| Version 0.6.3 |  Minor edits for improved clarity in README.md                                                                                           | 2024 May 18          |

## Sources of funding

- NIH: R01 CA242845
- NIH: R01 AI088011
- NIH: P30 CA225520 (PI: R. Mannel)
- NIH P20GM103640 and P30GM145423 (PI: A. West)
