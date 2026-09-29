<script>

const input = document.getElementById("fileInput");
const preview = document.getElementById("previewImage");
const form = document.getElementById("uploadForm");

const loader = document.getElementById("loaderBox");
const progressBar = document.getElementById("uploadProgress");
const progressText = document.getElementById("progressText");
const statusText = document.getElementById("statusText");
const scan = document.getElementById("scanEffect");


/* =========================
   IMAGE PREVIEW
========================= */

input.onchange = function(){

    const file = this.files[0];

    if(file){

        preview.src = URL.createObjectURL(file);

        preview.style.display = "block";

    }

};


/* =========================
   UPLOAD PROGRESS + AI SCAN
========================= */

form.onsubmit = function(){

    loader.style.display = "block";

    scan.classList.add("scanning");

    let value = 0;

    progressBar.style.width = "0%";

    progressText.innerHTML = "0%";


    const interval = setInterval(function(){

        value += 2;

        progressBar.style.width = value + "%";

        progressText.innerHTML = value + "%";


        if(value < 35){

            statusText.innerHTML = "Uploading Image...";

        }

        else if(value < 70){

            statusText.innerHTML = "Preparing AI Model...";

        }

        else{

            statusText.innerHTML = "Analyzing Face...";

        }


        if(value >= 100){

            clearInterval(interval);

        }

    },40);

};


/* =========================
   CONFIDENCE BAR
========================= */

window.onload = function(){

    scan.classList.remove("scanning");

    loader.style.display = "none";


    const bar = document.getElementById("bar");


    if(bar){

        const value = parseFloat(
            bar.dataset.confidence
        );


        if(!isNaN(value)){

            setTimeout(function(){

                bar.style.width = value + "%";

            },300);

        }

    }

};

</script>