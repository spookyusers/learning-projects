# Creating a local LLM following a guide 

## Links and Resources

"Local LLM's with MATLAB" by Sivylla Paraskevopoulou
[https://blogs.mathworks.com/deep-learning/2024/07/09/local-llms-with-matlab/?s_eid=psm_bl&source=15308](local-llm-matlab article)

[https://github.com/matlab-deep-learning/llms-with-matlab/](github repo llms with matlab)

[https://ollama.com/download](Ollama download)

[https://github.com/matlab-deep-learning/llms-with-matlab/blob/main/doc/Ollama.md](
llms with matlab - ollama doc)

## Set up Ollama Server

```matlab
curl -fsSL https://ollama.com/install.sh | sh
```

## Pull Model into Server

```matlab
ollama pull llama3
```
Can also pull llama2, codellama, phi3, mistral, gemma (probably others).

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
    



















