from flask import Flask, render_template, request

app = Flask(__name__)

# ---------- LENGTH UNITS ----------
length_units = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.34
}

@app.route("/", methods=["GET", "POST"])
def length():
    result = None

    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from"]
        to_unit = request.form["to"]

        result = value * length_units[from_unit] / length_units[to_unit]

    return render_template("length.html", result=result)

# ---------- WEIGHT UNITS ----------
weight_units = {
    "mg": 0.001,
    "g": 1,
    "kg": 1000,
    "ounce": 28.3495,
    "pound": 453.592
}

@app.route("/weight", methods=["GET", "POST"])
def weight():
    result = None

    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from"]
        to_unit = request.form["to"]

        result = value * weight_units[from_unit] / weight_units[to_unit]

    return render_template("weight.html", result=result)

# ---------- TEMPERATURE ----------
@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    result = None

    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from"]
        to_unit = request.form["to"]

        # Convert to Celsius
        if from_unit == "C":
            temp_c = value
        elif from_unit == "F":
            temp_c = (value - 32) * 5/9
        else:  # Kelvin
            temp_c = value - 273.15

        # Convert from Celsius
        if to_unit == "C":
            result = temp_c
        elif to_unit == "F":
            result = (temp_c * 9/5) + 32
        else:
            result = temp_c + 273.15

    return render_template("temperature.html", result=result)

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)