# NetHyTech-TTS

NetHyTech-TTS is a Python package for text-to-speech (TTS) conversion using Selenium WebDriver.

## Installation

You can install NetHyTech-TTS using pip:

```bash
pip install NetHyTech-TTS
```

## Usage

```python
from NetHyTech_TTS import speak

# Speak the text
speak("Hello, world!")
```

This will open a headless Chrome browser and navigate to the TTS website (https://tts.5e7en.me/), input the text "Hello, world!", and play the generated audio.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver (automatically managed by WebDriverManager)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository]().

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
