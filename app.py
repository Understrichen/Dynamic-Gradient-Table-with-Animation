from flask import Flask, jsonify, render_template  # Import necessary Flask modules

# Initialize the Flask application, specifying the folder where HTML templates are located
app = Flask(__name__, template_folder='templates')

# Your dataset — defined as a list of tuples in the desired order
data_list = [
    ("Twitch Chat", 100),
    ("Parkzer", 95),
    ("MugMug", 66),
    ("Pajama Sam", 54),
    ("Jokebot", 45),
    ("Michael Wave", 12),
    ("Chris Snack", 0),
    ("DougDoug", -59)
]

# Configuration defined in Python:
# - segments: an array of dictionaries, each with count, startColor, and endColor, Default is black
# - effect: a string defining the type of visual effect ("wave" or "waveFlow")
gradient_segments = [
    {"count": 4, "startColor": "#006400", "endColor": "#90EE90"},  # First color segment (dark to light green)
    {"count": 4, "startColor": "#e88f90", "endColor": "#f70104"}   # Second color segment (light to dark red)
]
chosen_effect = "waveFlow"  # Visual effect type, can be "wave" or "waveFlow"

# Route for the root URL, renders the main HTML page
@app.route("/")
def index():
    return render_template("index.html")  # Serve the index.html file from the templates folder

# Route that serves the data as JSON
@app.route("/data")
def data():
    # Convert list of tuples into a list of dictionaries with keys 'name' and 'score'
    rows = [{"name": n, "score": s} for n, s in data_list]
    # Return the data along with the segment configuration and chosen effect as a JSON response
    return jsonify({
        "rows": rows,
        "segments": gradient_segments,
        "effect": chosen_effect
    })

# If the script is run directly (not imported), start the Flask development server
if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode for easier development and troubleshooting
