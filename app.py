from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Function to simulate flipping the coin
def flip_coin():
    return "heads" if random.random() < 0.5 else "tails"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flip', methods=['POST'])
def flip():
    # Get the number of flips from the user input
    num_flips = int(request.form.get('num_flips', 1))
    
    heads = 0
    tails = 0
    
    # Flip the coin and store the results for each flip
    results = []
    for _ in range(num_flips):
        result = flip_coin()
        if result == "heads":
            heads += 1
        else:
            tails += 1
        results.append(result)

    # Calculate percentages
    heads_percentage = (heads / num_flips) * 100
    tails_percentage = (tails / num_flips) * 100
    
    return jsonify({
        "results": results,
        "heads": heads,
        "tails": tails,
        "heads_percentage": heads_percentage,
        "tails_percentage": tails_percentage
    })

if __name__ == '__main__':
    app.run(debug=True)
