 // to make artifiligance delay 
   function sleep(milliseconds) {
        const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
    }
    sleep(3000);
    //hide prelodaer
    window.onload=function(){
      let preloader = document.getElementById('preloader');
      preloader.style.display='none';
    };