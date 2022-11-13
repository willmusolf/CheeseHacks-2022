<template>
    <div class="load">
        <div class="dot"></div>
        <div class="dot"></div>
        <div class="dot"></div>
    </div>  
</template>

<script>
  export default {};
</script>

<style>

@keyframes bounce {
  from {
    tranform: scaleX(1.25);
  }
  to {
    transform: translateY(-50px) scaleX(1)
  }
}

body {
    justify-content: center;
    flex-direction: column;
    align-items: center;
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100vh;
    display: flex;
    background-color: #1E1E1E;
}

.load {
    box-sizing: border-box;
    width: 120px;
    height: 75px;
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
}

.dot {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background-color: #7684FF;
    animation: bounce .5s alternate infinite;
}

.dot:nth-child(2) {
  animation-delay: .25s;
}

.dot:nth-child(3) {
  animation-delay: .5s;
}
    
</style>