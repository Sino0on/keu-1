const burgerOpen = document.querySelector(".burger__open");
const burgerClose = document.querySelector(".burger__close");
const burgerItem = document.querySelectorAll(".burger__item.dropdown");

burgerOpen.addEventListener("click", () => {
  burgerOpen.classList.add("active");
});

burgerClose.addEventListener("click", () => {
  burgerOpen.classList.remove("active");
});

burgerItem.forEach((item) => {
  item.addEventListener("click", () => {
    item.querySelector(".burger__dropdown").classList.toggle("active");
    item.querySelector("img").classList.toggle("active");
  });
});

//const swiper = new Swiper(".swiper", {
//  pagination: {
//    el: ".swiper-pagination",
//    clickable: true,
//  },
//  breakpoints: {
//    841: {
//      slidesPerView: 3,
//      spaceBetween: 24,
//    },
//  },
//});

const featuresContent = document.querySelector(".features__content");

const featuresItems = [
  {
    id: 1,
    title: "ADMISSION AND FINANCIAL SUPPORT",
    img: "./assets/img/features-img-1.png",
  },
  {
    id: 2,
    title: "RESEARCH",
    img: "./assets/img/features-img-2.png",
  },
  {
    id: 3,
    title: "ACADEMIC PROGRAMS",
    img: "./assets/img/features-img-3.png",
  },
  {
    id: 4,
    title: "STUDENT LIFE",
    img: "./assets/img/features-img-4.png",
  },
  {
    id: 5,
    title: "VACANCIES",
    img: "./assets/img/features-img-5.png",
  },
  {
    id: 6,
    title: "OFFICES",
    img: "./assets/img/features-img-6.png",
  },
];

//featuresItems.forEach((item) => {
//  featuresContent.innerHTML += `
//  <div class="features__item item">
//    <div class="item__top">
//        <img src="${item.img}" alt="features-img">
//        <h2 class="item__title">${item.title}</h2>
//    </div>
//    <div class="item__bottom">
//        <button>
//            About
//        </button>
//    </div>
//  </div>
//  `;
//});

//const newsContent = document.querySelector(".swiper-wrapper");
//
//const newsItems = [
//  {
//    id: 1,
//    title: `Student scientific conference on "Problems of science: a student's view".`,
//    img: "./assets/img/news-img-1.png",
//  },
//  {
//    id: 2,
//    title: `Student scientific conference on "Problems of science: a student's view".`,
//    img: "./assets/img/news-img-2.png",
//  },
//  {
//    id: 3,
//    title: `Student scientific conference on "Problems of science: a student's view".`,
//    img: "./assets/img/news-img-3.png",
//  },
//];

//newsItems.forEach((item) => {
//  newsContent.innerHTML += `
//    <div class="swiper-slide">
//        <div class="news__item item">
//            <div class="item__top">
//                <img src="${item.img}" alt="news-img">
//            </div>
//            <div class="item__bottom">
//                <p>
//                ${item.title}
//                </p>
//                <i>
//                    <a href="#">Read More</a>
//                </i>
//            </div>
//        </div>
//    </div>
//  `;
//});

const partnersContent = document.querySelector(".partners__content");

const partnersItems = [
  "./assets/img/partners-img-1.png",
  "./assets/img/partners-img-2.png",
  "./assets/img/partners-img-3.png",
  "./assets/img/partners-img-4.png",
  "./assets/img/partners-img-5.png",
]

//partnersItems.forEach((item) => {
//  partnersContent.innerHTML += `
//  <div class="partners__item">
//    <img src="${item}" alt="">
//  </div>
//  `;
//});
