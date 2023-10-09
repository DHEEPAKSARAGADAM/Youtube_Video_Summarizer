#Problem Statement
We spend a considerable amount of time on YouTube. Which is a primary source of knowledge because it contains lecture videos from primer institutes. We watch a hour long video and try to grab the important ideas from it. What if we can let a system do it. Understand the important ideas from the video and summarize it in a way which will allow you to look back and revisit the key ideas without watching the video all over again

# Youtube_Video_Summarizer
This project uses Advanced NLP techniques to extract the summary of the video. Its always difficult to run these codes for a common user. What if we have a GUI which allows us to just paste in the link of the YouTube video and the application does all the hard lifting for us and saves the summary in the text format as pdf filex

#Process
Extract the closed caption in English from the user given YouTube link
If there is no caption for video then it uses speech recognition model to text conversion
Clean the Data by removing all the time stamps and make it a single document
Run the NLP text summarization algorithm on the given document
Develop a GUI to link the process
Finally save this summary or insight as Pdf
