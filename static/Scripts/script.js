
const transilations = {
  en:{

    //NAV
    // home:"Home",
    // detector:"Detector",
    // ecg:"Ecg",
    // stroke:"Stroke",
    // chd:"Chd",
    // analysis:"Analysis",
    // strokeAnalysis:"Stroke",
    // chdAnalysis:"Chd",
    // about:"About",
    // chatbot:"Chatbot",
    english:"English",
    arabic:"Arabic",

    // STROKE
    STtitle:"Stroke Questionaire",
    STtitle2:"Answer this Questions",
    strokeTitle:"What is your gender?",
    gender:"Gender",
    male:"Male",
    female:"Female",
    currentWork:"Which of the following best describes your current work status?",
    private:"Private",
    govtJob:"Govt_job",
    children:"Children",
    age:"What is your current age?",
    bloodPressure:"Have you been diagnosed with hypertension (high blood pressure)?",
    yse:"Yes",
    no:"No",
    status:"Have you ever been married?",
    heartDisease:"Do you have Heart disease",
    live:"Do you live in an urban or rural area?",
    urban:"Urban",
    rural:"Rural",
    glucoseLevel:"What is your most recent fasting blood glucose level (mg/dL)?",
    bodyMass:"What is your current Body Mass Index (BMI)?",
    smokeStatus:"Which of the following best describes your smoking status?",
    neverSmoke:"Never Smoked",
    smoke:"Smokes",
    formerlySmoke:"Formerly Smoked",

    // ECG
    ECGtitle:"Our Services",
    ECGtitle2:"Tell Us How Can Help?",
    ECGhead:"Part 1: Quick Questionaire",
    ckmb:"CK-MB",
    troponin:"Troponin",

    //CHD
    CHDtitle:"CHD Questionaire",
    CHDtitle2:"Answer this  Questions",
    cigsNum:"If you currently smoke, how many cigarettes do you smoke per day?",
    troponibloodPressuren:"TroponAre you currently taking any blood pressure medications?in",
    stroke:"Have you ever had a stroke?",
    hypertension:"Have you ever been diagnosed with hypertension (high blood pressure)?",
    diabetes:"Have you ever been diagnosed with diabetes?",
    cholesterolLevel:"What is your most recent total cholesterol level (mg/dL)?",
    topBloodPressure:"What is your most recent systolic blood pressure reading (the top number)?",
    bottomBloodPressure:"What is your most recent diastolic blood pressure reading (the bottom number)?",
    bmi:"What is your current body mass index (BMI)",
    restingHeartRate:"What is your resting heart rate (beats per minute)?",
    glucoseLevel:"What is your most recent fasting blood glucose level (mg/dL)?",

    //RESULT
    formCheck:"Check your Heart",
    result:"Your Result",

    // DOCTOR
    // meetDr:"Meet Our",
    // topDr:"Top Rated Doctors",
    // topicsDr:"Lorem ipsum dolor sit amet consectetur adipisicing elit.Quasi, voluptas exercitationem atque mollitia necessitatibussuscipit laudantium quia incidunt molestias dolorum! Quasiincidunt doloremque quisquam iusto?Dolore necessitatibus eligendi voluptates laudantium!",
    // drName:"Smokes",
    // drLoc:"Smokes",
    // drPrice:"Smokes",
    // drBook:"Book Appointment",

    // detector:"Detector",

  },
  ar:{
    // home:"الرئيسية",
    // detector:"الكشف",
    // ecg:"Ecg",
    // stroke:"Stroke",
    // chd:"Chd",
    // analysis:"تحاليل",
    // strokeAnalysis:"Stroke",
    // chdAnalysis:"Chd",
    // about:"عنا",
    // chatbot:"الدردشة",
    english:"انجليزي",
    arabic:"عربي",
    STtitle:"استبيان Stroke ",
    STtitle2:"املا هذه البيانات",
    gender:"ما هو نوعك",
    male:"ذكر",
    female:"أنثي",
    currentWork:" أي مما يلي يصف بشكل أفضل حالة عملك الحالية ؟",
    private:"خاص",
    govtJob:"وظائف حكومية",
    children:"أطفال",
    age:"ما هو عمرك الحالي",
    bloodPressure:"هل تم تشخيص إصابتك بارتفاع ضغط الدم (ارتفاع ضغط الدم)؟",
    yes:"نعم",
    no:"لا",
    status:"هل سبق لك الزواج؟",
    heartDisease:"هل تعاني من مرض القلب",
    live:"هل تعيش في منطقة حضرية أم ريفية؟",
    urban:"حضري",
    rural:"ريفي",
    glucoseLevel:"ما هو أحدث مستوى للجلوكوز في الدم أثناء الصيام (مجم/ديسيلتر)؟",
    bodyMass:"ما هو مؤشر كتلة جسمك الحالي (BMI)؟",
    smokeStatus:"أي مما يلي يصف حالة التدخين لديك بشكل أفضل؟",
    neverSmoke:"لم ادخن أبدا",
    smoke:"ادخن",
    formerlySmoke:"مدخن سابقا",
    formCheck:"ابدا الفحص",

    //ECG
    ECGtitle:"ترجم",
    ECGtitle2:"ترجم",
    ECGhead:"ترجم",
    ckmb:"ترجم",
    troponin:"ترجم",

     //CHD
     CHDtitle:"ترجم",
     CHDtitle2:"ترجم",
     cigsNum:"ترجم",
     troponibloodPressuren:"ترجم",
     stroke:"ترجم",
     hypertension:"ترجم",
     diabetes:"ترجم",
     cholesterolLevel:"ترجم",
     topBloodPressure:"ترجم",
     bottomBloodPressure:"ترجم",
     bmi:"ترجم",
     restingHeartRate:"ترجم",
     glucoseLevel:"ترجم",
 
    //RESULT
    result:"نتيجتك",

    //DOCTOR
    // meetDr:"تواصل مع",
    // topDr:"الاطباء الاعلي تقييما",
    // topicsDr:"Lorem ipsum dolor sit amet consectetur adipisicing elit.Quasi, voluptas exercitationem atque mollitia necessitatibussuscipit laudantium quia incidunt molestias dolorum! Quasiincidunt doloremque quisquam iusto?Dolore necessitatibus eligendi voluptates laudantium!",
    // drName:"Smokes",
    // drLoc:"Smokes",
    // drPrice:"Smokes",
    // drBook:"Book Appointment",
    // detector:"Detector",

  },
}

const langSelector = document.querySelector("select")

langSelector.addEventListener("change",(event)=>{
  setLanguage(event.target.value)
  // console.log(event.target.value)
  // localStorage.setItem("lang",event.target.value)
  // langSelector.options.removeAttribute("selected")
})
document.addEventListener('DOMContentLoaded',()=>{
  // setLanguage(localStorage.getItem("lang"))
  // langSelector.textContent=localStorage.getItem("lang")
})

const setLanguage = (language)=>{
  const elements = document.querySelectorAll('[data-lng]')
  // console.log(element)
  elements.forEach((element)=>{
    const transilationKey = element.getAttribute("data-lng")
    element.textContent = transilations[language][transilationKey]
  })

  // if(lang === 'ar'){
  //   document.getElementById('my-form').dir= 'rtl'
  //   document.getElementById("formBtn").style.marginRight='13rem'
  //   document.getElementById('Services-Sheader').dir= 'rtl'
  // }
  document.getElementById('Services-Sheader').dir = language === 'ar'? 'rtl': 'ltr';
  document.getElementById('my-form').dir = language === 'ar'? 'rtl': 'ltr'
  document.getElementById("formBtn").style.marginRight = language==='ar'?'13rem':'0'

}



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
  document.getElementById("Services-Sheader").scrollIntoView({ behavior: "smooth" });
});

// window.addEventListener("scroll", function() {
//   if (window.scrollY > 0) {
//     document.getElementById("Navebar").style.backgroundColor = "#f0f0f0"; /* Change background color on scroll */
//   } else {
//     document.getElementById("Navebar").style.backgroundColor = "transparent"; /* Reset background color on top */
//   }
// });



imageUpload.addEventListener("change", function(event) {
  const file = event.target.files[0]; // Get the selected image file

  // Validate file type (optional):
  if (!file.type.match("image.*")) {
    alert("Please select an image file.");
    return;
  }

  const reader = new FileReader();
  reader.onload = function(event) {
    previewImage.src = event.target.result; // Display the preview
  };
  reader.readAsDataURL(file); // Read the file as a data URL
});


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




