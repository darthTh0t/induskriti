'use strict'


// Flash message closes after 3 seconds
setTimeout(function() {
    document.getElementById('flash-message').style.display = 'none';
}, 3000);



// submit button actions

const submitBtn = document.querySelector('.submit-btn')
submitBtn.addEventListener('click', (e) => {
    e.preventDefault()
})
