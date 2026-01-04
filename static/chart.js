let chart;

function predict() {
    const data = {
        P_RADIUS: parseFloat(document.getElementById("P_RADIUS").value),
        P_MASS: parseFloat(document.getElementById("P_MASS").value),
        P_DENSITY: parseFloat(document.getElementById("P_DENSITY").value),
        P_SURFACE_TEMP: parseFloat(document.getElementById("P_SURFACE_TEMP").value),
        P_PERIOD: parseFloat(document.getElementById("P_PERIOD").value),
        P_DISTANCE: parseFloat(document.getElementById("P_DISTANCE").value),
        S_TYPE: parseFloat(document.getElementById("S_TYPE").value),
        S_LUMINOSITY: parseFloat(document.getElementById("S_LUMINOSITY").value),
        S_TEMPERATURE: parseFloat(document.getElementById("S_TEMPERATURE").value),
        S_METALLICITY: parseFloat(document.getElementById("S_METALLICITY").value)
    };

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "x-api-key": "habitability_api_2026"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(res => {
        document.getElementById("result").classList.remove("d-none");
        document.getElementById("result").innerHTML =
            `<b>Prediction:</b> ${res.prediction}<br>
             <b>Habitability Score:</b> ${res.habitability_score}<br>
             <b>Rank:</b> ${res.rank}`;

        drawChart(data);
    });
}

function drawChart(data) {
    const ctx = document.getElementById("featureChart").getContext("2d");

    if (chart) chart.destroy();

    chart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: Object.keys(data),
            datasets: [{
                label: "Feature Values",
                data: Object.values(data)
            }]
        }
    });
}
