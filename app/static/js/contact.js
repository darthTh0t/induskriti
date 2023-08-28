'use strict'


// Flash message closes after 3 seconds
setTimeout(function() {
    document.getElementById('flash-message').style.display = 'none';
}, 3000);



// Infinite continuous vertical scrolling
// const testimonialList = document.getElementById('testimonial-list');
// const testimonials = document.querySelectorAll('#testimonial');

// let currentIndex = 0;
// const totalTestimonials = testimonials.length;

// function cloneAndAppendTestimonial() {
//     const currentTestimonial = testimonials[currentIndex];
//     const clonedTestimonial = currentTestimonial.cloneNode(true);
//     testimonialList.appendChild(clonedTestimonial);

//     currentIndex++;
//     if (currentIndex >= totalTestimonials) {
//         currentIndex = 0;
//     }
// }

// // Call the function to start the scrolling
// setInterval(cloneAndAppendTestimonial, 10000); // Adjust the interval as needed (in milliseconds)
