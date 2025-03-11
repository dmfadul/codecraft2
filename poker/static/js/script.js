document.addEventListener("DOMContentLoaded", function () {
    const grid = document.getElementById("card-grid");
    const positionDropdown = document.getElementById("position");
    const saveButton = document.getElementById("saveButton");

    const suits = ["s", "o"];
    const ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"];

    // Generate card grid
    function createGrid() {
        grid.innerHTML = "";
        for (let i = 0; i < ranks.length; i++) {
            for (let j = 0; j < ranks.length; j++) {
                if (i <= j) { // Ensures unique hand combinations
                    let hand = `${ranks[i]}${ranks[j]}${i === j ? "" : suits[i > j ? 1 : 0]}`;
                    let card = document.createElement("div");
                    card.classList.add("card");
                    card.textContent = hand;
                    card.dataset.hand = hand;
                    card.dataset.status = "none"; // "raise", "limp", or "none"
                    grid.appendChild(card);
                }
            }
        }
    }

    createGrid();

    // Handle card clicks
    grid.addEventListener("click", function (event) {
        if (event.target.classList.contains("card")) {
            let card = event.target;
            let status = card.dataset.status;

            if (status === "none") {
                card.classList.add("raise");
                card.dataset.status = "raise";
            } else if (status === "raise") {
                card.classList.remove("raise");
                card.classList.add("limp");
                card.dataset.status = "limp";
            } else {
                card.classList.remove("limp");
                card.dataset.status = "none";
            }
        }
    });

    // Save ranges to backend
    saveButton.addEventListener("click", function () {
        let position = positionDropdown.value;
        let selectedRanges = [];

        document.querySelectorAll(".card").forEach(card => {
            if (card.dataset.status !== "none") {
                selectedRanges.push({
                    hand: card.dataset.hand,
                    action: card.dataset.status
                });
            }
        });

        fetch("/save_ranges/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken()
            },
            body: JSON.stringify({ position, ranges: selectedRanges })
        })
        .then(response => response.json())
        .then(data => alert(data.message))
        .catch(error => console.error("Error:", error));
    });

    // Function to get CSRF token from Django
    function getCSRFToken() {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            document.cookie.split(";").forEach(cookie => {
                let [name, value] = cookie.trim().split("=");
                if (name === "csrftoken") cookieValue = decodeURIComponent(value);
            });
        }
        return cookieValue;
    }
});
