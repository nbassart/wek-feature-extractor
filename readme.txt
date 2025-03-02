You can download the feature extractor from the following GitHub repository:
wek-feature-extractor

Description

This feature extractor captures real-time audio from the microphone, analyzes the volume (amplitude), and sends this data to Wekinator via OSC (Open Sound Control). It can be used for various applications, such as:

Interactive sound-based machine learning projects

Music or performance-driven interactions

Real-time audio feature extraction for classification

Adaptive sound-driven interfaces

Dependencies and Installation

Before running the feature extractor, ensure you have the following dependencies installed:

Python 3.x

numpy

sounddevice

python-osc

To install these dependencies, run:

pip install numpy sounddevice python-osc

How to Run

Clone the repository or download the files:

git clone https://github.com/nbassart/wek-feature-extractor.git
cd wek-feature-extractor

Run the Python script:

python envia_volum.py

Open Wekinator and set it to receive inputs on port 6448 with the message /wek/inputs.

The program will continuously send the audio volume level to Wekinator in real time.

Notes

Ensure your microphone is properly configured and has the correct permissions.

You can modify the script to analyze other audio features such as pitch or frequency.

Press Ctrl+C to stop the program.

For any issues or suggestions, feel free to contribute or raise an issue on GitHub!

