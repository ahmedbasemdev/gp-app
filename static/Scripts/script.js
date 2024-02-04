






const imageUpload = document.getElementById("imageUpload");
const previewImage = document.getElementById("previewImage");
// document.getElementById("Navebar").classList.add("show");

//  ##### HOME PAGE #####

// animation navbar
let prevScrollPos = window.pageYOffset;

window.onscroll = function() {
  let currentScrollPos = window.pageYOffset;

  if (prevScrollPos > currentScrollPos) {
    // document.getElementById("Navebar").style.left = "0";
    document.getElementById("Navebar").style.paddingLeft = "6rem";
  } else {
    document.getElementById("Navebar").style.paddingLeft = "0rem";
    // document.getElementById("content").style. = "-100%";
  }

  prevScrollPos = currentScrollPos;
};

// // active Class 
// function setActive(index) {
//   // Remove 'active' class from all list items
//   var lis = document.querySelectorAll('#Navebar li');
//   // console.log(lis)
//   lis.forEach(function(li) {
//     li.classList.remove('active');
//   });

//   // Add 'active' class to the selected list item
//   lis[index].classList.add('active');
// }







document.getElementById("homeBtn").addEventListener("click", function() {
  document.getElementById("Services").scrollIntoView({ behavior: "smooth" });
});

// window.addEventListener("scroll", function() {
//   if (window.scrollY > 0) {
//     document.getElementById("Navebar").style.backgroundColor = "#f0f0f0"; /* Change background color on scroll */
//   } else {
//     document.getElementById("Navebar").style.backgroundColor = "transparent"; /* Reset background color on top */
//   }
// });



// imageUpload.addEventListener("change", function(event) {
//   const file = event.target.files[0]; // Get the selected image file

//   // Validate file type (optional):
//   if (!file.type.match("image.*")) {
//     alert("Please select an image file.");
//     return;
//   }

//   const reader = new FileReader();
//   reader.onload = function(event) {
//     previewImage.src = event.target.result; // Display the preview
//   };
//   reader.readAsDataURL(file); // Read the file as a data URL
// });


document.querySelector(".intro").classList.add("show");
// Add the 'image-show' class to the 'intro' element to trigger the image animation
setTimeout(() => {
  document.querySelector(".intro").classList.add("image-show");
}, 500); // Delay the image animation by 500 milliseconds

// window.addEventListener("scroll", function() {
//   var sections = document.querySelector(".intro");
//   for (var i = 0; i < sections.length; i++) {
//     var section = sections[i];
//     var sectionTop = section.offsetTop;
//     var sectionBottom = sectionTop + section.offsetHeight;
//     var viewportTop = window.pageYOffset;
//     var viewportBottom = viewportTop + window.innerHeight;

//     if (sectionBottom > viewportTop && sectionTop < viewportBottom) {
//       section.classList.add("active");
//     } else {
//       section.classList.remove("active");
//     }
//   }
// });
// window.addEventListener("scroll", function() {
//   var image = document.querySelector("#introImg");
//   var imageTop = image.offsetTop;
//   var imageBottom = imageTop + image.offsetHeight;
//   var viewportTop = window.pageYOffset;
//   var viewportBottom = viewportTop + window.innerHeight;

//   if (imageBottom > viewportTop && imageTop < viewportBottom) {
//     image.classList.add("animate-on-scroll");
//   } else {
//     image.classList.remove("animate-on-scroll");
//   }
// });
// window.addEventListener("scroll", function() {
//   var image = document.querySelector(".image-to-animate");
//   // var imageTop = image.offsetTop;
//   var imageBottom = imageTop + image.offsetHeight;
//   var viewportTop = window.pageYOffset;
//   var viewportBottom = viewportTop + window.innerHeight;

//   if (imageBottom > viewportTop && imageTop < viewportBottom) {
//     image.classList.add("animate-on-scroll");
//   } else {
//     image.classList.remove("animate-on-scroll");
//   }
// });

// window.onscroll = function() {scrollFunction()};

// function scrollFunction() {
//   if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
//     document.getElementById("Navebar").style.left = "0";
//   } else {
//     document.getElementById("Navebar").style.left = "-50px";
//   }
// }



