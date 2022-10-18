<template>
  <!--<img alt="Vue logo" src="./assets/logo.png">-->
  <FileUp msg="file upload"/>
</template>

<script>
import FileUp from './components/FileUp.vue'
//import HelloWorld from './components/HelloWorld.vue'
//import CallSM from './components/CallSM.vue'

export default {
  name: 'App',
  components: {
    FileUp,
    //HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
