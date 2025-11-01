# LBPH Face Recognition – “Every AI is not ML”

by [Benax Technologies](https://github.com/benax-rw)  
_with gratitude to the guidance and contribution of Benax Technologies._

---

## Overview

This project demonstrates a classical **computer vision** pipeline using the **Local Binary Patterns Histograms (LBPH)** algorithm for facial recognition.  
It emphasizes that **Artificial Intelligence (AI)** extends beyond machine learning, by relying on handcrafted visual descriptors rather than deep neural networks.

---

## Project Objective

The goal of this project is to implement a fully functional facial recognition system built entirely on traditional computer vision principles.  
The pipeline performs face detection, feature extraction, and identity recognition based on local texture patterns.  
It showcases how reliable recognition can be achieved using **LBPH** without data-hungry machine learning models.

---

## Pipeline Workflow

1. **Dataset Creation**

   - Captures and stores multiple face images for each individual.
   - Ensures consistent lighting, angle, and framing during acquisition.

2. **Dataset Review**

   - Involves visual inspection of captured samples.
   - Retains only clear, properly framed, and well-lit images to enhance recognition accuracy.

3. **Model Training**

   - Utilizes the LBPH algorithm to encode local binary patterns from approved images.
   - Generates a trained recognition model and a label mapping file.

4. **Face Recognition**
   - Performs real-time or single-image predictions using the trained model.
   - Displays identified names and confidence metrics directly on video frames.

---

## Technical Highlights

- **Algorithm**: Local Binary Patterns Histograms (LBPH)
- **Detection**: Haar Cascade Classifier for frontal face detection
- **Recognition**: Texture-based matching of encoded histograms
- **Language**: Python 3
- **Libraries**: OpenCV (Contrib), NumPy, Pillow
- **Runtime Options**:
  - Webcam-based real-time recognition
  - Single-image recognition mode

---

## Installation and Environment Setup

A Python virtual environment is required to isolate dependencies.  
All required packages are listed in the `requirements.txt` file.  
Once installed, the environment enables running dataset creation, training, and prediction modules seamlessly.

---

## Dataset Management

Images are stored under a designated dataset directory, organized by unique subject identifiers.  
Each dataset undergoes a manual review phase to remove blurred, incomplete, or misaligned samples.  
This ensures the model learns from consistent and representative visual data.

---

## Model Artifacts

The training process produces the following key artifacts:

- **Trained Model File** – Stores the learned LBPH descriptors (`.yml` format).
- **Cascade Classifier File** – Used for real-time face detection (`.xml` format).
- **Label Map File** – Maps numeric identifiers to human-readable names (`.json` format).

---

## Usage Guidelines

- Launch the recognition pipeline after completing dataset collection and training.
- Use consistent camera placement and lighting conditions to maintain recognition quality.
- Adjust the threshold and confidence parameters based on testing results for optimal accuracy.

---

## Contribution and Acknowledgment

This work was developed under mentorship and technical direction from **Benax Technologies**, whose expertise in computer vision and AI ethics has guided the conceptual and practical aspects of this project.

Special thanks to **Benax Technologies** for contributing educational support, design insight, and technical collaboration.

---

## Key Insight

> “Every AI is not ML.”  
> Classical methods like LBPH remind us that intelligence can arise from well-designed logic — not only from data-driven learning.

---

## License

This project is released for educational and research purposes.  
Refer to the repository’s license file for specific usage permissions.

---
