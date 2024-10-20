#!/bin/bash
# This script starts the Ollama server, pulls the model, and launches MATLAB

# Kill any previous instance of Ollama
echo "Terminating existing Ollama processes..."
pkill -f ollama

# Start Ollama server with AMD GPU override
echo "Starting Ollama server with AMD GPU settings..."
HSA_OVERRIDE_GFX_VERSION=10.3.0 ollama serve &
#ollama serve &


# Wait a few seconds to make sure the server starts properly
sleep 5

# Pull the Llama3 model (if it's not already pulled)
echo "Pulling Llama3 model..."
ollama pull llama3

# Navigate to directory containing matlabchatbot.m script
echo "Navigating to the directory containing matlabchatbot.m script..."
cd /home/kym/learning-projects/llms-with-matlab

# Set up MATLAB to run the chatbot
echo "Launching MATLAB..."
gnome-terminal -- bash -c "matlab -nodesktop -nosplash -r 'matlabchatbot'; exec bash"


