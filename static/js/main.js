$(document).ready(function() {
  var navbar = $('.navbar');
  var isShrunk = false;
  var menuOpen = false;

  // Scroll function
  $(window).scroll(function() {
      if (!menuOpen) {
          if ($(document).scrollTop() > 50 && !isShrunk) {
              if ($(window).width() >= 1700) {
                  gsap.to(navbar, {
                      backgroundColor: "rgb(0 0 0 / 70%)",
                      height: 80, // Increase the height to 100px for width >= 2224px
                      duration: 0.3,
                      boxShadow: "0 2px 4px rgba(0, 0, 0, 0.2)",
                  });
              } else if ($(window).width() < 992) {
                  gsap.to(navbar, {
                      backgroundColor: "rgb(0 0 0 / 70%)",
                      height: 90, // Increase the height to 100px for width >= 2224px
                      duration: 0.3,
                      boxShadow: "0 2px 4px rgba(0, 0, 0, 0.2)",
                  });
              } else {
                  gsap.to(navbar, {
                      backgroundColor: "rgb(0 0 0 / 70%)",
                      height: 60,
                      duration: 0.3,
                      boxShadow: "0 2px 4px rgba(0, 0, 0, 0.2)",
                  });
              }

              isShrunk = true;
          } else if ($(document).scrollTop() <= 50 && isShrunk) {
              gsap.to(navbar, {
                  backgroundColor: "transparent",
                  height: "auto",
                  duration: 0.3,
                  boxShadow: "none",
              });

              isShrunk = false;
          }
      }
  });

  // Menu open function
  $('.navbar-toggler').click(function() {
      if (!navbar.hasClass('expanded')) {
          gsap.to(navbar, {
              backgroundColor: "rgb(0 0 0 / 70%)",
              height: "auto", // Allow navbar to expand to fit content
              duration: 0.3,
          });
          navbar.addClass('expanded');
          menuOpen = true; // Set menuOpen flag
      } else {
          gsap.to(navbar, {
              backgroundColor: "transparent",
              height: 60, // Revert back to original height when toggler is clicked again
              duration: 0.3,
          });
          navbar.removeClass('expanded');
          menuOpen = false; // Unset menuOpen flag
      }
  });
});




// navbar hover
var linkClicked = document.getElementsByClassName('nav-link');
var numClass = linkClicked.length;

for (var i = 0; i < numClass; i++) {
		linkClicked[i].addEventListener('click', function(){
      var onTheMoment = document.getElementsByClassName('active');
			onTheMoment[0].className = onTheMoment[0].className.replace(' active', '');
			this.className += ' active';
    }, false);
	}

  document.addEventListener("DOMContentLoaded", function () {
    var imgContainer = document.querySelector('.img-container');

    window.addEventListener('scroll', function () {
      var scrollAmount = window.scrollY;
      imgContainer.style.transform = 'translateY(' + (-scrollAmount / 2) + 'px)';
    });
  });



  

// owlCarousel


  

