// Selecting tab buttons
var tabButtons = document.querySelectorAll("#button_class a");

// Selecting tab content forms
var tabForms = document.querySelectorAll(".form-container form");

// Function to show the selected form and hide others
function showForm(formId) {
    tabForms.forEach(function(form) {
        if (form.getAttribute("id") === formId) {
            form.classList.remove("hidden");
        } else {
            form.classList.add("hidden");
        }
    });
}

// Adding click event listener to each tab button
tabButtons.forEach(function(tabButton) {
    tabButton.addEventListener("click", function(event) {
        event.preventDefault(); // Prevent default link behavior

        // Remove active class from all tab buttons
        tabButtons.forEach(function(btn) {
            btn.classList.remove("active");
        });

        // Add active class to the clicked tab button
        tabButton.classList.add("active");

        // Get the form ID associated with the clicked tab button
        var formId = tabButton.getAttribute("href").substr(1);

        // Show the corresponding form
        showForm(formId);
    });
});

// Initially show the first tab content
showForm(tabButtons[0].getAttribute("href").substr(1));
