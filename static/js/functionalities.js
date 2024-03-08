document.addEventListener("DOMContentLoaded", function() {
    const tab1 = document.getElementById("content-1");
    const tab2 = document.getElementById("content-2");
    const content1 = document.getElementById("docket_forms");
    const content2 = document.getElementById("make_search");

    tab1.addEventListener("click", function() {
        content1.classList.remove("hidden");
        content2.classList.add("hidden");
    });

    tab2.addEventListener("click", function() {
        content1.classList.add("hidden");
        content2.classList.remove("hidden");
    });
});
