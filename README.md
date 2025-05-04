# Heads or Tails Coin Flip App

A simple web-based coin flip simulator that allows users to flip a virtual coin a specified number of times. It shows the results of each flip and provides a percentage breakdown of heads vs. tails at the end of the session. The app also plays a sound on each flip for a more interactive experience.

## Features

- Flip a virtual coin any number of times
- View results for each individual flip (Heads or Tails)
- See the percentage breakdown of heads and tails at the end
- Play a sound effect on each flip
- Simple and responsive design
- Built using HTML, CSS, JavaScript, and Python (Flask)

## Installation

To use the app locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/heads-or-tails-coin-flip.git
    ```

2. **Navigate to the project folder**:
    ```bash
    cd heads-or-tails-coin-flip
    ```

3. **Create a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

6. **Run the Flask server**:
    ```bash
    python app.py
    ```

7. **Open the app in your browser**:
    - Navigate to `http://127.0.0.1:5000/` in your browser to view the app.

## Usage

1. **Set the number of flips**: 
    - Enter a number in the input field to specify how many times you want the coin to flip.
    
2. **Flip the coin**: 
    - Click the **Flip the Coin** button or press the **Space Bar** to start the flipping process.
    
3. **View results**:
    - The coin will flip, and the result of each flip (Heads or Tails) will be shown.
    - The sound will play with each flip.
    - At the end of the flips, the app will calculate the percentage of heads and tails and display the results.

## How it Works

The app works with a combination of frontend (HTML, CSS, JavaScript) and backend (Python with Flask):

1. **Frontend**: The user interface allows the user to input the number of flips, start the flipping process, and view results in real-time. The coin flipping animation is handled using CSS.
   
2. **Backend**: The Python server (Flask) handles the logic for flipping the coin and returning the results. The number of flips is passed to the server via an API request, which is then processed and the results are sent back to the frontend.

3. **Coin Flip Logic**: 
    - The Python server generates a random result (Heads or Tails) each time the coin is flipped.
    - The results are updated and returned for display on the frontend.

4. **Sound Effect**: The sound effect for each flip is played using an HTML `<audio>` element.

## Technologies Used

- **HTML**: For the structure of the page.
- **CSS**: For styling the page and animations (CSS 3D transformations for the coin flip effect).
- **JavaScript**: For the logic of the coin flip and to handle user interactions.
- **Python (Flask)**: For the backend logic of handling coin flips and providing results.
- **Bootstrap 5**: For the responsive layout and easy styling of the buttons and other elements.

## Flask Backend Setup

The backend of the app is built using [Flask](https://flask.palletsprojects.com/), a micro web framework for Python. Here's how the backend works:

1. The app listens for requests from the frontend when the coin flips need to be processed.
2. It generates a random result (Heads or Tails) based on a random number.
3. It returns the results in JSON format, which is then displayed on the frontend.
4. The Flask app runs on `http://127.0.0.1:5000/` by default.

### Backend Setup Instructions:

1. **Install Flask**:
    ```bash
    pip install Flask
    ```

2. **Run the Flask server**:
    ```bash
    python app.py
    ```

3. The server should now be running at `http://127.0.0.1:5000/`.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributing

If you'd like to contribute to the project, feel free to fork the repository and create a pull request. You can suggest improvements, fix bugs, or even add new features!

### Steps for contributing:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add a new feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Open a pull request.

## Acknowledgments

- Thanks to [Pixabay](https://pixabay.com/) for the coin flip sound used in the app.
- [Bootstrap 5](https://getbootstrap.com/) for the responsive design.
- [MDN Web Docs](https://developer.mozilla.org/en-US/) for the extensive resources on HTML, CSS, and JavaScript.

---

Let me know if you need any further adjustments or additional details!
