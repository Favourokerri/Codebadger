
function openNav(){
    const nav = document.getElementById('side-nav');
    nav.style.left='0px';
    console.log(nav);
}

function closeNav(){
    const nav = document.getElementById('side-nav');
    nav.style.left= '-500px';
}

document.addEventListener('DOMContentLoaded', function() {
    const dropdown = document.querySelectorAll('.dropdown');
    dropdown.forEach(function(dropdown) {
        dropdown.addEventListener('click', function(){
            const dropdownContent = this.querySelector('.dropdown-content');
            if (dropdownContent.style.display === "none" || dropdownContent.style.display === "") {
                dropdownContent.style.display = "block";
            } else {
                dropdownContent.style.display = "none";
            }
        });
    });

});