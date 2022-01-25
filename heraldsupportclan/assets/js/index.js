let toggleNavStatus = false;

let toggleNav = function() {
    let getSidebar = document.querySelector(".menu-btn");
    let getSidebarUl = document.querySelector(".menu-btn ul");
    let getSidebarLinks = document.querySelectorAll(".menu-btn a");

    if (toggleNavStatus === false) {
        getSidebarUl.style.visibility = "visible";
        getSidebar.style.width = "272px";


        let arrayLength = getSidebarLinks.length;
        for(let i = 0; i < arrayLength; i++) {
            getSidebarLinks[i].style.opacity = "1";
        }

        toggleNavStatus = true;
    }

    else if (toggleNavStatus === true) {
        getSidebar.style.width = "50px";
    

        let arrayLength = getSidebarLinks.length;
        for(let i = 0; i < arrayLength; i++) {
            getSidebarLinks[i].style.opacity = "0";
        }

        getSidebarUl.style.visibility = "hidden";

        toggleNavStatus = false;
    }

}