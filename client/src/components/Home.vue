<template class = "page-wrap">
  <div v-if=loading>
    <Loading />
  </div>
  <div v-else-if=results>
    <Results v-bind:majors="data" />
  </div>
  <div v-else>
    <div class = "upper-section">
        <p class = "degree-text">
        degreemate
          <div class = "header-line"></div>
        </p>
        <p class = "description-text"> 
        Our transcript parser and degree audit algorithm will
        output the majors you are closest to completing. 
        </p>
        <div class = "description-line"></div>
        <div class = "vector-one"></div>
        <div class = "vector-two"></div>
        <img class = "degree-image" src = "../assets/degreeicon.png">
    </div>
    <div class = "lower-section">
        <div class = "upload-box">
            <div class="upload-image-container">
                <img class = "upload-image" src = "../assets/upload-incon.webp">
            </div>
            <div class="upload-selector">
                <input type="file" id="file" name="file-upload-input" />  
            </div>
            <button class = "submit-button" v-on:click="submit()">Submit</button>
        </div>
        <div class = "lower-line"></div>
        <p class = "copyright-text">
          <button style="font-size: 14px; border: none; background-color: Transparent;" v-on:click="update()"><i class="fa fa-refresh"></i></button>
          &nbsp;
          Copyright © 2022 412 LLC
        </p>
    </div>
  </div>
</template>

<script>
import Loading from '@/components/Loading';
import Results from '@/components/Results';

export default {
  name: 'Home',
  components: {
    Loading,
    Results
  },
  data() {
    return {
      msg: 'Hello!',
      data: null,
      loading: false,
      results: false,
      updated: false
    };
  },
  methods: {
    async update() {
      if (!this.updated) {
        require('dotenv').config();

        this.updated = true;
        console.log("Scraping...");
        await fetch("http://{YOUR_IP_HERE}:5000/update", {
          method: 'GET'
        });
      }
    },
    async submit() {
      const formData = new FormData();
      formData.append('file', document.querySelector('input[type="file"]').files[0]);

      if (formData.get('file') === 'undefined') {
        // TODO show error modal
        return;
      }

      this.loading = true;

      await fetch("http://{YOUR_IP_HERE}/update", {
        method: 'POST',
        body: formData
      }).then(response => {
        response.json().then(data => {
          if (data.status) {
            this.loading = false;
            // TODO show error modal
          } else {
            this.loading = false;
            this.data = data;
            this.results = true;
          }
        });
      });
    }
  }
};
</script>

<style>

@keyframes slideInFromLeft {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(0);
  }
}

@keyframes slideInFromRight {
  0% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(0);
  }
}

@keyframes fadeInAnimation {
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
     }
}

.page-wrap {
}

.upper-section {
    position: fixed;
    top: 0%;
    left: 0%;
    width: 100%;
    height: 55%;
    background: linear-gradient(167.15deg, #49179f 9.29%, rgba(64, 64, 64, 0) 300%);
}

.lower-section {
    height: 45%; 
    position: fixed; 
    bottom: 0%;
    left: 0%;
    width: 100%; 
    background-color: #202020;
}

.upload-box {
    position: absolute;
    left: 10%;
    right: 10%;
    top: 25%;
    bottom: 40%;
    display: flex;
    align-items: center;
    background: linear-gradient(132.78deg, #333 37.55%, rgba(187, 187, 187, 0) 165.67%);
    box-shadow: 0px 3px 0px 2px #1C1C1C;
    border-radius: 10px;
    /* animation: 1s ease-out 0s 1 slideInFromLeft; */
    animation: fadeInAnimation ease 3s;
    /* animation-iteration-count: 2;
    animation-fill-mode: forwards; */
}

.header-line {
    position: relative;
    width: 100%;
    top: -55px;

    border: 1px solid rgba(187, 187, 187, 0.42);
}

.lower-line {
    position: fixed;
    width: 100%;
    /* top: 90%; */
    bottom: 40px;

    border: 1px solid rgba(187, 187, 187, 0.42);
}

.copyright-text {
    position: fixed;
    bottom: -8px;
    left: 10px;

    font-family: 'Open Sans';
    font-style: normal;
    font-weight: 400;
    font-size: 15px;
    line-height: 27px;

    color: #444444;
}

.description-text {
    text-align: left;
    inline-size: 500px;
    overflow-wrap: break-word;
    position: absolute;
    width: 497px;
    height: 54px;
    left: 107px;
    top: 172px;

    font-family: 'Open Sans';
    font-style: normal;
    font-weight: 400;
    font-size: 20px;
    line-height: 27px;

    color: #BBBBBB;

    animation: 2.0s ease-out 0s 1 slideInFromRight;
}

.degree-text {
    position: relative;
    width: 106px;
    height: 55px;
    left: 10px;
    top: -50px;

    font-family: 'ChauPhilomeneOne';
    font-style: normal;
    font-weight: 400;
    font-size: 25px;
    line-height: 96px;

    color: #BBBBBB;
}

.description-line {
    position: fixed;
    width: 494px;
    height: 0px;
    left: 107px;
    top: 250px;

    border: 1px solid #BBBBBB;
    animation: 2.0s ease-out 0s 1 slideInFromLeft;
}

.vector-one {
    position: relative;
    width: 100%;
    left: 38%;
    top: 25%;

    border: 1px solid #BBBBBB;
    transform: rotate(-29.48deg);
}

.vector-two {
    position: relative;
    width: 100%;
    left: -20%;
    top: 75%;

    border: 1px solid #BBBBBB;
    transform: rotate(16.97deg);
    
}

.transcript-box {
    position: absolute;
    width: 1100px;
    height: 70px;
    left: 225px;
    top: 40px;

    background: #D9D9D9;
    border-radius: 10px;
    border: 1px solid #929292;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.transcript-box-text {
    position: absolute;
    width: 500px;
    height: 41px;
    left: -125px;
    top: -5px;

    font-family: 'Open Sans';
    font-style: normal;
    font-weight: 400;
    font-size: 20px;
    line-height: 41px;


    color: rgba(68, 68, 68, 0.48);
}

.upload-image {
    position: relative;
    width: 97px;
    left: -11%;
}

.upload-image-container {
    width: 20%;
}

.upload-selector {
    position: relative;
    border-radius: 6px;
    text-align: left;
    left: -75px;
    width: 75%;
    margin: 10px;
    height: 20%;
    align-items: center;
    cursor: pointer;
    background: #202020;
    color: #929292;
    overflow: hidden;

}

.upload-selector input[type="file"] {
  font-family: 'Open Sans';
  font-style: normal;
  font-weight: 400;
  font-size: 15px;
  line-height: 20px;
  position: absolute;
  top: 8px;
  border-radius: 4px;
  width: 96.5%;
  padding: 5px;
}

.upload-selector button {
    font-family: 'Open Sans';
    font-style: normal;
    font-weight: 400;
    font-size: 15px;
    line-height: 20px;
    width: 15%;
    margin: 0 auto;
	  background: black;
	  padding: 10px;
    border-radius: 6px;
    border: 2px solid black;
}

.upload-selector {
	display: inline-block;
	padding: 10px;
}

.upload-selector:hover input[type="file"] {
    background: #929292;
    cursor: pointer;
    color: #202020;
    transition: all 0.5s ease-in-out;
    -moz-transition: all 0.5s ease-in-out;
    -webkit-transition: all 0.5s ease-in-out;
    -o-transition: all 0.5s ease-in-out;
}

.upload-selector input[type="file"]::before {
    font-family: 'Open Sans';
    font-style: normal;
    font-weight: 400;
    font-size: 15px;
    line-height: 20px;
    content: 'Upload your transcript!';
}

.upload-selector input[type="file"]::after {
    display: none;
}

.upload-selector input[type="file"]::-webkit-file-upload-button {
    visibility: hidden;
}

.degree-image {
  position: fixed;
  right: -20px;
  width: 350px;
  top: 250px;
  opacity: 0.85;
}

.submit-button {
  box-sizing: border-box;
  position: relative;
  width: 118px;
  height: 46px;
  left: -45px;

  font-family: 'Open Sans';
  font-style: normal;
  font-weight: 400;
  font-size: 15px;
  line-height: 20px;
  line-height: 27px;
  letter-spacing: -0.02em;
  color: #929292;

  background: #202020;
  border: 0px solid #929292;
  box-shadow: 0px 0px 0px 2px #202020;
  border-radius: 5px;


}

.submit-button:hover {
  background-color:#929292;
  color: #202020;
  transition: 0.5s;
  cursor: pointer;
}

</style>
