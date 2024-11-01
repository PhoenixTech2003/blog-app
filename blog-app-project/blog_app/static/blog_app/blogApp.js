const navIcon = document.querySelector('.menuIcon');
const navigationMenu = document.querySelector('.menu')
const closeIcon = document.querySelector('#close')

const displayNavigation = function displaysNavigationMenuWhenIconIsClicked (){

    navigationMenu.classList.toggle('hidden')
}

const closeNavigation = function closesNavigationSidePanelWhenIconIsClicked (){
    navigationMenu.classList.toggle('hidden')
}


navIcon.addEventListener('click', displayNavigation)
closeIcon.addEventListener('click', closeNavigation)