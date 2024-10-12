# Local LLM with Ollama and MATLAB

## Links and Resources

"Local LLM's with MATLAB" by Sivylla Paraskevopoulou
[local-llm-matlab-article](https://blogs.mathworks.com/deep-learning/2024/07/09/local-llms-with-matlab/?s_eid=psm_bl&source=15308)

[github repo llms matlab](https://github.com/matlab-deep-learning/llms-with-matlab/)

[ollama dwnload](https://ollama.com/download)

[llms matlab ollama doc](https://github.com/matlab-deep-learning/llms-with-matlab/blob/main/doc/Ollama.md)

## Set up Ollama Server

```bash
curl -fsSL https://ollama.com/install.sh | sh
```
## Pull Model into Server

```bash
ollama pull llama3
```

## Run chat
```bash
ollama run llama3
```
- Did this in terminal as well. Went fine. Can also pull llama2, codellama, phi3, mistral, gemma (probably others).

## Running in MATLAB
This part was rough. I had to clone the llms-with-matlab repo, then I had a bunch of issues. My GPU is AMD Radeon so ollama didn't like that. I had to mess with openCL and ROCm to make sure that was all working properly. Once working and my GPU was recognized and utilized, the following command starts the ollama server:
```bash
HSA_OVERRIDE_GFX_VERSION=10.3.0 ollama serve
```
This made it work very well. Following this, I pull the model:
```bash
ollama pull llama3
```

## Setting path in MATLAB
I had to set the path in matlab to make sure the repo commands and everything were available.
```matlab
addpath('/path/to/llms-with-matlab');
savepath;
```

## Running ollamaChat
After the above was settled, the chat worked well.
```matlab
chat = ollamaChat("llama3");
response = generate(chat, "Prompt goes here");
disp(response);
```

## The rest of doc is just learning for now

- For the following parts, I assume I do all of it in MATLAB. I'm running on Ubuntu and just using matlab -nodesktop so hopefully this goes well.


## Initialize Chat for RAG (Retrieval Augmented Generation)

Enhances results using own data. This example uses a blog post but can be modified I assume to use whatever data file works.

- Specify URL of a blogpost

```matlab
url = "https://<blog>.com/abc"
```

- Define local path, download post, save it

```matlab
localpath = "./data/";
if ~exist(localpath, 'dir')
    mkdir(localpath);
end

filename = "blog.html";
websave(localpath+filename,url);
```

- Read text from file with FileDatastore object

```matlab
fds = fileDatastore(localpath, "FileExtensions", ".html", "ReadFcn", @extractFileText);

str = [];
while hasdata(fds)
    textData = read(fds);
    str = [str; textData];
end
```

- Define a function for text processing

```matlab
function allDocs = preprocessDocuments(str)
    paragraphs = splitParagraphs(join(str));
    allDocs = tokenizedDocument(paragraphs);
end
```

- Split the text data into paragraphs
```matlab
document = preprocessDocuments(str);
```

## Retrieve Document

- Tokenize query and find similarity scores between query and document
```
embQuery = bm25Similarity(document, tokenizedDocument(query_tech));
```

- Sort docs in descending order of similarity scores
```
[~, idx] = sort(embQuery, "descend");
limitWords = 1000
selectedDocs = [];
totalWords = 0;
```

- Iterate over the sorted doc indices until word limit reached
```
i = 1;
while totalWords <= limitWords && i <= length(idx)
    totalWords = totalWords + size(document(idx(i)).tokenDetails,1);
    selectedDocs = [selectedDocs; joinWords(document(idx(i)))];
    i = i + 1;
end
```

## Generate response with RAG

- Define the prompt for the chatbot with added technical context, and generate response
```matlab
prompt_rag = "Context:" + join(selectedDocs, " ")...
    + newline +"Answer the following question: "+ query_tech;
response_rag = generate(chat, prompt_rag);
wrapText(response_rag)
```
    



















