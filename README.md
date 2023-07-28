# Speech-Recognition-For-Inventory-Check

This simple Python program utilizes speech recognition to determine whether a given item is present in the inventory list. The program records audio input from the user, processes it using Google's speech recognition service, and then checks if the recognized item is in the predefined list of fruits.

## Prerequisites

Before running the program, make sure you have the required libraries installed. You can install them using pip:

```bash
pip install SpeechRecognition
```

## How to Use

1. Run the script and allow microphone access.

2. **Customization:**

   - **Inventory List:** You can customize the inventory list to include your own items. Modify the `fruits` list in the script to add, remove, or update the items you want to recognize. For example:
   
     ```python
     fruits = ['apple', 'orange', 'banana', 'mango', 'grapes']
     ```
   
   - **Recognition Language:** By default, the program uses Google's speech recognition service. You can change the recognition language or switch to another service by modifying the `recognize_google` function call. Check the [SpeechRecognition documentation](https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#speech-recognition-library-reference) for more information.
   
3. Wait for a second to let the program adjust the energy threshold based on the surrounding noise level.

4. Speak the name of the fruit you want to check.

5. The program will process your speech and indicate whether the fruit is present in the inventory list or not.

## Inventory List

The program uses the following inventory list of fruits:

- apple
- orange
- kiwi
- mango
- grapes
- apricots
- lychee
- blueberries
- raspberries
- strawberries

## Contribution

We welcome contributions to enhance the functionality or add new features to this program. If you have any ideas, bug fixes, or improvements, feel free to open a pull request. Your contributions will be appreciated and will make this project more useful to others.

Let's make speech recognition better together! 🎉

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify this program as per your needs.
