// add hovered class to selected list item
let list = document.querySelectorAll(".navigation li");

function activeLink() {
  list.forEach((item) => {
    item.classList.remove("hovered");
  });
  this.classList.add("hovered");
}

list.forEach((item) => item.addEventListener("mouseover", activeLink));

// Menu Toggle
let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");
let cardwelcome = document.querySelector(".cardwelcome");

toggle.onclick = function () {
  navigation.classList.toggle("active");
  main.classList.toggle("active");
};



// login admin
const forms= document.querySelector(".login-admin"), 
  pwShowHide = document.querySelectorAll(".eye-icon");

pwShowHide.forEach(eyeicon => {
  eyeicon.addEventListener("click", () => {
    let pwFields = eyeicon.parentElement.parentElement.querySelectorAll(".password");
    
    pwFields.forEach (password => {
      if(password.type === "password"){ 
        password.type = "text";
        eyeicon.classList.replace("bxs-hide", "bxs-show");
        return;
      }
      password.type = "text";
        eyeicon.classList.replace("bxs-show", "bxs-hide");
    })

  })
})

$(document).ready(function() {
  $('.dropdown-toggle').click(function() {
    $(this).next('.dropdown-menu').toggle();
  });
});


//=============== GOOGLE TRANSLATE ========

function googleTranslateElementInit() {
  new google.translate.TranslateElement({
      pageLanguage: 'en',
      includedLanguages: 'id,en',
      layout: google.translate.TranslateElement.InlineLayout.SIMPLE
  }, 'google_translate_element');
}

function translateText() {
  var paragraphs = document.getElementsByClassName('paragraf-deskripsi');
  var translationService = new google.translate.TranslateService();

  for (var i = 0; i < paragraphs.length; i++) {
    var originalText = paragraphs[i].innerHTML;
    translationService.translate(originalText, 'id', function (translation) {
      paragraphs[i].innerHTML = translation;
    });
  }
}


var deskripsiElement = document.querySelector('.deskripsi-konten');
var tombolSuara = document.getElementById('btn-suara');

function putarSuara(teks) {
    responsiveVoice.speak(teks, 'Indonesian Female', {locale: 'id-ID'});
}

tombolSuara.addEventListener('click', function() {
    var teksDeskripsi = deskripsiElement.textContent;
    putarSuara(teksDeskripsi);
});
