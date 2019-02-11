window.onload = function(){
    $('.ui.dropdown').dropdown();
};

// console.log("Hello, World")

var backdrop = document.querySelector('.backdrop');
var modal = document.querySelector('.modal');
var selectPlanButton = document.querySelectorAll('#generate');
var modalNoButtons = document.querySelector(".modal__action--negative");
// var mobileNav = document.querySelector(".mobile-nav");

// console.dir(toggleButton);

for(var i=0;i<selectPlanButton.length;i++){
    selectPlanButton[i].addEventListener('click',function(){
        // modal.style.display = "block";
        // backdrop.style.display = "block";

        modal.classList.add('open');
        backdrop.classList.add('open');
        checkboxes.style.display = "none";
    });
};


backdrop.addEventListener('click',function(){
    // mobileNav.style.display = "none";
    this.classList.remove('open');
    closeModal();
});

if(modalNoButtons){
    modalNoButtons.addEventListener('click', closeModal);
}


function closeModal() {
    backdrop.classList.remove('open');
    if(modal){
        modal.classList.remove('open');
    }
};

var state_list = ["Bihar", "Delhi", "Rajasthan", "Kerala", "Goa", "Gujrat"];

function chooseState(){
    $('.ui.longer.modal').modal('show');
}




