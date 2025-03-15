
let li=document.querySelector('li');

var a=document.querySelectorAll('a');

a.forEach(e => {

    e.addEventListener('click', function(){

        a.querySelector('.nav-link active').classList.remove('nav-link active');
        e.classList.add('nav-link active');

    });

});
