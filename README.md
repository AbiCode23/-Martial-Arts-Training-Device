# Martial Arts Training Device

## Description

The Martial Arts Training Device is a personalized training assistant designed to help martial artists improve their skills through guided tracking and analysis. The project leverages a modular approach to focus on key aspects like pushups, squats, and repetition-based exercises, providing a comprehensive and user-friendly experience.

## Features

- Tracks and analyzes repetitions for exercises like pushups and squats.
- Offers a web-based interface for visualization and interaction.
- Modular design for easy extension and customization.

## Technologies Used

- Python
- Flask
- HTML/CSS for the web interface

## Getting Started

### Prerequisites

- Python 3.x installed on your system
- Flask (Install via `pip install flask`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/martial-arts-training-device.git
   ```
2. Navigate to the project directory:
   ```bash
   cd martial-arts-training-device
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the main application script:
   ```bash
   python app.py
   ```
2. Open your web browser and visit:
   ```
   http://127.0.0.1:5000
   ```

## File Structure

- `app.py`: Main application script.
- `Pushups.py`: Handles logic for pushup exercises.
- `Reps.py`: Manages repetition tracking.
- `Squats.py`: Tracks and analyzes squats.
- `templates/index.html`: The web interface for user interaction.

## Future Enhancements

- Integration with more martial arts-specific drills and exercises.
- Progress tracking with detailed analytics.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## License

This project is licensed under the [MIT License](LICENSE).
