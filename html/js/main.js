const form = document.getElementById("userForm");
const formBox = document.getElementById("formBox");
const outputBox = document.getElementById("outputBox");

const vornameOutput = document.getElementById("showVorname");
const nachnameOutput = document.getElementById("showNachname");
const emailOutput = document.getElementById("showEmail");

if (form && formBox && outputBox && vornameOutput && nachnameOutput && emailOutput) {
    window.addEventListener("load", function () {
        form.reset();
        formBox.style.display = "block";
        outputBox.style.display = "none";
    });

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const vornameInput = document.getElementById("vorname").value.trim();
        const nachnameInput = document.getElementById("nachname").value.trim();
        const emailInput = document.getElementById("email").value.trim();

        const vorname = vornameInput === "" ? "not given" : vornameInput;
        const nachname = nachnameInput === "" ? "not given" : nachnameInput;
        const email = emailInput === "" ? "not given" : emailInput;

        vornameOutput.textContent = vorname;
        nachnameOutput.textContent = nachname;
        emailOutput.textContent = email;

        formBox.style.display = "none";
        outputBox.style.display = "block";
    });
}
