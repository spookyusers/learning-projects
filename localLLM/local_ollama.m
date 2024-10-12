% Local LLM with Ollama 
% Kym Derriman
% 10/11/2024
% Guide: "Local LLMs with MATLAB" by Sivylla Paraskevopoulou

% ---------------------

% This begins assuming you've installed Ollama and pulled llama3

% Specify url of data (blogpost in this example)
url = "https://www.caltech.edu/about/news/gargantuan-black-hole-jets-are-biggest-seen-yet#:~:text=Astronomers%20have%20spotted%20the%20biggest,Way%20galaxies%20back%20to%20back."

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

%




