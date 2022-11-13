<template>
    <div class = "main-wrapper">

      <p class = "degree-text">
          degreemate
        <div class = "header-line"> </div>
      </p>

      <div class = "major-one">
        <a :href="majors.major1page" target = _blank class = "title">{{ majors.major1 }}</a>
        <a :href="majors.major1page" target = _blank class = "title-two">{{ "For more information >" }}</a>
      </div>

      <div class = "major-two">
        <a :href="majors.major2page" target = _blank class = "title">{{ majors.major2 }}</a>
        <a :href="majors.major2page" target = _blank class = "title-two">{{ "For more information >" }}</a>
      </div>

      <div class = "major-three">
        <a :href="majors.major3page" target = _blank class = "title">{{ majors.major3 }}</a>
        <a :href="majors.major3page" target = _blank class = "title-two">{{ "For more information >" }}</a>
      </div>

      <div class = "major-four">
        <a :href="majors.major4page" target = _blank class = "title">{{ majors.major4 }}</a>
        <a :href="majors.major4page" target = _blank class = "title-two">{{ "For more information >" }}</a>
      </div>

      <div class = "major-five">
        <a :href="majors.major5page" target = _blank class = "title">{{ majors.major5 }}</a>
        <a :href="majors.major5page" target = _blank class = "title-two">{{ "For more information >" }}</a>
      </div>

      <div class = "major-six">
        <a :href="majors.major6page" target = _blank class = "title">{{ majors.major6 }}</a>
        <a :href="majors.major6page" target = _blank class = "title-two">{{ "For more information >" }}</a>
      </div>

      <div class = "gen-eds" v-html="majors.bs" >
      </div>

      <div class = "lower-line"></div>
        <p class = "copyright-text">
          Copyright © 2022 412 LLC
        </p>

    </div>
  
  </template>
  
  <script lang="ts">
    export default{
      props: {
        majors: {
          major1: String,
          major2: String,
          major3: String,
          major4: String,
          major5: String,
          major6: String,
          major1page: String,
          major2page: String,
          major3page: String,
          major4page: String,
          major5page: String,
          major6page: String,
          ba: String,
          bs: String
        }
      },
      name: 'Results',
      data() {
        return {

        };
      }
    };
  </script>
    
<style>

@keyframes slideInFromBottom {
  0% {
    transform: translateY(100%);
  }
  100% {
    transform: translateY(0);
  }
}

.lsreq {
  text-align: left;
  font-family: 'Peddana-Regular';
  font-style: normal;
  font-weight: 400;
  line-height: 50px;
  font-size: 42px;
  margin-top: 10px;
  margin-bottom: 10px;
  margin-right: 5px;
  left: 15px;
  color: #FFFFFF;

}

input[type="checkbox"] {
  position: relative;
  text-shadow: 1px 1px 2px white;
}

input[type="checkbox"] label {
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 50%;
  cursor: pointer;
  height: 28px;
  left: 0;
  position: absolute;
  top: 0;
  width: 28px;
}

input[type="checkbox"] label:after {
  border: 2px solid #fff;
  border-top: none;
  border-right: none;
  content: "";
  height: 6px;
  left: 7px;
  opacity: 0;
  position: absolute;
  top: 8px;
  transform: rotate(-45deg);
  width: 12px;
}

input[type="checkbox"]:checked + label {
  background-color: blue;
  border-color: blue;
}

input[type="checkbox"]:checked + label:after {
  opacity: 1;
}

.lsyes {
  font-family: 'Peddana-Regular';
  font-style: normal;
  font-weight: 400;
  line-height: 50px;
  font-size: 28px;
  color: #016fad;
  /* color: #01a23c; */
  text-align: right;
  right: 25px;
  text-shadow: 0px 0px 0x white;
}

.lsno {
  font-family: 'Peddana-Regular';
  text-align: right;
  right: 25px;
  font-style: normal;
  font-weight: 400;

  line-height: 50px;
  font-size: 28px;
  color: #bfbfbf;
  /* color: #94362d; */
  text-shadow: 0px 0px 0px white;
}

a {
  text-decoration: none;
  vertical-align: middle;
  line-height: 5ren;
}

.main-wrapper {
  position: fixed;
  top: 0%;
  left: 0%;
  width: 100%;
  height: 100%;
  background: linear-gradient(167.15deg, #1E1E1E 9.29%, rgba(64, 64, 64, 0) 300%);
}

.title {
  position: absolute;
  inline-size: 1000px; 
  text-align: left;
  overflow: hidden;
  margin: auto;
  left: 25px;

  font-family: 'Peddana-Regular';
  font-style: normal;
  font-weight: 400;
  font-size: 40px;
  line-height: 73px;

  color: #FFFFFF;
}

.title-two {
  position: absolute;
  inline-size: 1000px; 
  text-align: right;
  overflow: hidden;
  margin: auto;
  right: 25px;

  font-family: 'Peddana-Regular';
  font-style: normal;
  font-weight: 400;
  font-size: 40px;
  line-height: 73px;

  color: #016FAD;
}

.header-line {
  position: relative;
  width: 100%;
  top: -55px;

  border: 1px solid rgba(187, 187, 187, 0.42);
}

.major-one {

  box-sizing: border-box;

  position: absolute;
  left: 0%;
  right: 0%;
  top: 0%;
  bottom: 0%;

  width: 934px;
  height: 65px;
  left: 755px;
  top: 125px;

  background: #333333;
  box-shadow: 0px 3px 0px 2px #444444;
  border-radius: 10px;
  transition: all .2s ease-out; 
  animation: 0.5s ease-out 0s 1 slideInFromBottom;

}

.major-one:hover {
  transition: all .2s ease-in; 
  transform: scale(1.05); 
}


.major-two {
  box-sizing: border-box;

  position: absolute;
  left: 0%;
  right: 0%;
  top: 0%;
  bottom: 0%;

  position: relative;
  width: 934px;
  height: 65px;
  left: 755px;
  top: 120px;

  background: #333333;
  box-shadow: 0px 3px 0px 2px #444444;
  border-radius: 10px;
  transition: all .2s ease-out; 
  animation: 0.6s ease-out 0s 1 slideInFromBottom;
}

.major-two:hover {
  transition: all .2s ease-in; 
  transform: scale(1.05); 
}

.major-three {
  box-sizing: border-box;

  position: absolute;
  left: 0%;
  right: 0%;
  top: 0%;
  bottom: 0%;

  position: relative;
  width: 934px;
  height: 65px;
  left: 755px;
  top: 175px;

  background: #333333;
  box-shadow: 0px 3px 0px 2px #444444;
  border-radius: 10px;
  transition: all .2s ease-out; 
  animation: 0.7s ease-out 0s 1 slideInFromBottom;
}

.major-three:hover {
  transition: all .2s ease-in; 
  transform: scale(1.05); 
}

.major-four {
  box-sizing: border-box;

  position: absolute;
  left: 0%;
  right: 0%;
  top: 0%;
  bottom: 0%;

  position: relative;
  width: 934px;
  height: 65px;
  left: 755px;
  top: 230px;

  background: #333333;
  box-shadow: 0px 3px 0px 2px #444444;
  border-radius: 10px;
  transition: all .2s ease-out; 
  animation: 0.8s ease-out 0s 1 slideInFromBottom;
}

.major-four:hover {
  transition: all .2s ease-in; 
  transform: scale(1.05); 
}

.major-five {
  box-sizing: border-box;

  position: absolute;
  left: 0%;
  right: 0%;
  top: 0%;
  bottom: 0%;

  position: relative;
  width: 934px;
  height: 65px;
  left: 755px;
  top: 285px;

  background: #333333;
  box-shadow: 0px 3px 0px 2px #444444;
  border-radius: 10px;
  transition: all .2s ease-out; 
  animation: 0.9s ease-out 0s 1 slideInFromBottom;
}

.major-five:hover {
  transition: all .2s ease-in; 
  transform: scale(1.05); 
}

.major-six {
  box-sizing: border-box;

  position: absolute;
  left: 0%;
  right: 0%;
  top: 0%;
  bottom: 0%;

  position: relative;
  width: 934px;
  height: 65px;
  left: 755px;
  top: 340px;

  background: #333333;
  box-shadow: 0px 3px 0px 2px #444444;
  border-radius: 10px;
  transition: all .2s ease-out; 
  animation: 1s ease-out 0s 1 slideInFromBottom;
}

.major-six:hover {
  transition: all .2s ease-in; 
  transform: scale(1.05); 
}

.gen-eds {
  position: absolute;
  left: 2.6%;
  right: 58.97%;
  top: 7.71%;
  bottom: 9.23%;
  text-align: right;
  vertical-align: middle;
  padding: 17.5px;
  height: 65%;
  margin-top: 65px;
  margin-left: 30px;
  width: 33%;

  background: #333333;
  box-shadow: 0px 3px 0px 2px #444444;
  border-radius: 10px;
  transition: all .2s ease-out; 
}

.gen-eds:hover {
  transition: all .2s ease-in; 
  transform: scale(1.025); 
}

</style>
