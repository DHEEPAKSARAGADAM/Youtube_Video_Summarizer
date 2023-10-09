from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.tokenizer import tokenize_and_preprocess
from app.summarizer import download_video, transcribe_audio, summarize_text

app = FastAPI()

class VideoURL(BaseModel):
    url: str

class KeywordInput(BaseModel):
    keywords: list[str]

@app.post("/summarize/")
async def summarize(video_url: VideoURL, keywords: KeywordInput = None):
    try:
        download_video(video_url.url)
        transcribed_text = transcribe_audio('video.mp4')

        # Tokenize and preprocess the transcribed text
        preprocessed_text = " ".join(tokenize_and_preprocess(transcribed_text))

        # Summarize the preprocessed text
        if keywords:
            summary = summarize_text(preprocessed_text, keywords.keywords)
        else:
            summary = summarize_text(preprocessed_text)

        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
