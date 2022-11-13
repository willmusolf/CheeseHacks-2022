<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style>

@font-face {
  font-family: "OpenSans";
  src: local("OpenSans"),
   url(./fonts/OpenSans/OpenSans-Regular.ttf) format("truetype");

}

@font-face {
  font-family: "ChauPhilomeneOne";
  src: local("ChauPhilomeneOne"),
   url(./fonts/ChauPhilomeneOne/ChauPhilomeneOne-Regular.ttf) format("truetype");

}

@font-face {
  font-family: "Peddana-Regular";
  src: local("Peddana-Regular"),
   url(./fonts/Peddana/Peddana-Regular.ttf) format("truetype");

}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

</style>
