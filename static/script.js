// JavaScript for AI Disease Prediction System

document.addEventListener('DOMContentLoaded', function() {
    // Form submission handling
    const symptomForm = document.getElementById('symptomForm');
    const predictBtn = document.getElementById('predictBtn');
    const loading = document.getElementById('loading');
    
    if (symptomForm) {
        symptomForm.addEventListener('submit', function(e) {
            // Show loading animation
            if (predictBtn) predictBtn.style.display = 'none';
            if (loading) loading.classList.remove('hidden');
        });
    }
    
    // Smooth scrolling for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Add hover effects to cards
    const cards = document.querySelectorAll('.card-hover');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Checkbox interaction feedback
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const label = this.nextElementSibling;
            if (this.checked) {
                label.style.fontWeight = 'bold';
                label.style.color = '#2563eb';
            } else {
                label.style.fontWeight = 'normal';
                label.style.color = '#374151';
            }
        });
    });
});