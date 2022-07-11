let menuBurger = document.querySelector(".header__menu");
let navList = document.querySelector(".navigate__list");
let closeMenu = document.querySelector(".header__close");


menuBurger.addEventListener("click",function(){
    navList.style.setProperty('display', 'flex');
    menuBurger.style.setProperty('display', 'none');
    closeMenu.style.setProperty('display', 'block');

})

closeMenu.addEventListener("click",function(){
    navList.style.setProperty('display', 'none');
    closeMenu.style.setProperty('display', 'none');
    menuBurger.style.setProperty('display', 'block');

})