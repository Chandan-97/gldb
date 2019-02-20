window.onload = function(){
    $('.ui.dropdown').dropdown();
};

var backdrop = document.querySelector('.backdrop');
var modal = document.querySelector('.modal');
var selectPlanButton = document.querySelectorAll('#generate');
var modalNoButtons = document.querySelector(".modal__action--negative");

for(var i=0;i<selectPlanButton.length;i++){
    selectPlanButton[i].addEventListener('click',function(){
    });
};


backdrop.addEventListener('click',function(){
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




