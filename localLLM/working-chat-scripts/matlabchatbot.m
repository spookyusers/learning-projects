% -------------------------
% Simple Chatbot for MATLAB
% -------------------------


% When run, interactive chat starts. To leave the chat, type "end" or press Ctrl+C.

%This example includes three steps:
% - Define model parameters, such as the maximum word count, and a stop word.
% - Create an ollamaChat object and set up a meta prompt.
% - Set up the chat loop.

% --------------------
% Setup Model and Chat
% --------------------

% Set the maximum allowable number of words per chat session and define the keyword that, when entered by the user, ends the chat session.
wordLimit = 2000;
stopWord = "bye";
fprintf("AI: Hello, how can I help?\nWhen you're done, just type 'bye'.\n"); 

% Create an instance of ollamaChat to perform the chat and messageHistory to store the conversation history.
chat = ollamaChat("llama3");
messages = messageHistory;

% Chat loop
% Start the chat and keep it going until it sees the word in stopWord.
totalWords = 0;
messagesSizes = [];

% The main loop continues indefinitely until you input the stop word or press Ctrl+C.
while true
    query = input("User: ", "s");
    query = string(query);
    %dispWrapped("User", query)     uncomment if using outside terminal

% If the you input the stop word, display a farewell message and exit the loop.
    if query == stopWord
        disp("AI: Closing the chat. Have a great day!")
        break;
    end

    numWordsQuery = countNumWords(query);
% If the query exceeds the word limit, display an error message and halt execution.
    if numWordsQuery>wordLimit
        error("Your query should have fewer than " + wordLimit + " words. You query had " + numWordsQuery + " words.")
    end

% Keep track of the size of each message and the total number of words used so far.
    messagesSizes = [messagesSizes; numWordsQuery]; %#ok
    totalWords = totalWords + numWordsQuery;

% If the total word count exceeds the limit, remove messages from the start of the session until it no longer does.
    while totalWords > wordLimit
        totalWords = totalWords - messagesSizes(1);
        messages = removeMessage(messages, 1);
        messagesSizes(1) = [];
    end

% Add the new message to the session and generate a new response.
    messages = addUserMessage(messages, query);
    [text, response] = generate(chat, messages);
    
    dispWrapped("AI", text)

% Count the number of words in the response and update the total word count.
    numWordsResponse = countNumWords(text);
    messagesSizes = [messagesSizes; numWordsResponse]; %#ok
    totalWords = totalWords + numWordsResponse;

% Add the response to the session.
    messages = addResponseMessage(messages, response);
end

% ----------------
% Helper Functions
% ----------------

% Function to count the number of words in a text string
function numWords = countNumWords(text)
    numWords = doclength(tokenizedDocument(text));
end

% Function to display wrapped text, with hanging indentation from a prefix
function dispWrapped(prefix, text)
    indent = [newline, repmat(' ',1,strlength(prefix)+2)];
    text = strtrim(text);
    disp(prefix + ": " + join(textwrap(text, 70),indent))
end
