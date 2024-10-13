#---
# MATLAB Chatbot from Shell
#
# This script will start the Ollama server with HSA Override 
# and pull llama3 from Ollama, then start matlab and run the 
# matlab chatbot script.

# HSA Override to ensure that ollama serve uses AMD GPU and
# sends it to background.
HSA_OVERRIDE_GFX_VERSION=10.3.0 ollama serve &

# Pull llama3 model
ollama pull llama3

# Navigate to directory with matlabchatbot script
cd /home/kym/learning-projects/localLLM/matlab-llm

# Launch MATLAB and run matlabchatbot script
gnome-terminal -- bash -c "matlab -nodesktop -nosplash -r 'matlabchatbot'; exec bash"


