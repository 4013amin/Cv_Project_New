const navOpenBtn= document.querySelector('.nav-icon');
const menuNav =document.querySelector('.menuNav');
const overlay = document.querySelector('.overlay');
const closeNav = document.querySelector('.close-nav');

// Search Btn Blogs
const searchBtn = document.querySelector('.searchBtn')
const searchInput = document.querySelector('.searchInput')

// Tab BTN
const showContent = document.querySelectorAll('.showContent');
const allContent = document.querySelectorAll('.Content');



showContent.forEach((tab,index) =>{
    tab.addEventListener('click', (e)=>{
        e.preventDefault();
        showContent.forEach(t=> {t.classList.remove('bg-BlueC-300')});
        tab.classList.add('bg-BlueC-300')

        allContent.forEach(cont=> {cont.classList.add('hidden')});
        allContent[index].classList.remove('hidden');
    })
})


// Mobile Menu
function closeNavMenu(){
    menuNav.classList.remove('right-0');
    menuNav.classList.add('-right-64');
    overlay.classList.add('hidden');
}

navOpenBtn.addEventListener("click" ,function () { 
    console.log('sjdkfhjdsfdf')
    menuNav.classList.add('right-0');
    menuNav.classList.remove('-right-64');
    overlay.classList.remove('hidden');
    overlay.addEventListener('click',closeNavMenu);
 });


closeNav.addEventListener('click',closeNavMenu);


// Search Blog Btn
searchBtn.addEventListener('click', function() {
    searchInput.classList.toggle('w-0')
});

