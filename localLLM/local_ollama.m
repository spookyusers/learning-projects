% Local LLM with Ollama 
% Kym Derriman
% 10/11/2024
% Guide: "Local LLMs with MATLAB" by Sivylla Paraskevopoulou

% ---------------------

% This begins assuming you've installed Ollama and pulled llama3

% Specify url of data (blogpost in this example)
url = "https://www.caltech.edu/about/news/gargantuan-black-hole-jets-are-biggest-seen-yet#:~:text=Astronomers%20have%20spotted%20the%20biggest,Way%20galaxies%20back%20to%20back."

% Define the technical query (this was not in blog instructions)
query_tech = "black hole jets";

% Define local path, download from url, save
localpath = "./data/";
if ~exist(localpath, 'dir')
    mkdir(localpath);
end

filename = "blog.html";
websave(localpath+filename,url);

% Read text from file with FileDatastore object
fds = fileDatastore(localpath, "FileExtensions", ".html", "ReadFcn", @extractFileText);

str = [];
while hasdata(fds)
    textData = read(fds);
    str = [str; textData];
end

% Define function text processing
function allDocs = preprocessDocuments(str)
    paragraphs = splitParagraphs(join(str));
    allDocs = tokenizedDocument(paragraphs);
end

% Split text data into paragraphs
document = preprocessDocuments(str);

% Tokenize query and find similarity scores between query and doc
embQuery = bm25Similarity(document, tokenizedDocument(query_tech));

% Sort docs descending order of similarity scores
[~, idx] = sort(embQuery, "descend");

limitWords = 1000
selectedDocs = [];
totalWords = 0;

% Iterate over sorted doc indices until word limit reached
i = 1;
while totalWords <= limitWords && i <= length(idx)
    totalWords = totalWords + size(document(idx(i)).tokenDetails,1);
    selectedDocs = [selectedDocs; joinWords(document(idx(i)))];
    i = i + 1;
end

% Define prompt with added context and generate response
prompt_rag = "Context:" + join(selectedDocs, " ")...
    + newline +"Answer the following question: "+ query_tech;
response_rag = generate(chat, prompt_rag);
wrapText(response_rag)






