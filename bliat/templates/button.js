/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
let visibleFac = false,
    visibleUniv = false;
function clickFaculty() {
    document.getElementById("dropdownFacContent").classList.toggle("show");
}

function clickUniversity() {
    document.getElementById("dropdownUnivContent").classList.toggle("show");
}


// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.buttonFac')) {
        let dropdowns = document.getElementsByClassName("dropdownFacContent");
        for (let i = 0; i < dropdowns.length; i++) {
            let openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
    if (!event.target.matches('.buttonUniv')) {
        dropdowns = document.getElementsByClassName("dropdownUnivContent");
        for (let i = 0; i < dropdowns.length; i++) {
            let openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}