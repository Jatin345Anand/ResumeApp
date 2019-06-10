window.addEventListener('load',init)
function init(){
    console.log('In Init');
    document.querySelector('#sa').addEventListener('click',doanim);
}
function doanim(){
    alert('In animation..');
    console.log('In Animation');
}