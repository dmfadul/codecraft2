document.addEventListener("DOMContentLoaded", function () {
    const grid = document.querySelector("#grid-container table");
    const positionSelect = document.getElementById("position-select");

    grid.addEventListener("click", function (event) {
        if (event.target.classList.contains("hand-cell")) {
            toggleAction(event.target);
        }
    });

    function toggleAction(cell) {
        if (cell.classList.contains("raise")) {
            cell.classList.remove("raise");
            cell.classList.add("limp");
        } else if (cell.classList.contains("limp")) {
            cell.classList.remove("limp");
        } else {
            cell.classList.add("raise");
        }
        saveSelection(cell.dataset.hand, getAction(cell));
    }

    function getAction(cell) {
        if (cell.classList.contains("raise")) return "raise";
        if (cell.classList.contains("limp")) return "limp";
        return null;
    }

    function saveSelection(hand, action) {
        const positionId = positionSelect.value;
        if (!positionId) return alert("Please select a position first.");

        fetch("/save_range/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken(),
            },
            body: JSON.stringify({
                position_id: positionId,
                hand: hand,
                action: action
            })
        });
    }

    function getCSRFToken() {
        return document.cookie.split("; ")
            .find(row => row.startsWith("csrftoken="))
            ?.split("=")[1];
    }
});
