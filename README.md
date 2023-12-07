# StorytellerAI with GPT4 and TTS

After a debate about AI in literature this idea jumped to my head and I just did it for fun.

## Installation

Install the requirements.

```bash
pip install -r requirements.txt
```

## Examples

Check stories in `story_docs` look for `story_after_critique_3.md`. its the final written version.

Check audio in `story_audio`.

## Project Structure

In the src file we have 5 modules.

`main.py`: the main endpoint of our project and the sailer.  
`storyteller.py`: here the main logic of the idea, there is two classes `WriterGPT` and `CritiqueGPT` which make the initial idea.  
`config.py`: the main configs for our project e.g. `API_KEY`.  
`utils.py`: utility functions like `text_to_speech`.  
`schemas.py`: currently is empty but TODO: implement pydantic schemas for writing.

## Contributing

Feel free to contact with me and let's build this fun project, fork and pr.
