
 var slides=document.querySelector('.slider-items').children;
 var nextSlide=document.querySelector(".right-slide");
var prevSlide=document.querySelector(".left-slide");
var totalSlides=slides.length;
var index=0;

nextSlide.onclick=function () {
     next("next");
}
prevSlide.onclick=function () {
     next("prev");
}

function next(direction){

   if(direction=="next"){
      index++;
       if(index==totalSlides){
        index=0;
       }
   } 
   else{
           if(index==0){
            index=totalSlides-1;
           }
           else{
            index--;
           }
    }

  for(i=0;i<slides.length;i++){
          slides[i].classList.remove("active");
          
          
  }
  slides[index].classList.add("active");
    setTimeout(next, 3000);
     

}


// scroll to top btn
let myButton=document.querySelector("#myBtn")

window.onscroll=function(){
     scrollFunction();
}
function scrollFunction(){
     if(document.body.scrollTop>20 || document.documentElement.scrollTop>20){
          myButton.style.display="block";

     }
     else{
          myButton.style.display="none";
     }
}



// scroll to top

function topFunction(){
     document.body.scrollTop=0;
     document.documentElement.scrollTop=0;
}



// print year
let newDate= new Date();
let year= document.querySelector(".year").innerHTML=newDate.getFullYear();



// show menu function on click