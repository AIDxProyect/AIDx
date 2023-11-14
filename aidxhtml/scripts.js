document.addEventListener('DOMContentLoaded', function() {
    let featuresElement = document.querySelector('#features');
    let learnMoreBtn = document.querySelector('#learnMoreBtn');
    
    learnMoreBtn.addEventListener('click', function() {
        window.scrollTo({
            top: featuresElement.offsetTop,
            behavior: 'smooth'
        });
    });
});

// Inicializar AOS
AOS.init();



let backToTopBtn = document.getElementById('backToTop');

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
        backToTopBtn.style.display = "block";
    } else {
        backToTopBtn.style.display = "none";
    }
});

backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});


let navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    if (window.pageYOffset > navbar.offsetTop) {
        navbar.classList.add('sticky');
    } else {
        navbar.classList.remove('sticky');
    }
});
