document.addEventListener('DOMContentLoaded', function() {
  // Mobile nav toggle
  var toggle = document.getElementById('cafe-nav-toggle');
  var links = document.getElementById('cafe-nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function() {
      var isOpen = links.classList.contains('open');
      links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', !isOpen);
    });
    // Close on link click
    links.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        links.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // Intersection Observer for fade-in animations
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.cafe-card, .cafe-product-card, .cafe-process-card, .cafe-culture-card, .cafe-stat').forEach(function(el) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px)';
      el.style.transition = 'opacity .5s ease, transform .5s ease';
      observer.observe(el);
    });
  }

  // Process step animation on scroll (proceso page)
  var processCards = document.querySelectorAll('.cafe-process-card');
  if (processCards.length > 0 && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var processObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateX(0)';
          processObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.2 });

    processCards.forEach(function(card, index) {
      card.style.opacity = '0';
      card.style.transform = 'translateX(-20px)';
      card.style.transition = 'opacity .4s ease ' + (index * 0.1) + 's, transform .4s ease ' + (index * 0.1) + 's';
      processObserver.observe(card);
    });
  }

  // Timeline animation
  var timelineItems = document.querySelectorAll('.cafe-timeline-item');
  if (timelineItems.length > 0 && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var timelineObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          timelineObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.3 });

    timelineItems.forEach(function(item, index) {
      item.style.opacity = '0';
      item.style.transform = 'translateY(15px)';
      item.style.transition = 'opacity .4s ease ' + (index * 0.15) + 's, transform .4s ease ' + (index * 0.15) + 's';
      timelineObserver.observe(item);
    });
  }
});
