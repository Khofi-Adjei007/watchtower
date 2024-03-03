// Select all link divs inside the button_class
var linkDivs = document.querySelectorAll("#button_class div");

// Select all form elements with IDs starting with "docket_forms"
var formElements = document.querySelectorAll('[id^="docket_forms"]');
var formElements = document.querySelectorAll('[id^="make_search"]');
var formElements = document.querySelectorAll('[id^="calls_tracking"]');
var formElements = document.querySelectorAll('[id^="another_docket"]');



// Add click event listeners to each link div
linkDivs.forEach(function(linkDiv) {
    linkDiv.addEventListener("click", function() {
        // Remove the 'active' class from all link divs
        linkDivs.forEach(function(div) {
            div.classList.remove("active");
        });
        // Add the 'active' class to the clicked link div
        this.classList.add("active");
        
        // Get the ID of the clicked link div
        var clickedId = this.id;
        
        // Loop through all form elements
        formElements.forEach(function(form) {
            // Hide all form elements
            form.style.display = "none";
            // If the form ID matches the clicked link div ID, display it
            if (form.id === "docket_forms_" + clickedId) {
                form.style.display = "block";
            }
        });
    });
});
