const searchBtn = document.querySelector('.search-btn');
const results = document.querySelector('.rem')
const body = document.querySelector('.body')
const theme = document.querySelector('.theme')
const searchboxTheme = document.querySelector('.searchTheme')
const searchbox = document.querySelector('.search_box')
const themeBtn = document.querySelector('.fa-circle-half-stroke')
searchBtn.addEventListener('click',function(){
results.classList.remove('hidden')
})

themeBtn.addEventListener('click',function(){
body.classList.add('theme')
searchbox.classList.add('searchTheme')
alert('To get back into white theme click Esc button on your keyboard...')
document.addEventListener('keydown', function(a){
    if (a.key=='Escape') {

        body.classList.remove('theme')
searchbox.classList.remove('searchTheme')
    }
})
})